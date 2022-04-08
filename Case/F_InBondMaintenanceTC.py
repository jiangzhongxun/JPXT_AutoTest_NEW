# coding=utf-8
import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import Base.PositionElement as  BP
from SearchPage.InBondMaintenance import InBondMaintenance
from SearchPage.LogIn import LogIn


class InBondMaintenanceTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        logInEntity = LogIn(cls.driver)
        logInEntity.logInContent('admin')

    # 编辑入库单
    def test01_editInBondContains(self):# 获取登录excel位置
        # 本地调试
        excelPath = r'%s\Data\InBond.xlsx' % sys.path[0]
        # TestRunner联跑
        # excelPath = r'%s\Data\InBond.xlsx' % (os.path.abspath(os.getcwd()) + os.path.sep + '.')
        inBondMainData = InBondMaintenance(self.driver)
        inBondData, length = inBondMainData.readExcel(excelPath)
        inBondMainData.entryInBond()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.inBondBut)))).text), "修改")
        inBondMainData.clickEditBut()
        inBondMainData.editInBondAddress(inBondData['入库单维护'][0]['InBondAddress'])
        inBondMainData.editInBondPhone(inBondData['入库单维护'][0]['InBondPhone'])
        inBondMainData.editInBondRemark(inBondData['入库单维护'][0]['InBondRemark'])
        inBondMainData.editInBondMust(inBondData['入库单维护'][0]['inBondMust'])
        inBondMainData.clickEditBut()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationSuccess)))).text), "修改成功")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
