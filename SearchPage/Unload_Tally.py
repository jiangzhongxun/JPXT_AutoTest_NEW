import random
import time
import os
import sys
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.by import By
from Base.BasePage import BasePage
import Base.PositionElement  as  BP



class unloading_Entry(BasePage):

#卸货理货（管理）
    # 点击卸货理货管理
    def optTallyEntry(self):
        self.leftClick(By.XPATH, BP.Unloading_tally_management)  # 点击卸货理货管理
        time.sleep(1)

    # 点击待卸货理货
    def waitForTally(self):
        self.leftClick(By.XPATH, BP.Tally_tobe_unloaded)

    # 输入体积
    def Volume_path(self):
        self.sendText("30", By.XPATH, BP.Volume)
    # 输入总重量
    def Total_wei(self):
        self.sendText("600", By.XPATH, BP.Total_weight)
    # 输入总件数
    def Total_pack(self):
        self.sendText("700", By.XPATH, BP.Total_package)
    # 选择包装种类
    def Package(self):
        self.leftClick(By.XPATH, BP.Packages)
        self.leftClick(By.XPATH, BP.Protect)
    # 输入长
    def len_path(self):
        self.sendText("1000", By.XPATH, BP.Len)
    # 输入宽
    def Width_path(self):
        self.sendText("2000", By.XPATH, BP.Wid)
    # 输入高
    def Hight_path(self):
        self.sendText("3000", By.XPATH, BP.High)
    # 输入重量
    def Weight_path(self):
        self.sendText("650", By.XPATH, BP.Weig)
    # 输入件数
    def Piece_path(self):
        self.sendText("750", By.XPATH, BP.Piece)
    # 输入有无损坏及异常
    def Damage_path(self):
        self.sendText("无", By.XPATH, BP.Damage_unusual)
    # 点击照片信息
    def Photograph_path(self):
        self.leftClick(By.XPATH, BP.Photograph)
    #添加照片
    def Photograph_Add(self):
        ele = self.driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/button/span/img')  # 点击加号
        ele.click()
        time.sleep(2)
        # send_keys(r"%s%s.jpg" % ('%s\File\ImportFile\\' % sys.path[0], random.randint(1, 16)))
        send_keys(r"%sFile\ImportFile\%s.jpg" % ((os.path.abspath(os.getcwd()) + os.path.sep), random.randint(1, 16)))
        time.sleep(2)
        send_keys("{VK_RETURN}")
    #点击理货确认
    def Cargo_arrived_report(self):
        self.leftClick(By.XPATH, BP.Cargo_arrived)

#卸货理货维护
    def optTallyEntry_weihu(self):
        self.Volume_path()  # 输入体积
        self.Total_wei()  # 输入总重量
        self.Total_pack()  # 输入总件数
        self.Package()  # 选择包装种类
        self.len_path()  # 输入长
        self.Width_path()  # 输入宽
        self.Hight_path()  # 输入高
        self.Weight_path()  # 输入重量
        self.Piece_path()  # 输入件数
        self.Damage_path()  # 输入有无损坏及异常
        time.sleep(1)
        self.Photograph_path()  # 点击照片信息
        self.Photograph_Add()  # 添加照片


#申报运抵（管理）
    # 点击已卸货理货
    def alreadyTally(self):
        self.leftClick(By.XPATH, BP.Tally_loaded)

    # 选择申报状态
    def UnDeclare(self):
        self.leftClick(By.XPATH, BP.Declare_stu)  # 选择运抵申报状态
        time.sleep(1)
        self.leftClick(By.XPATH, BP.UnDeclare)  # 选择未申报运抵
        time.sleep(1)
        self.leftClick(By.XPATH, BP.Tally_status)  # 选择理货状态
        time.sleep(1)
        self.leftClick(By.XPATH, BP.Tally_normal)  # 选择理货正常
        time.sleep(1)
        self.leftClick(By.XPATH, BP.Inquiry)  # 点击查询
    # 点击入库单信息
    def Godown_info(self):
        self.leftClick(By.XPATH, BP.Godownentry_info)
    # 获取运营公司导出入库单的入仓编号
    def getTallyWNo(self):
        result = self.getElement(By.XPATH, BP.Tally_WNo)
        text = ''.join(result.text).split('：')[1]
        return text

    # 获取当前登录的账户
    def getUserOnLoad(self):
        result = self.getElement(By.XPATH, BP.operationLogOutEnter)
        user = ''.join(result.text)
        return user


    # 点击入库单下载
    def Godown_down(self):
        self.leftClick(By.XPATH, BP.Godownentry_down)
        time.sleep(4)
        self.renameFile((self.getTallyWNo() + '入库单.docx'), (self.getTallyWNo() + '入库单' + '-' + self.getUserOnLoad() + '-' + self.timeStrftime() + '.docx'))
        time.sleep(1)
    # 添加照片
    def Photograph_Add_arrive(self):
        ele = self.driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/button/span/img')  # 点击加号
        ele.click()
        time.sleep(2)
        # send_keys(r"%s%s.jpg" % ('%s\File\ImportFile\\' % sys.path[0], random.randint(1, 16)))
        send_keys(r"%sFile\ImportFile\%s.jpg" % ((os.path.abspath(os.getcwd()) + os.path.sep), random.randint(1, 16)))
        send_keys("{VK_RETURN}")
    # 点击运抵申报
    def Cargo_arrived_info(self):
        self.leftClick(By.XPATH, BP.Cargo_arrived)