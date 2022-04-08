# coding=utf-8
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SearchPage.OperationCompany import OperationCompany
from SearchPage.LogIn import LogIn
import Base.PositionElement as  BP


class OperationCustomerCompanyTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        logInEntity = LogIn(cls.driver)
        logInEntity.logInContent('admin')

    # 新增发货公司
    def test01_addShipperCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.operationAddShipperORConsignee)))).text), "新增发货公司")
        operationCompanyData.webDriverWaitCustomClick(BP.operationShipperCompany)
        operationCompanyData.entryOperationAddCompany()
        operationCompanyData.operationAddCompanyContains()
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "操作成功")
        sleep(1)


    # 新增重复发货公司中文名称
    def test02_addShipperComRepeatChi(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        operationCompanyData.webDriverWaitCustomClick(BP.operationShipperCompany)
        comChiName, comEngName = operationCompanyData.getExsitOCName()
        operationCompanyData.entryOperationAddCompany()
        operationCompanyData.operationAddCompanyContains(comChiName=comChiName)
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        operationCompanyData.clickEmptyToCancel()
        sleep(1)


    # 新增重复发货公司英文名称
    def test03_addShipperComRepeatEng(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        operationCompanyData.webDriverWaitCustomClick(BP.operationShipperCompany)
        comChiName, comEngName = operationCompanyData.getExsitOCName()
        operationCompanyData.entryOperationAddCompany()
        operationCompanyData.operationAddCompanyContains(comEngName=comEngName)
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        operationCompanyData.clickEmptyToCancel()
        sleep(1)


    # 新增收货公司
    def test04_addConsigneeCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        operationCompanyData.entryOperationAddCompany()
        operationCompanyData.operationAddCompanyContains()
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "操作成功")
        sleep(1)


    # 新增重复收货公司中文名称
    def test05_addConsigneeComRepeatChi(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        comChiName, comEngName = operationCompanyData.getExsitOCName()
        operationCompanyData.entryOperationAddCompany()
        operationCompanyData.operationAddCompanyContains(comChiName=comChiName)
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        operationCompanyData.clickEmptyToCancel()
        sleep(1)


    # 新增重复收货公司英文名称
    def test06_addConsigneeComRepeatEng(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        comChiName, comEngName = operationCompanyData.getExsitOCName()
        operationCompanyData.entryOperationAddCompany()
        operationCompanyData.operationAddCompanyContains(comEngName=comEngName)
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        operationCompanyData.clickEmptyToCancel()
        sleep(1)


    # 取消新增发货公司
    def test07_addShipperCompanyCancel(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        operationCompanyData.webDriverWaitCustomClick(BP.operationShipperCompany)
        operationCompanyData.entryOperationAddCompany()
        operationCompanyData.operationAddCompanyContains()
        operationCompanyData.operationAddOREditConsigneeCompanyCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.operationAddShipperORConsignee)))).text), "新增发货公司")


    # 取消新增收货公司
    def test08_addConsigneeCompanyCancel(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        operationCompanyData.entryOperationAddCompany()
        operationCompanyData.operationAddCompanyContains()
        operationCompanyData.clickEmptyToCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.operationAddShipperORConsignee)))).text),
                         "新增收货公司")


    # 修改运营公司发货公司
    def test09_editShipperCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationShipperCompany)
        operationCompanyData.jumpToLastPage()
        operationCompanyData.editOperationCompany()
        operationCompanyData.operationAddCompanyContains()
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "操作成功")
        sleep(1)


    # 修改重复运营公司收货公司中文名称
    def test10_editConsigneeCompanyRepeatChi(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        comChiName, comEngName = operationCompanyData.getExsitOCName()
        operationCompanyData.jumpToLastPage()
        operationCompanyData.editOperationCompany()
        operationCompanyData.operationAddCompanyContains(comChiName=comChiName)
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        operationCompanyData.clickEmptyToCancel()
        sleep(1)


    # 修改重复运营公司收货公司英文名称
    def test11_editConsigneeCompanyRepeatEng(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        comChiName, comEngName = operationCompanyData.getExsitOCName()
        operationCompanyData.jumpToLastPage()
        operationCompanyData.editOperationCompany()
        operationCompanyData.operationAddCompanyContains(comEngName=comEngName)
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        operationCompanyData.clickEmptyToCancel()
        sleep(1)


    # 取消运营公司对发货公司的修改
    def test12_editPlusCancelShipperCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationShipperCompany)
        operationCompanyData.jumpToLastPage()
        operationCompanyData.editOperationCompany()
        operationCompanyData.operationAddCompanyContains()
        operationCompanyData.operationAddOREditConsigneeCompanyCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.operationAddShipperORConsignee)))).text), "新增发货公司")


    # 修改运营公司收货公司
    def test13_editConsigneeCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        operationCompanyData.jumpToLastPage()
        operationCompanyData.editOperationCompany()
        operationCompanyData.operationAddCompanyContains()
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "操作成功")
        sleep(1)


    # 修改重复运营公司收货公司中文名称
    def test14_editConsigneeCompanyRepeatChi(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        comChiName, comEngName = operationCompanyData.getExsitOCName()
        operationCompanyData.jumpToLastPage()
        operationCompanyData.editOperationCompany()
        operationCompanyData.operationAddCompanyContains(comChiName=comChiName)
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        operationCompanyData.clickEmptyToCancel()
        sleep(1)


    # 修改重复运营公司收货公司中文名称
    def test15_editConsigneeCompanyRepeatEng(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        comChiName, comEngName = operationCompanyData.getExsitOCName()
        operationCompanyData.jumpToLastPage()
        operationCompanyData.editOperationCompany()
        operationCompanyData.operationAddCompanyContains(comEngName=comEngName)
        operationCompanyData.operationAddOREditConsigneeCompanySubmit()
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyNameOperationSuccess)))).text),
                         "公司名称已存在")
        operationCompanyData.clickEmptyToCancel()
        sleep(1)


    # 取消运营公司对收货公司的修改
    def test16_editPlusCancelConsigneeCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        sleep(1)
        operationCompanyData.jumpToLastPage()
        operationCompanyData.editOperationCompany()
        operationCompanyData.operationAddCompanyContains()
        operationCompanyData.clickEmptyToCancel()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.operationAddShipperORConsignee)))).text), "新增收货公司")
        sleep(1)


    # 删除发货公司
    def test17_deleteShipperCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationShipperCompany)
        operationCompanyData.jumpToLastPage()
        operationCompanyData.deleteOperationCompany()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyDeleteSuccessDetail)))).text), "删除成功")
        sleep(1)


    # 删除收货公司
    def test18_deleteConsigneeCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        sleep(1)
        operationCompanyData.jumpToLastPage()
        operationCompanyData.deleteOperationCompany()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.operationCompanyDeleteSuccessDetail)))).text), "删除成功")
        sleep(1)


    # 取消删除发货公司
    def test19_deletePlusCancelShipperCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationShipperCompany)
        operationCompanyData.jumpToLastPage()
        operationCompanyData.deletePlusCancelOperationCompany()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.operationAddShipperORConsignee)))).text), "新增发货公司")


    # 取消删除收货公司
    def test20_deletePlusCancelConsigneeCompany(self):
        operationCompanyData = OperationCompany(self.driver)
        operationCompanyData.operationEnterCompany()
        sleep(1)
        operationCompanyData.webDriverWaitCustomClick(BP.operationConsigneeCompany)
        operationCompanyData.jumpToLastPage()
        operationCompanyData.deletePlusCancelOperationCompany()
        sleep(1)
        self.assertEqual(((WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, BP.operationAddShipperORConsignee)))).text), "新增收货公司")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
