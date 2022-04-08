import random
import string
from time import sleep
import os
import pyautogui
import sys
from pywinauto.keyboard import send_keys
from selenium.webdriver import ActionChains
import Base.PositionElement as  BP
from selenium.webdriver.common.by import By
from Base.BasePage import BasePage


class PackageManage(BasePage):
    # 进入装箱管理
    def entryPackageMan(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.homePage)
        self.anotherWayToClick(By.XPATH, BP.entryPackageMan)

    # 输入装箱计划头
    def planHead(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.containerTypePack)
        sleep(1)
        self.leftClick(By.XPATH, BP.containerTypePackIndex)  # 选择集装箱类型
        sleep(1)
        self.sendText(self.generateContainerNum(), By.XPATH, BP.containerNum)  # 输入集装箱号
        sleep(1)
        self.leftClick(By.XPATH, BP.packageArea)
        sleep(1)
        self.leftClick(By.XPATH, BP.packageAreaIndex)  # 选择装箱区

    # 输入装箱计划体
    def planBodyAdd(self, length):
        for i in range(length):
            self.dragInEntrustToPackage()
            sleep(1)

    # 修改装箱计划体
    def planBodyEdit(self):
        self.dragOutEntrust()
        sleep(1)

    # 拖拽货物进计划装箱区
    def dragInEntrustToPackage(self):
        beforeDragPosition = self.driver.find_element_by_xpath(BP.waitForPackage)
        afterDragPosition = self.driver.find_element_by_xpath(BP.planArea)
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(beforeDragPosition).perform()
        pyautogui.moveTo(beforeDragPosition.location['x'] + 100, beforeDragPosition.location['y'] + 330)
        # 实现拖拽功能
        pyautogui.dragTo(afterDragPosition.location['x'] + 300, afterDragPosition.location['y'] + 400, duration=1)

    # 拖出货物
    def dragOutEntrust(self):
        afterDragPosition = self.driver.find_element_by_xpath(BP.waitForPackage)
        beforeDragPosition = self.driver.find_element_by_xpath(BP.planArea)
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(beforeDragPosition).perform()
        pyautogui.moveTo(beforeDragPosition.location['x'] + 300, beforeDragPosition.location['y'] + 400)
        sleep(3)
        # 实现拖拽功能
        pyautogui.dragTo(afterDragPosition.location['x'] + 100, afterDragPosition.location['y'] + 330, duration=2)

    # 点击保存装箱计划
    def submitPackagePlan(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.savePackPlan)

    # 点击保存装箱报告
    def submitPackageReport(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.savePackReport)

    # 搜索已申报的装箱计划/装箱报告
    def searchDeclaredPlanOrReport(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.planOrReportStatus)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.planOrReportStatusAlready)
        sleep(1)
        self.leftClick(By.XPATH, BP.planOrReportSearchBut)

    # 点击修改装箱计划/装箱报告
    def clickPackPlanOrReportEdit(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.packPlanOrReportEdit)

    # 点击导出装箱计划/装箱报告
    def clickPackPlanOrReportExport(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.packPlanOrReportExport)
        sleep(4)

    # 点击申报按钮
    def clickDeclare(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.planOrReportDeclare)
        sleep(1)

    # 获取装箱计划/装箱报告的集装箱号
    def getPackConNum(self):
        sleep(1)
        result = self.getElement(By.XPATH, BP.conNumPlanedOrReported)
        conNum = ''.join(result.text)
        return conNum

    # 编辑按钮找不到
    def editButtonNotFound(self):
        try:
            self.getElement(By.XPATH, BP.packPlanOrReportEdit)
            return True
        except:
            return False

    # 切换到装箱计划
    def switchToPlan(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.planPage)

    # 切换到装箱报告
    def switchToReport(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.reportPage)

    # 上传装箱照片
    def uploadReportPhoto(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.reportPhotoUpLoad)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.reportPhotoUpLoadAdd)
        sleep(3)
        send_keys('%s\File\ImportFile' % sys.path[0])
        send_keys("{VK_RETURN}")
        for i in random.sample(range(1, 17), 6):
            send_keys(('"%d.jpg"') % i)
            # send_keys(r'%s\File\ImportFile%s.jpg' %(os.path.abspath(os.getcwd()) + os.path.sep, i))
        send_keys("{VK_RETURN}")
        sleep(1)

    # 保存上传的装箱照片
    def saveReportPhoto(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.reportPhotoUpLoadSubmit)

    # 打开随车附件
    def entryTrainAccessor(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.withTrainAccessor)

    # 填写随车附件数据
    def withTrainAccessorContains(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.consigneeEngAddress)
        sleep(1)
        self.leftClick(By.XPATH, BP.consigneeEngAddressFirst)
        sleep(1)
        self.sendText(random.randint(10000000, 100000000), By.XPATH, BP.invoiceNo)
        sleep(1)
        self.leftClick(By.XPATH, BP.containerDestineStation)
        sleep(1)
        self.leftClick(By.XPATH, BP.containerDestineStationFirst)
        sleep(1)
        self.leftClick(By.XPATH, BP.saveWithTrainAccessor)

    def exportWithTrainAccessor(self):
        sleep(2)
        self.leftClick(By.XPATH, BP.exportAccessor)
        sleep(5)
        self.leftClick(By.XPATH, BP.exportStuffingList)
        sleep(5)

    # 切换到堆存管理
    def switchToStorageMan(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.entryStorageMan)

    # 导出移位计划
    def exportPackMovePlan(self, text):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.shiftPlan)
        sleep(1)
        self.sendText(text, By.XPATH, BP.packMovePlanExportConNum)
        self.leftClick(By.XPATH, BP.packMovePlanExportConNumSearch)
        sleep(1)
        self.leftClick(By.XPATH, BP.packMovePlanExport)
        sleep(4)

    # 取消导出移位计划
    def cancelMovePlan(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.movePlanCancel)

    # 计划确认
    def confirmPackagePlan(self, text):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.packagePlanConfirm)  # 打开装箱计划确认弹窗
        sleep(1)
        self.sendText(text, By.XPATH, BP.packPlanConfirmConNum)
        self.leftClick(By.XPATH, BP.packPlanConfirmSearch)  # 输入集装箱号查询
        sleep(1)
        self.leftClick(By.XPATH, BP.packActualArea)
        sleep(1)
        self.leftClick(By.XPATH, BP.packActualAreaIndex2)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.packPlanConfirmSubmit)

    # 退出计划确认/移位计划导出
    def cancelConfirmOrExport(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.packPlanConfirmCancel)