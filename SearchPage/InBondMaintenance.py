from time import sleep
from selenium.webdriver.common.by import By
import Base.PositionElement as  BP
from Base.BasePage import BasePage


class InBondMaintenance(BasePage):
    # 进入入库单维护
    def entryInBond(self):
        self.anotherWayToClick(By.XPATH, BP.homePage)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.OCMaintenanceEntry)
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.inBoundEntry)
        sleep(1)

    # 点击修改按钮
    def clickEditBut(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.inBondBut)

    # 编辑入库地址
    def editInBondAddress(self, text):
        self.sendText(text, By.XPATH, BP.inBoundAddress)

    # 编辑联系方式
    def editInBondPhone(self, text):
        self.sendText(text, By.XPATH, BP.inBoundPhone)

    # 编辑备注
    def editInBondRemark(self, text):
        self.sendText(text, By.XPATH, BP.inBondRemark)

    # 编辑需知
    def editInBondMust(self, text):
        self.sendText(text, By.XPATH, BP.inBondMust)

