# coding=utf-8
import unittest
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SearchPage.LogIn import LogIn
from time import sleep
import Base.PositionElement as BP


class LogInTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test01_logIn(self):
        # 获取登录excel位置
        # 本地调试
        excelPath = r'%s\Data\LogIn.xlsx' % sys.path[0]
        # TestRunner联跑
        # excelPath = r'%s\Data\LogIn.xlsx' % (os.path.abspath(os.getcwd()) + os.path.sep + '.')
        logInEntity = LogIn(self.driver)
        account, lenOfUsername = logInEntity.readExcel(excelPath)
        # 循环读取用户名和密码
        for i in range(lenOfUsername):
            logInEntity.logInContent(account['Sheet1'][i]['username'])
            if  account['Sheet1'][i]['username'] == 'huozhu':
                self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
                    EC.visibility_of_element_located((By.XPATH, BP.customerLogOutEnter)))).text), "huozhu")
                sleep(1)
                logInEntity.logOutSys()
            elif account['Sheet1'][i]['username'] == u'李四':
                self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
                    EC.visibility_of_element_located((By.XPATH, BP.customerLogOutEnter)))).text), u"李四")
                sleep(1)
                logInEntity.logOutSys()
            elif account['Sheet1'][i]['username'] == 'admin':
                self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
                    EC.visibility_of_element_located((By.XPATH, BP.operationLogOutEnter)))).text), "admin")
                sleep(1)
                logInEntity.logOutSysOper()
            else:
                print("账户错误")
            sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
