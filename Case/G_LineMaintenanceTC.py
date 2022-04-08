# coding=utf-8
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Base.PositionElement as  BP
from SearchPage.LineMaintenance import LineMaintenance
from SearchPage.LogIn import LogIn
from selenium.webdriver.support import expected_conditions as EC


class LineMaintenanceTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        logInEntity = LogIn(cls.driver)
        logInEntity.logInContent('admin')

    # 新增线路维护——始发地默认西安
    def test01_addLineMainDFXA(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.newLineMain)))).text), "新增线路")
        lineMainData.entryNewLine()
        lineMainData.addLineDFXA()
        lineMainData.saveLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "操作成功")
        sleep(1)


    # 新增线路维护
    def test02_addLineMaintenance(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.entryNewLine()
        lineMainData.addLineContains()
        lineMainData.saveLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "操作成功")
        sleep(1)

    # 新增重复线路
    def test03_addLineMainRepeatLine(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainStart, lineMainEnd, lineMainCode= lineMainData.getExistLineData()
        lineMainData.entryNewLine()
        lineMainData.addLineContains(lineMainStart = lineMainStart, lineMainEnd = lineMainEnd)
        lineMainData.saveLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "该线路已存在")
        lineMainData.clickEmptyToCancel()
        sleep(1)

    # 新增重复线路代码
    def test04_addLineMainRepeatLineCode(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainStart, lineMainEnd, lineMainCode= lineMainData.getExistLineData()
        lineMainData.entryNewLine()
        lineMainData.addLineContains(lineMainCode = lineMainCode)
        lineMainData.saveLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "线路代码重复！")
        lineMainData.clickEmptyToCancel()
        sleep(1)


    # 取消新增线路
    def test05_cancelLineMaintenance(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.entryNewLine()
        lineMainData.addLineContains()
        lineMainData.cancelLineMain()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.newLineMain)))).text), "新增线路")


    # 抽屉取消新增线路
    def test06_clickEmptyCancelLineMain(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.entryNewLine()
        lineMainData.addLineContains()
        lineMainData.clickEmptyToCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.newLineMain)))).text), "新增线路")


    # 停用/启用线路
    def test07_disableOREnable(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.disableOREnable()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "设置成功")
        sleep(1)


    # 启用/停用线路
    def test08_enableORDisable(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.disableOREnable()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "设置成功")
        sleep(1)



    # 修改线路维护
    def test09_editLineMaintenance(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.editLineMain()
        lineMainData.saveLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "操作成功")
        sleep(1)

    # 修改重复线路代码
    def test10_editLineMainRepeatLine(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainStart, lineMainEnd, lineMainCode = lineMainData.getExistLineData()
        lineMainData.editLineMain(lineMainCode)
        lineMainData.saveLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "线路代码重复！")
        lineMainData.clickEmptyToCancel()
        sleep(1)


    # 取消修改线路维护
    def test11_editPlusCancelLineMain(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.editLineMain()
        lineMainData.clickEmptyToCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.newLineMain)))).text), "新增线路")


    # 取消删除线路
    def test12_deletePlusCancelLineMain(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.deletePlusCancelLineMain()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.newLineMain)))).text), "新增线路")


    # 删除线路
    def test13_deleteLineMaintenance(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.deleteLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "删除成功")
        sleep(1)

    def test14_deleteLineMainAgain(self):
        lineMainData = LineMaintenance(self.driver)
        lineMainData.entryLineMain()
        lineMainData.deleteLineMain()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.lineMainDetail)))).text), "删除成功")
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()