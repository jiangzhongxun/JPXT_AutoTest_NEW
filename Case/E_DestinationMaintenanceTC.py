# coding=utf-8
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Base.PositionElement as  BP
from SearchPage.DestinationMaintenance import DestinationMaintenance
from SearchPage.LogIn import LogIn


class DestinationMaintenanceTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        logInEntity = LogIn(cls.driver)
        logInEntity.logInContent('admin')

    # 新增目的站维护数据
    def test01_addDestinationMaintenance(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        self.driver.implicitly_wait(10)
        DMData.entryAddMaintenance()
        self.driver.implicitly_wait(10)
        DMData.addDestMaintenanceContains()
        DMData.saveDestMaintenance()
        # self.driver.save_screenshot(DMData.exportImagePath('新增目的站'))
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.OCDestinationMaintenanceNewButton)))).text), "新增目的地")
        sleep(1)


    # 新增重复目的站代码数据
    def test02_addDMWithRepeatDCode(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        DCode, DName, DEName = DMData.getExistDC()
        self.driver.implicitly_wait(10)
        DMData.entryAddMaintenance()
        self.driver.implicitly_wait(10)
        DMData.addDestMaintenanceContains(DCode = DCode)
        DMData.saveDestMaintenance()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.OCDestinationDeleteSuccessDetail)))).text), "目的站代码已存在")
        DMData.clickEmptyToCancel()
        sleep(1)

    # 新增重复目的站中文名称数据
    def test03_addDMWithRepeatDName(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        DCode, DName, DEName = DMData.getExistDC()
        self.driver.implicitly_wait(10)
        DMData.entryAddMaintenance()
        self.driver.implicitly_wait(10)
        DMData.addDestMaintenanceContains(DName = DName)
        DMData.saveDestMaintenance()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.OCDestinationDeleteSuccessDetail)))).text), "目的站中文名称已存在")
        DMData.clickEmptyToCancel()
        sleep(1)

    # 新增重复目的站英文名称数据
    def test04_addDMWithRepeatDEName(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        DCode, DName, DEName = DMData.getExistDC()
        self.driver.implicitly_wait(10)
        DMData.entryAddMaintenance()
        self.driver.implicitly_wait(10)
        DMData.addDestMaintenanceContains(DEName = DEName)
        DMData.saveDestMaintenance()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.OCDestinationDeleteSuccessDetail)))).text), "目的站英文名称已存在")
        DMData.clickEmptyToCancel()
        sleep(1)


    # 取消目的站维护数据新增
    def test05_cancelDestinationMaintenance(self):
        DMData = DestinationMaintenance(self.driver)
        self.driver.implicitly_wait(10)
        DMData.entryDestMaintenance()
        self.driver.implicitly_wait(10)
        DMData.entryAddMaintenance()
        DMData.addDestMaintenanceContains()
        sleep(10)
        DMData.cancelDestMaintenance()
        # self.driver.save_screenshot(DMData.exportImagePath('取消新增目的站'))
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.OCDestinationMaintenanceNewButton)))).text), "新增目的地")
        sleep(1)


    # 通过点击抽屉外区域取消目的站维护数据新增
    def test06_clickEmptyDestinationMaintenance(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        self.driver.implicitly_wait(10)
        DMData.entryAddMaintenance()
        self.driver.implicitly_wait(10)
        DMData.addDestMaintenanceContains()
        DMData.clickEmptyToCancel()
        # self.driver.save_screenshot(DMData.exportImagePath('抽屉外取消目的站新增'))
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.OCDestinationMaintenanceNewButton)))).text), "新增目的地")
        sleep(1)


    # 修改目的站维护数据
    def test07_editDestinationMaintenance(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        sleep(1)
        DMData.destinationLastPage()
        DMData.editDestMaintenance()
        DMData.addDestMaintenanceContains()
        DMData.saveDestMaintenance()
        # self.driver.save_screenshot(DMData.exportImagePath('修改目的站'))
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.OCDestinationMaintenanceNewButton)))).text), "新增目的地")
        sleep(1)

    # 编辑重复的目的站代码
    def test08_editDMRepeatDCode(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        DCode, DName, DEName = DMData.getExistDC()
        sleep(1)
        DMData.destinationLastPage()
        DMData.editDestMaintenance()
        DMData.addDestMaintenanceContains(DCode = DCode)
        DMData.saveDestMaintenance()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.OCDestinationDeleteSuccessDetail)))).text),
                         "目的站代码已存在")
        DMData.clickEmptyToCancel()
        sleep(1)

    # 编辑重复的目的站代码
    def test09_editDMRepeatDName(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        DCode, DName, DEName = DMData.getExistDC()
        sleep(1)
        DMData.destinationLastPage()
        DMData.editDestMaintenance()
        DMData.addDestMaintenanceContains(DName = DName)
        DMData.saveDestMaintenance()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.OCDestinationDeleteSuccessDetail)))).text),
                         "目的站中文名称已存在")
        sleep(1)
        DMData.clickEmptyToCancel()


    # 编辑重复的目的站代码
    def test10_editDMRepeatDEName(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        DCode, DName, DEName = DMData.getExistDC()
        sleep(1)
        DMData.destinationLastPage()
        DMData.editDestMaintenance()
        DMData.addDestMaintenanceContains(DEName = DEName)
        sleep(1)
        DMData.saveDestMaintenance()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.OCDestinationDeleteSuccessDetail)))).text), "目的站英文名称已存在")
        sleep(1)
        DMData.clickEmptyToCancel()


    # 取消对目的站维护数据的修改
    def test11_editPlusCancelDestinationMaintenance(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        sleep(1)
        DMData.destinationLastPage()
        DMData.editDestMaintenance()
        DMData.addDestMaintenanceContains()
        DMData.clickEmptyToCancel()
        # self.driver.save_screenshot(DMData.exportImagePath('取消修改目的站'))
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.OCDestinationMaintenanceNewButton)))).text), "新增目的地")
        sleep(1)


    # 删除目的站维护数据
    def test12_deleteDestinationMaintenance(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        sleep(1)
        DMData.destinationLastPage()
        DMData.deleteDestMaintenance()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.OCDestinationDeleteSuccessDetail)))).text), "删除成功")
        # self.driver.save_screenshot(DMData.exportImagePath('删除目的站'))
        sleep(1)


    # 取消对目的站的删除
    def test13_deletePlusCancelDestinationMaintenance(self):
        DMData = DestinationMaintenance(self.driver)
        DMData.entryDestMaintenance()
        sleep(1)
        DMData.destinationLastPage()
        DMData.deletePlusCancelDestMaintenance()
        # self.driver.save_screenshot(DMData.exportImagePath('取消删除目的站'))
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.OCDestinationMaintenanceNewButton)))).text), "新增目的地")
        sleep(1)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
