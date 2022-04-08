# coding=utf-8
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SearchPage.CustomerCompany import CustomerCompany
from SearchPage.LogIn import LogIn
import Base.PositionElement as BP


class CustomerCompanyTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        logInEntity = LogIn(cls.driver)
        logInEntity.logInContent('huozhu')

    # 新增发货公司
    def test01_addShipperCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.addShipperORConsignee)))).text), "新增发货公司")
        customerCompanyData.anotherWayToClick(By.XPATH, BP.shipperCompany)
        customerCompanyData.entryCompanyAddCompany()
        customerCompanyData.addCompanyContains()
        customerCompanyData.addOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyNameOperationSuccess)))).text), "新增成功")
        sleep(1)

    # 新增收货公司
    def test02_addConsigneeCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        customerCompanyData.anotherWayToClick(By.XPATH, BP.consigneeCompany)
        customerCompanyData.entryCompanyAddCompany()
        customerCompanyData.addCompanyContains()
        customerCompanyData.addOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyNameOperationSuccess)))).text), "新增成功")
        sleep(1)

    # 新增重复的发货公司
    def test03_addRepeatSCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        customerCompanyData.anotherWayToClick(By.XPATH, BP.shipperCompany)
        sleep(1)
        repeatCompany = customerCompanyData.getRepeatCompany()
        customerCompanyData.entryCompanyAddCompany()
        customerCompanyData.addCompanyContains(repeatCompany)
        customerCompanyData.addOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyNameOperationSuccess)))).text), "公司名称已存在")
        customerCompanyData.clickEmptyToCancel()
        sleep(1)

    # 新增重复的收货公司
    def test04_addRepeatCCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        customerCompanyData.anotherWayToClick(By.XPATH, BP.consigneeCompany)
        sleep(1)
        repeatCompany = customerCompanyData.getRepeatCompany()
        customerCompanyData.entryCompanyAddCompany()
        customerCompanyData.addCompanyContains(repeatCompany)
        customerCompanyData.addOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        customerCompanyData.clickEmptyToCancel()
        sleep(1)

    # 取消新增发货公司
    def test05_addShipperCompanyCancel(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        customerCompanyData.anotherWayToClick(By.XPATH, BP.shipperCompany)
        customerCompanyData.entryCompanyAddCompany()
        customerCompanyData.addCompanyContains()
        customerCompanyData.addOREditConsigneeCompanyCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.addShipperORConsignee)))).text), "新增发货公司")
        sleep(1)

    # 取消新增收货公司
    def test06_addConsigneeCompanyCancel(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        customerCompanyData.anotherWayToClick(By.XPATH, BP.consigneeCompany)
        customerCompanyData.entryCompanyAddCompany()
        customerCompanyData.addCompanyContains()
        customerCompanyData.clickEmptyToCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.addShipperORConsignee)))).text), "新增收货公司")
        sleep(1)

    # 修改重复的发货公司
    def test07_editRepeatSCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        customerCompanyData.anotherWayToClick(By.XPATH, BP.shipperCompany)
        sleep(1)
        repeatCompany = customerCompanyData.getRepeatCompany()
        customerCompanyData.editCompanyCompany()
        customerCompanyData.addCompanyContains(repeatCompany)
        customerCompanyData.addOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        customerCompanyData.clickEmptyToCancel()
        sleep(1)

    # 修改发货公司
    def test08_editShipperCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        sleep(1)
        customerCompanyData.anotherWayToClick(By.XPATH, BP.shipperCompany)
        customerCompanyData.jumpToLastPage()
        customerCompanyData.editCompanyCompany()
        customerCompanyData.addCompanyContains()
        customerCompanyData.addOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyNameOperationSuccess)))).text),
                         "修改成功")
        sleep(1)

    # 修改重复的收货公司
    def test09_editRepeatCCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        customerCompanyData.anotherWayToClick(By.XPATH, BP.consigneeCompany)
        sleep(1)
        repeatCompany = customerCompanyData.getRepeatCompany()
        customerCompanyData.editCompanyCompany()
        customerCompanyData.addCompanyContains(repeatCompany)
        customerCompanyData.addOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        customerCompanyData.clickEmptyToCancel()
        sleep(1)

    # 取消对发货公司的修改
    def test10_editPlusCancelShipperCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        sleep(1)
        customerCompanyData.anotherWayToClick(By.XPATH, BP.shipperCompany)
        customerCompanyData.jumpToLastPage()
        customerCompanyData.editCompanyCompany()
        customerCompanyData.addCompanyContains()
        customerCompanyData.addOREditConsigneeCompanyCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.addShipperORConsignee)))).text), "新增发货公司")
        sleep(1)

    # 修改运营公司收货公司
    def test11_editConsigneeCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        sleep(1)
        customerCompanyData.anotherWayToClick(By.XPATH, BP.consigneeCompany)
        customerCompanyData.jumpToLastPage()
        customerCompanyData.editCompanyCompany()
        customerCompanyData.addCompanyContains()
        customerCompanyData.addOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyNameOperationSuccess)))).text),
                         "修改成功")
        sleep(1)

    # 取消运营公司对收货公司的修改
    def test12_editPlusCancelConsigneeCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        sleep(1)
        customerCompanyData.anotherWayToClick(By.XPATH, BP.consigneeCompany)
        sleep(1)
        customerCompanyData.jumpToLastPage()
        customerCompanyData.editCompanyCompany()
        customerCompanyData.addCompanyContains()
        customerCompanyData.clickEmptyToCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.addShipperORConsignee)))).text), "新增收货公司")
        sleep(1)

    # 取消删除发货公司
    def test13_deletePlusCancelShipperCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        sleep(1)
        customerCompanyData.anotherWayToClick(By.XPATH, BP.shipperCompany)
        customerCompanyData.jumpToLastPage()
        customerCompanyData.deletePlusCancelCompanyCompany()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.addShipperORConsignee)))).text), "新增发货公司")
        sleep(1)

    # 取消删除收货公司
    def test14_deletePlusCancelConsigneeCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        sleep(1)
        customerCompanyData.anotherWayToClick(By.XPATH, BP.consigneeCompany)
        customerCompanyData.jumpToLastPage()
        customerCompanyData.deletePlusCancelCompanyCompany()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.addShipperORConsignee)))).text), "新增收货公司")
        sleep(1)

    # 删除发货公司
    def test15_deleteShipperCompany(self):
        sleep(1)
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        sleep(1)
        customerCompanyData.anotherWayToClick(By.XPATH, BP.shipperCompany)
        customerCompanyData.jumpToLastPage()
        customerCompanyData.deleteCompanyCompany()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyDeleteSuccessDetail)))).text), "删除成功")
        sleep(1)

    # 删除收货公司
    def test16_deleteConsigneeCompany(self):
        customerCompanyData = CustomerCompany(self.driver)
        customerCompanyData.enterCompany()
        sleep(1)
        customerCompanyData.anotherWayToClick(By.XPATH, BP.consigneeCompany)
        sleep(1)
        customerCompanyData.jumpToLastPage()
        customerCompanyData.deleteCompanyCompany()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.customerCompanyDeleteSuccessDetail)))).text), "删除成功")
        sleep(1)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
