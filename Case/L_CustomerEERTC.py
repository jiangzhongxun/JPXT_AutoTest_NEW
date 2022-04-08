# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Base.PositionElement as  BP
from SearchPage.CustomerEER import customerEER
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import os
import time




class TestHuozhu(unittest.TestCase):
    def setUp(self):
        # pag.FAILSAFE = False
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.1.211:8010/login")
        self.driver.maximize_window()
        time.sleep(2)
        # print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        # self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def test01(self):
        '''进出场预约--界面展示'''
        customerEEERData = customerEER(self.driver)
        customerEEERData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        customerEEERData.entryCustomerEEERIn()    # 进入货主预约进场界面
        jinchang = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[2]/div[1]/div[1]')  # 预约进场
        self.assertEqual(jinchang.text, "预约进场")

    def test02(self):
        '''进出场预约--货物进场预约详情'''
        customerEEERData = customerEER(self.driver)
        customerEEERData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        customerEEERData.entryCustomerEEERIn()  # 进入货主预约进场界面
        customerEEERData.Examine_part()  #点击查看详情
        ele=customerEEERData.Approach_order()
        self.assertEqual(ele.text, "货物进场预约详情")

    def test03(self):
        '''进出场预约--取消货物预约'''
        customerEEERData = customerEER(self.driver)
        customerEEERData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        customerEEERData.entryCustomerEEERIn()  # 进入货主预约进场界面
        customerEEERData.clickEEERInBut()  # 点击预约进场
        time.sleep(1)
        customerEEERData.customerEEERIn(customerEEERData.generateRegistNum())  # 进场预约时间和日期
        customerEEERData.dragEntrust()  # 单票货物拖拽
        customerEEERData.cancelEEERIn()  # 取消货物预约
        jinchang = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[2]/div[1]/div')  # 预约进场
        self.assertEqual(jinchang.text, "预约进场")

    def test04(self):
        '''进出场预约--一票货物'''
        customerEEERData = customerEER(self.driver)
        customerEEERData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        customerEEERData.entryCustomerEEERIn()  # 进入货主预约进场界面
        customerEEERData.clickEEERInBut()   #点击预约进场
        time.sleep(1)
        customerEEERData.customerEEERIn(customerEEERData.generateRegistNum())   # 进场预约时间和日期
        customerEEERData.dragEntrust()      #单票货物拖拽
        customerEEERData.submitEEERIn()     # 提交货物预约
        time.sleep(1)
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")

    def test05(self):
        '''进出场预约--重复预约车'''
        customerEEERData = customerEER(self.driver)
        customerEEERData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        customerEEERData.entryCustomerEEERIn()  # 进入货主预约进场界面
        chepai = customerEEERData.chepai()
        customerEEERData.clickEEERInBut()  # 点击预约进场
        time.sleep(1)
        customerEEERData.customerEEERIn(chepai)  # 进场预约时间和日期
        customerEEERData.dragEntrust()  # 单票货物拖拽
        customerEEERData.submitEEERIn()
        time.sleep(1)
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "该车辆在当前时间段已有预约")


    def test06(self):
        '''进出场预约--两票货物'''
        customerEEERData = customerEER(self.driver)
        customerEEERData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        customerEEERData.entryCustomerEEERIn()  # 进入货主预约进场界面
        customerEEERData.clickEEERInBut()  # 点击预约进场
        time.sleep(1)
        customerEEERData.customerEEERIn(customerEEERData.generateRegistNum())  # 进场预约时间和日期
        customerEEERData.dragMultiEntrust(2)  # 多票货物拖拽
        customerEEERData.submitEEERIn()  # 提交货物预约
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")

    def test07(self):
        '''进出场预约--两票放一票货物'''
        customerEEERData = customerEER(self.driver)
        customerEEERData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        customerEEERData.entryCustomerEEERIn()
        customerEEERData.clickEEERInBut()
        customerEEERData.customerEEERIn(customerEEERData.generateRegistNum())
        customerEEERData.deleteOneSelectedEntrust()
        customerEEERData.submitEEERIn()
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")


if __name__ == "__main__":
    unittest.main()