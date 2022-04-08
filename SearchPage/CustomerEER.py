import pyautogui
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base.BasePage import BasePage
import Base.PositionElement   as  BP
import time

class customerEER(BasePage):
    # 进入货主预约进场界面
    def entryCustomerEEERIn(self):
        self.rollBackTop()
        self.anotherWayToClick(By.XPATH, BP.customerEntryExitRes)   #点击进出场预约
        time.sleep(2)
        self.anotherWayToClick(By.XPATH, BP.customerEEEREntry)    #点击货物预约
        time.sleep(2)

    # 查看详情
    def Examine_part(self):
        self.leftClick(By.XPATH, BP.Examine_particulars)  # 点击查看详情

    # 货物进场预约详情
    def Approach_order(self):
        ele= self.getElement(By.XPATH, BP.Approach_order_detail)
        return ele

    # 点击预约进场按钮
    def clickEEERInBut(self):
        self.webDriverWaitCustomClick(BP.customerEEERIn)

    # 进场预约时间和日期
    def customerEEERIn(self, text):
        self.sendText(text, By.XPATH, BP.customerEEERInNum)
        self.leftClick(By.XPATH, BP.customerEEERInDay)
        self.leftClick(By.XPATH, BP.customerEEERInDaySel)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.customerEEERInTime)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.customerEEERInTimeSel)

    def chepai(self):
        result = self.getElement(By.XPATH, '//div[@class="page"]/div/div[3]/ul/li/div[3]/div/span')
        text = ''.join(result.text).split('：')[1]
        return text


    # 拖拽单票货物
    def dragEntrust(self):
        # 确定拖拽前后位置
        beforeDragPosition = self.driver.find_element_by_xpath(BP.customerEntrustPositionNotSelected)
        afterDragPosition = self.driver.find_element_by_xpath(BP.customerEntrustPositionSelected)
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(beforeDragPosition).perform()
        pyautogui.moveTo(beforeDragPosition.location['x'] + 300, beforeDragPosition.location['y'] + 400)
        # 实现拖拽功能
        pyautogui.dragTo(afterDragPosition.location['x'] + 700, afterDragPosition.location['y'] + 500, duration=1)


    # 拖拽多票货物
    def dragMultiEntrust(self, num):
        try:
            for i in range(num):
                self.dragEntrust()
        except ElementNotVisibleException as ENV:
            print("无足够的货物可预约！")
            print(ENV.args)
            print(str(ENV))
            print(repr(ENV))

    # 将已选货物删除一票
    def deleteOneSelectedEntrust(self):
        self.dragMultiEntrust(2)
        afterDragPosition = self.driver.find_element_by_xpath(BP.customerEntrustPositionNotSelected)
        beforeDragPosition = self.driver.find_element_by_xpath(BP.customerEntrustPositionSelected)
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(beforeDragPosition).perform()
        pyautogui.moveTo(beforeDragPosition.location['x'] + 700, beforeDragPosition.location['y'] + 500)
        # 实现拖拽功能
        pyautogui.dragTo(afterDragPosition.location['x'] + 300, afterDragPosition.location['y'] + 400, duration=1)


    # 提交货物预约
    def submitEEERIn(self):
        element = self.driver.find_element_by_xpath(BP.customerEEERInSubmit)
        self.driver.execute_script("arguments[0].click();", element)

    # 取消货物预约
    def cancelEEERIn(self):
        element = self.driver.find_element_by_xpath(BP.customerEEERInCancel)
        self.driver.execute_script("arguments[0].click();", element)

    # 查看详情
    def seeDetailsButton(self):
        element = self.driver.find_element_by_xpath(BP.customerEEERInSeeDetail)
        self.driver.execute_script("arguments[0].click();", element)

    # 查看详情返回按钮
    def seeDetailsBack(self):
        element = self.driver.find_element_by_xpath(BP.customerEEERInSeeDetailBack)
        self.driver.execute_script("arguments[0].click();", element)