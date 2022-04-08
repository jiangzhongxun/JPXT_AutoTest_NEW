# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SearchPage.EntrustOfCustomer import EntrustOfCustomer
from selenium.webdriver.common.by import By
from selenium import webdriver
import Base.PositionElement as BP
import unittest
import os
import time


class Test(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": "%s\File\ExportFile" % os.path.abspath(os.getcwd()) + os.path.sep}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("http://192.168.1.211:8010/login")
        self.driver.maximize_window()
        time.sleep(2)
        # print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:\\develop\\pythonProject\\JPXT_NEW\\test\\screenshot"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:\\develop\\pythonProject\\JPXT_NEW\\', 'test', 'screenshot'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        # self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def test01(self):
        '''检查查询页面展示'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()
        time.sleep(2)
        entrust = addEntrustData.Add_info()
        self.assertEqual(entrust.text, "新增委托信息")

    def test02(self):
        '''新增委托信息-界面展示'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()
        time.sleep(2)
        addEntrustData.Add_info_click()
        entrustText =addEntrustData.Basic_info()
        goodText = addEntrustData.Goods_info()
        time.sleep(1)
        self.assertEqual(entrustText.text, "基本信息")
        self.assertEqual(goodText.text, "商品信息")

    def test03(self):
        '''新增委托信息必填项-2条商品信息-成功'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()     #进入委托界面
        for i in range(1):
            time.sleep(2)
            addEntrustData.Base_info()         #新增基本信息
            addEntrustData.Mustfirst_goodf_info()  # 新增商品信息
            for i in range(1):
                addEntrustData.AddGoods()
                addEntrustData.Mustfirst_goodf_info()  #新增商品信息
            addEntrustData.SaveEntrust()       # 点击提交
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")

    def test04(self):
        '''新增委托所有信息-2条商品信息-成功'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()  # 进入委托界面
        for i in range(1):
            time.sleep(2)
            addEntrustData.Base_info()  # 新增基本信息
            addEntrustData.first_goodf_info()  # 新增商品信息
            for i in range(1):
                addEntrustData.AddGoods()
                addEntrustData.first_goodf_info()  # 新增商品信息
            addEntrustData.SaveEntrust()  # 点击提交
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")

    def test05(self):
        '''新增委托信息-查看信息详情'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()               # 进入委托界面
        time.sleep(2)
        addEntrustData.Check_detail_info()           #点击查看详情
        time.sleep(1)
        fp = addEntrustData.BasicInfo()
        pf= addEntrustData.GOODInfo()
        time.sleep(1)
        self.assertEqual(fp.text, "基本信息")
        self.assertEqual(pf.text, "商品信息")



    def test06(self):
        '''新增委托信息-删除1条商品信息-成功'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()  # 进入委托界面
        for i in range(1):
            time.sleep(2)
            addEntrustData.Base_info()  # 新增基本信息
            addEntrustData.first_goodf_info()  # 新增商品信息
            for i in range(1):
                addEntrustData.AddGoods()
                addEntrustData.first_goodf_info()  # 新增商品信息
        addEntrustData.DeleteGoods()    #点击删除
        addEntrustData.SaveEntrust()  # 点击提交
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")

    def test07(self):
        '''新增委托信息-审核不通过'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.Find_gl()  # 点击查询按钮
        addEntrustData.Goods_stu()    # 点击货物状态
        addEntrustData.Goods_wait_audit()  # 选择待审核
        time.sleep(2)
        addEntrustData.MustFind_gl()  # 点击查询按钮
        time.sleep(2)
        addEntrustData.Audit_button()  # 点击审核按钮
        addEntrustData.No_button() # 点击否
        addEntrustData.FailReason()  # 输入不通过原因
        addEntrustData.Submit()  # 点击提交
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "提交成功")


    def test08(self):
        '''新增委托信息-删除货物信息'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()
        time.sleep(2)
        addEntrustData.MustFind_hz()  #点击查询
        addEntrustData.Goods_stu()             #点击货物状态
        addEntrustData.Auditing_fail()         #选择审核不通过
        addEntrustData.Find_hz()               #点击查询
        time.sleep(2)
        addEntrustData.Delete_Goods()          #点击删除
        time.sleep(2)
        addEntrustData.Delete_Sure()           #点击确定
        ele=WebDriverWait(self.driver, 10,0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "删除成功")

    def test09(self):
        '''新增委托信息-1条商品信息-成功'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()  # 进入委托界面
        for i in range(0, 2):
            time.sleep(2)
            addEntrustData.Base_info()  # 新增基本信息
            addEntrustData.first_goodf_info()  # 新增商品信息
            addEntrustData.SaveEntrust()  # 点击提交
            # addEntrustData.leftClick(By.XPATH, BP.saveEntrustPath)  # 点击提交
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
            self.assertEqual(ele.text, "操作成功")

    def test10(self):
        '''新增委托信息-审核不通过'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.Find_gl()  # 点击查询按钮
        addEntrustData.Goods_stu()  # 点击货物状态
        addEntrustData.Goods_wait_audit()  # 选择待审核
        time.sleep(2)
        addEntrustData.MustFind_gl()  # 点击查询按钮
        time.sleep(2)
        addEntrustData.Audit_button()  # 点击审核按钮
        addEntrustData.No_button()  # 点击否
        addEntrustData.FailReason()  # 输入不通过原因
        addEntrustData.Submit()  # 点击提交
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "提交成功")

    def test11(self):
        '''新增委托信息-审核不通过-修改'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()  # 进入委托界面
        time.sleep(2)
        addEntrustData.MustFind_hz()  # 点击查询
        addEntrustData.Goods_stu()  # 点击货物状态
        addEntrustData.Auditing_fail()  # 选择审核不通过
        time.sleep(2)
        addEntrustData.Find_hz()  # 点击查询
        time.sleep(3)
        addEntrustData.change_info() #点击修改
        time.sleep(2)
        addEntrustData.Refer_INFO()  # 点击提交
        time.sleep(1)
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")

    def test12(self):
        '''新增委托信息-审核通过'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.Find_gl()  # 点击查询按钮
        addEntrustData.Goods_stu()  # 点击货物状态
        addEntrustData.Goods_wait_audit()  # 选择待审核
        time.sleep(1)
        addEntrustData.MustFind_gl()  # 点击查询按钮
        for i in range(0, 2):
            time.sleep(1)
            addEntrustData.Audit_button()  # 点击审核按钮
            addEntrustData.Yes_button()  # 点击是
            time.sleep(2)
            addEntrustData.Timetable()  # 点击发车时间
            addEntrustData.Last_time()  # 选择时间
            addEntrustData.Train_shift()  # 输入班次号
            time.sleep(2)
            addEntrustData.Submit()  # 点击提交
            addEntrustData.MustSubmit()   #二次确认
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
            self.assertEqual(ele.text, "提交成功")


    def test13(self):
        '''新增委托信息-导出入库单'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()  # 进入委托界面
        time.sleep(2)
        addEntrustData.Goods_stu()  # 点击货物状态
        addEntrustData.optEntrust_Pass()  # 选择审核通过
        addEntrustData.Find_hz()  # 点击查询
        time.sleep(1)
        addEntrustData.Warehousing_entry_derive()        #点击入库单导出


    def test14(self):
        '''管理-导出货物清单'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.GoodsListButton()  # 点击导出货物清单
        time.sleep(3)


    def test15(self):
        '''管理-查看信息详情'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()           # 点击业务委托
        time.sleep(1)
        addEntrustData.EntrustDetail()           #点击查看详情
        time.sleep(1)
        jiben= addEntrustData.EntrustBasicInfo()
        shangpin= addEntrustData.EntrustGoodsInfo()
        shenhe = addEntrustData.EntrustExamineInfo()
        fujian = addEntrustData.EntrustEnclosure()
        time.sleep(3)
        self.assertEqual(jiben.text, "基本信息")
        self.assertEqual(shangpin.text, "商品信息")
        self.assertEqual(shenhe.text, "审核信息")
        self.assertEqual(fujian.text, "附件信息")

    def test16(self):
        '''新增待审核信息'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()  # 进入委托界面
        for i in range(0, 4):
            time.sleep(2)
            addEntrustData.Base_info()  # 新增基本信息
            addEntrustData.first_goodf_info()  # 新增商品信息
            addEntrustData.SaveEntrust()  # 点击提交
            # addEntrustData.leftClick(By.XPATH, BP.saveEntrustPath)  # 点击提交
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
            self.assertEqual(ele.text, "操作成功")

    def test17(self):
        '''待审核信息-作废'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.Find_gl()  # 点击查询按钮
        addEntrustData.Goods_stu()  # 点击货物状态
        addEntrustData.Goods_wait_audit()  # 选择待审核
        time.sleep(1)
        addEntrustData.MustFind_gl()  # 点击查询按钮
        time.sleep(1)
        addEntrustData.EntrustDetail()  # 点击查看详情
        time.sleep(1)
        addEntrustData.BlankOut()   #点击作废
        addEntrustData.MustSubmit()  # 二次确认
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")


    def test18(self):
        '''新增委托信息-审核通过'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.Find_gl()  # 点击查询按钮
        addEntrustData.Goods_stu()  # 点击货物状态
        addEntrustData.Goods_wait_audit()  # 选择待审核
        time.sleep(1)
        addEntrustData.MustFind_gl()  # 点击查询按钮
        for i in range(0, 2):
            time.sleep(1)
            addEntrustData.Audit_button()  # 点击审核按钮
            addEntrustData.Yes_button()  # 点击是
            time.sleep(2)
            addEntrustData.Timetable()  # 点击发车时间
            addEntrustData.Last_time()  # 选择时间
            addEntrustData.Train_shift()  # 输入班次号
            time.sleep(2)
            addEntrustData.Submit()  # 点击提交
            addEntrustData.MustSubmit()  # 二次确认
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
            self.assertEqual(ele.text, "提交成功")

    def test19(self):
        '''审核通过-作废'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.Find_gl()  # 点击查询按钮
        addEntrustData.Goods_stu()  # 点击货物状态
        addEntrustData.optEntrust_Pass()  # 选择审核通过
        time.sleep(1)
        addEntrustData.MustFind_gl()  # 点击查询按钮
        time.sleep(1)
        addEntrustData.EntrustDetail()  # 点击查看详情
        time.sleep(1)
        addEntrustData.BlankOut()  # 点击作废
        addEntrustData.MustSubmit()  # 二次确认
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")

    def test20(self):
        '''新增委托信息-审核不通过'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.Find_gl()  # 点击查询按钮
        addEntrustData.Goods_stu()  # 点击货物状态
        addEntrustData.Goods_wait_audit()  # 选择待审核
        time.sleep(2)
        addEntrustData.MustFind_gl()  # 点击查询按钮
        time.sleep(2)
        addEntrustData.Audit_button()  # 点击审核按钮
        addEntrustData.No_button()  # 点击否
        addEntrustData.FailReason()  # 输入不通过原因
        addEntrustData.Submit()  # 点击提交
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "提交成功")


    def test21(self):
        '''审核不通过-作废'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.gl_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.Business_Delegate()  # 点击业务委托
        addEntrustData.Find_gl()  # 点击查询按钮
        addEntrustData.Goods_stu()  # 点击货物状态
        time.sleep(1)
        addEntrustData.Auditing_fail()  # 选择审核不通过
        time.sleep(1)
        addEntrustData.MustFind_gl()  # 点击查询按钮
        time.sleep(1)
        addEntrustData.EntrustDetail()  # 点击查看详情
        time.sleep(1)
        addEntrustData.BlankOut()  # 点击作废
        addEntrustData.MustSubmit()  # 二次确认
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "操作成功")

    def test22(self):
        '''报关资料-上传'''
        addEntrustData = EntrustOfCustomer(self.driver)
        addEntrustData.hz_login(BP.usernamePath, BP.passwordPath, BP.verificationCodePath, BP.loginButtonPath)
        addEntrustData.entry_entrust()  # 进入委托界面
        time.sleep(2)
        addEntrustData.MustFind_hz()  # 点击查询
        addEntrustData.Goods_stu()  # 点击货物状态
        time.sleep(1)
        addEntrustData.optEntrust_Pass()  # 选择审核通过
        time.sleep(1)
        addEntrustData.Find_hz()  # 点击查询
        time.sleep(2)
        addEntrustData.CustomsDeclarationInformation()  # 点击报关资料
        time.sleep(3)
        addEntrustData.AppendicesContract()  #添加合同附件
        time.sleep(1)
        addEntrustData.OtherAccessories()    #添加其他附件
        addEntrustData.TiJiao()  #点击提交
        time.sleep(1)
        ele = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "body > div.ivu-message > div > div > div:nth-child(1) > div > span")))
        self.assertEqual(ele.text, "已提交报关资料")


if __name__ == "__main__":
    unittest.main()
