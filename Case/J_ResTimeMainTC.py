# coding=utf-8
import unittest
from time import sleep
import Base.PositionElement as BP
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from SearchPage.LogIn import LogIn
from SearchPage.ResTimeMain import ResTimeMain


class ResTimeMainTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        logInEntity = LogIn(cls.driver)
        logInEntity.logInContent('admin')

    # 编辑提前预约时间
    def test01_editResTimeBeforeIn(self):
        resTimeMainData = ResTimeMain(self.driver)
        resTimeMainData.entryResTime()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.element_to_be_clickable((By.XPATH, BP.resTimeNew)))).text), "新增")
        resTimeMainData.editResTimeBeforeIn()
        resTimeMainData.resTimeBeforeInSave()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, BP.resTimeDetail)))).text), "保存成功")
        sleep(1)

    # 新增预约时间
    def test02_newResTime(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.newResTime()
        resTimeMainData.resTimeSub()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.resTimeDetail)))).text), "操作成功")
        sleep(1)

    # 新增重复预约时间
    def test03_newResTimerRepeat(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.newResTime()
        resTimeMainData.resTimeSub()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.resTimeDetail)))).text), "该时间段已存在")
        sleep(1)
        resTimeMainData.clickEmptyToCancel()

    # 取消新增预约时间
    def test04_newResTimeCancel(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.newResTime()
        resTimeMainData.resTimeCan()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.resTimeNew)))).text), "新增")
        sleep(1)

    # 禁用预约时间
    def test05_disableResTime(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.disableOrEnable()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.resTimeDetail)))).text), "设置成功")
        sleep(1)

    # 启用预约时间
    def test06_enableResTime(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.disableOrEnable()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.resTimeDetail)))).text), "设置成功")
        sleep(1)

    # 编辑预约时间
    def test07_editResTime(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.editResTime()
        resTimeMainData.resTimeSub()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.resTimeDetail)))).text), "操作成功")
        sleep(1)

    # 取消编辑预约时间
    def test08_editResTimeCancel(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.editResTime()
        resTimeMainData.resTimeCan()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.resTimeNew)))).text), "新增")
        sleep(1)

    # 取消删除预约时间
    def test09_deleteResTimeCancel(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.deleteResTime()
        resTimeMainData.deleteResTimeCancel()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.resTimeNew)))).text), "新增")
        sleep(1)

    # 删除预约时间
    def test10_deleteResTime(self):
        resTimeMainData = ResTimeMain(self.driver)
        # resTimeMainData.entryResTime()
        resTimeMainData.deleteResTime()
        resTimeMainData.deleteResTimeConfirm()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.resTimeDetail)))).text), "删除成功")
    sleep(1)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
