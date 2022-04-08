from time import sleep
from pymouse import PyMouse
from selenium.webdriver.common.by import By
import Base.PositionElement as BP
from Base.BasePage import BasePage


class ResTimeMain(BasePage):
    # 进入预约时间维护
    def entryResTime(self):
        self.rollBackTop()
        self.anotherWayToClick(By.XPATH, BP.homePage)
        self.anotherWayToClick(By.XPATH, BP.OCMaintenanceEntry)
        self.anotherWayToClick(By.XPATH, BP.resTimeEntry)

    # 修改提前预约进场时间
    def editResTimeBeforeIn(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.resTimeBeforeIn)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.resTimeBeforeInSec48)

    # 保存提前预约进场时间
    def resTimeBeforeInSave(self):
        self.anotherWayToClick(By.XPATH, BP.resTimeBeforeInSave)

    # 取消预约时间控件
    @staticmethod
    def canTimePlugIn():
        sleep(1)
        PyMouse().click(1550, 550)

    # 新增进场时间
    def newResTime(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.resTimeNew)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.resTimeBut)
        self.anotherWayToClick(By.XPATH, BP.resTimeStart)
        self.anotherWayToClick(By.XPATH, BP.resTimeEnd)
        self.canTimePlugIn()

    # 提交进场时间
    def resTimeSub(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.resTimeSub)

    # 取消新增/编辑
    def resTimeCan(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.resTimeCancel)

    # 停用/启用预约时间
    def disableOrEnable(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.resTimeEnOrDisable)

    # 编辑预约时间
    def editResTime(self):
        self.anotherWayToClick(By.XPATH, BP.resTimeEdit)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.resTimeBut)
        self.anotherWayToClick(By.XPATH, BP.resTimeStart2)
        self.anotherWayToClick(By.XPATH, BP.resTimeEnd2)
        self.canTimePlugIn()

    # 删除预约时间
    def deleteResTime(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.resTimeDelete)

    # 确认删除
    def deleteResTimeConfirm(self):
        sleep(2)
        self.anotherWayToClick(By.XPATH, BP.resTimeDeleteConfirm)
        sleep(1)

    # 取消删除
    def deleteResTimeCancel(self):
        sleep(5)
        self.anotherWayToClick(By.XPATH, BP.resTimeDeleteCancel)
        sleep(1)
