import random
import string
from time import sleep
from Base.BasePage import BasePage
from selenium.webdriver.common.by import By
import Base.PositionElement as  BP


class CameraMain(BasePage):
    # 进入摄像头维护
    def entryCameraMain(self):
        self.rollBackTop()
        self.anotherWayToClick(By.XPATH, BP.homePage)
        self.anotherWayToClick(By.XPATH, BP.OCMaintenanceEntry)
        self.anotherWayToClick(By.XPATH, BP.cameraMain)

    # 点击新增摄像头
    def clickNewCameraMainBut(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.newCameraMainBut)

    # 填写内容
    def cameraMainContains(self, text = None):
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainAFName)
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainAFN1)
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainAFAreaName)
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainAFAN1)
        if text is None:
            self.sendText('camName%s'%(''.join(random.sample(string.ascii_letters, 3))), By.XPATH, BP.cameraMainCName)
        else:
            self.sendText(text, By.XPATH, BP.cameraMainCName)
        self.sendText('127.0.0.1', By.XPATH, BP.cameraMainIP)
        self.sendText('CN%s'%(''.join(random.sample(string.digits, 4))), By.XPATH, BP.cameraMainChannel)
        self.sendText('%s'%(''.join(random.sample(string.ascii_letters, 5))), By.XPATH, BP.cameraMainEquipment)
        self.sendText('root', By.XPATH, BP.cameraMainUserName)
        self.sendText('root', By.XPATH, BP.cameraMainPassword)

    # 获取本存在的摄像头名称
    def getRepeatCameraName(self):
        sleep(1)
        result = self.getElement(By.XPATH, BP.cameraRepeatName)
        text = ''.join(result.text).split(' ')[1]
        return text

    # 点击提交
    def cameraMainBut(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainSubmit)

    # 点击取消
    def cameraMainCan(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainCancel)

    # 修改
    def editCameraMain(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainEdit)

    # 删除
    def deleteCameraMain(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainDelete)

    # 确认删除
    def deleteCameMainConfirm(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainDeleteConfirm)

    # 取消删除
    def deleteCameMainCancel(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainDeleteCancel)

    # 查看详情
    def seeCameMainDetails(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.cameraMainDetail)


