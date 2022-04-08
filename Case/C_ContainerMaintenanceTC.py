# coding=utf-8
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from SearchPage.ContainerMaintenance import ContainerMaintenance
from selenium.webdriver.support import expected_conditions as EC
from SearchPage.LogIn import LogIn
import Base.PositionElement as BP
import Base.SQLStatement as SS


class ContainerMaintenanceTC(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        logInEntity = LogIn(cls.driver)
        logInEntity.logInContent('admin')

    # 新增箱型
    def test01_addContainer(self):
        conMainData = ContainerMaintenance(self.driver)
        conMainData.containerMainEntry()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.containerTypeNewBut)))).text), "新增箱型")
        conMainData.clickAddContainerBut()
        conMainData.addContainerContains()
        conMainData.containerSub()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.containerDetail)))).text), "操作成功")
        sleep(1)

    # 新增重复集装箱
    def test02_addRepeatContainer(self):
        conMainData = ContainerMaintenance(self.driver)
        conMainData.containerMainEntry()
        repeatContainerType = conMainData.getRepeatContainerType()
        conMainData.clickAddContainerBut()
        conMainData.addContainerContains(repeatContainerType)
        conMainData.containerSub()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.containerDetail)))).text), "集装箱规格已存在")
        sleep(1)

    # 点击 × 取消新增
    def test03_addContainerCancel(self):
        conMainData = ContainerMaintenance(self.driver)
        conMainData.containerMainEntry()
        conMainData.clickAddContainerBut()
        conMainData.addContainerContains()
        conMainData.containerAddCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.containerTypeNewBut)))).text), "新增箱型")
        sleep(1)

    # 点击抽屉外区域取消新增
    def test04_addContainerClickEmpty(self):
        conMainData = ContainerMaintenance(self.driver)
        conMainData.containerMainEntry()
        conMainData.clickAddContainerBut()
        conMainData.addContainerContains()
        conMainData.clickEmptyToCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.containerTypeNewBut)))).text), "新增箱型")
        sleep(1)

    # 编辑集装箱规格
    def test05_editContainer(self):
        conMainData = ContainerMaintenance(self.driver)
        conMainData.containerMainEntry()
        conMainData.clickContainerEdit()
        conMainData.addContainerContains()
        conMainData.containerSub()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.containerDetail)))).text), "操作成功")
        sleep(1)

    # 编辑重复集装箱
    def test06_editRepeatContainer(self):
        conMainData = ContainerMaintenance(self.driver)
        conMainData.containerMainEntry()
        repeatContainerType = conMainData.getRepeatContainerType()
        conMainData.clickContainerEdit()
        conMainData.addContainerContains(repeatContainerType)
        conMainData.containerSub()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.containerDetail)))).text), "集装箱规格已存在")
        sleep(1)

    # 取消编辑集装箱规格
    def test07_editContainerCancel(self):
        conMainData = ContainerMaintenance(self.driver)
        conMainData.containerMainEntry()
        conMainData.clickContainerEdit()
        conMainData.addContainerContains()
        conMainData.containerAddCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.containerTypeNewBut)))).text), "新增箱型")

    # 由于集装箱规格没有删除功能，因此需要删除此次测试创建的数据
    def test08_deleteSQLData(self):
        conMainData = ContainerMaintenance(self.driver)
        conMainData.connectMySQL(SS.containerTypeDelete)
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
