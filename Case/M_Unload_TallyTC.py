# coding=utf-8
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from SearchPage.EntrustOfCustomer import EntrustOfCustomer
from SearchPage.Unload_Tally import unloading_Entry
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Base.PositionElement as  BP
import unittest
import os


class Test(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": "%s\File\ExportFile" %  os.path.abspath(os.getcwd()) + os.path.sep}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("http://192.168.1.210:8010/login")
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
        '''卸货理货'''
        unEntrustData = unloading_Entry(self.driver)
        unEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        unEntrustData.optTallyEntry()               # 点击卸货理货管理
        for i in range(4):
            time.sleep(1)
            unEntrustData.optTallyEntry_weihu()         #卸货理货维护
            time.sleep(1)
            unEntrustData.Cargo_arrived_report()         # 点击理货确认
            time.sleep(2)
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
            self.assertEqual(ele.text, "已确认理货")


    def test02(self):
        '''确认理货正常'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()
        for i in range(4):
            time.sleep(2)
            addEntrustData.Freight_forward_Stu()      #点击理货状态
            time.sleep(1)
            addEntrustData.Tally_abnorma_path()        #选择理货异常
            time.sleep(1)
            addEntrustData.tally_query()           #点击查询
            time.sleep(2)
            addEntrustData.tally_info()            #点击理货信息
            time.sleep(2)
            addEntrustData.tally_sure()            #点击理货确认
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
            self.assertEqual(ele.text, "已确认理货信息")

    def test03(self):
        '''申报运抵'''
        unEntrustData = unloading_Entry(self.driver)
        unEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        unEntrustData.optTallyEntry()             # 选择卸货理货管理
        unEntrustData.alreadyTally()              # 选择已卸货理货
        time.sleep(1)
        for i in range(4):
            unEntrustData.UnDeclare()                 #选择申报状态
            time.sleep(1)
            unEntrustData.Godown_info()               # 点击入库单信息
            unEntrustData.Godown_down()                # 点击入库单下载
            time.sleep(10)
            unEntrustData.Photograph_Add_arrive()      #添加照片
            time.sleep(3)
            unEntrustData.Cargo_arrived_info()         # 点击运抵申报
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
            self.assertEqual(ele.text, "已申报运抵")


if __name__ == "__main__":
    unittest.main()