import random
from time import sleep
from selenium.webdriver.common.by import By
import Base.PositionElement as BP
from Base.BasePage import BasePage


class ContainerMaintenance(BasePage):
    typeList = ['GP', 'GH', 'HC', 'HQ', 'HT', 'OT', 'RF', 'RH', 'TK', 'FR']
    sizeList = ['20', '40', '45']

    # 进入集装箱维护
    def containerMainEntry(self):
        self.rollBackTop()
        self.anotherWayToClick(By.XPATH, BP.homePage)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.OCMaintenanceEntry)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.containerType)
        self.driver.implicitly_wait(10)

    # 点击新增按钮
    def clickAddContainerBut(self):
        self.webDriverWaitCustomClick(BP.containerTypeNewBut)

    # 填写集装箱内容
    def addContainerContains(self, text=None):
        sleep(1)
        if text is None:
            conSpecificationData = ''.join(random.sample(self.sizeList, 1)) + ''.join(random.sample(self.typeList, 1))
            self.sendText(conSpecificationData, By.XPATH, BP.conSpecifications)
        else:
            self.sendText(text, By.XPATH, BP.conSpecifications)
        self.sendText('%d' % random.randint(200000, 500000), By.XPATH, BP.containerWeight)
        self.sendText('%d' % random.randint(20, 50), By.XPATH, BP.containerVolume)
        self.sendText('%d' % random.randint(7000, 9999), By.XPATH, BP.containerTare)

    # 获取已存在的集装箱型号
    def getRepeatContainerType(self):
        sleep(1)
        result = self.getElement(By.XPATH, BP.containerRepeat)
        text = ''.join(result.text).split('：')[1]
        return text

    # 提交新增/编辑
    def containerSub(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.containerSubmit)

    # 取消新增/编辑
    def containerAddCancel(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.containerCancel)

    # 点击编辑
    def clickContainerEdit(self):
        sleep(1)
        self.rollToBottom()
        self.leftClick(By.XPATH, BP.containerEditBut)
