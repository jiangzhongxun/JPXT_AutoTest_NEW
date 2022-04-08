import random
import string
from time import sleep
from selenium.webdriver.common.by import By
from Base.BasePage import BasePage
import Base.PositionElement as BP


class CustomerCompany(BasePage):
    # 进入客户收发货公司维护
    def enterCompany(self):
        self.rollBackTop()
        self.anotherWayToClick(By.XPATH, BP.customerCompanyManage)
        self.anotherWayToClick(By.XPATH, BP.customerCompany)
        sleep(1)

    # 保存
    def addOREditConsigneeCompanySubmit(self):
        self.leftClick(By.XPATH, BP.addOREditCompanySubmit)

    # 取消
    def addOREditConsigneeCompanyCancel(self):
        self.leftClick(By.XPATH, BP.addOREditCompanyCancel)

    # 点击新增收/发货公司
    def entryCompanyAddCompany(self):
        sleep(1)
        self.anotherWayToClick(By.XPATH, BP.addShipperORConsignee)

    # 输入公司内容
    def addCompanyContains(self, text=None):
        sleep(1)
        i = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        if text is None:
            self.sendText(r'Chi_%s' % i, By.XPATH, BP.addOREditCompanyName)
        else:
            self.sendText(text, By.XPATH, BP.addOREditCompanyName)
        self.sendText(r'Add_%s' % i, By.XPATH, BP.addOREditCompanyAddress)
        self.sendText(r'NM_%s' % i, By.XPATH, BP.addOREditShipperConsigneeName)
        self.sendText(r'151%s' % (''.join(random.sample(string.digits, 8))), By.XPATH,
                      BP.addOREditShipperConsigneePhone)
        self.sendText(r'%s@qq.com' % (''.join(random.sample(string.digits, 8))), By.XPATH,
                      BP.addOREditShipperConsigneeEmail)

    # 获取重复的公司名称
    def getRepeatCompany(self):
        sleep(1)
        result = self.getElement(By.XPATH, BP.customerCompanyRepeat)
        text = ''.join(result.text).split('：')[1]
        return text


    # 跳转尾页
    def jumpToLastPage(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.customerCompanyLastPage)
        sleep(1)
        self.rollToBottom()

    # 修改
    def editCompanyCompany(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.customerCompanyEditButton)

    # 删除
    def deleteCompanyCompany(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.customerCompanyDeleteButton)
        sleep(1)
        self.leftClick(By.XPATH, BP.customerCompanyDeleteSuccess)

    # 取消删除
    def deletePlusCancelCompanyCompany(self):
        self.leftClick(By.XPATH, BP.customerCompanyDeleteButton)
        sleep(1)
        self.leftClick(By.XPATH, BP.customerCompanyDeleteCancel)