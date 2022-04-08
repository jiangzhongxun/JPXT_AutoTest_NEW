import string
import random
from time import sleep
from selenium.webdriver.common.by import By
from Base.BasePage import BasePage
import Base.PositionElement as  BP


class OperationCompany(BasePage):
    # 进入客户收发货公司维护
    def operationEnterCompany(self):
        self.rollBackTop()
        self.anotherWayToClick(By.XPATH, BP.OCMaintenanceEntry)
        self.anotherWayToClick(By.XPATH, BP.operationCompany)
        self.driver.implicitly_wait(10)

    # 保存
    def operationAddOREditConsigneeCompanySubmit(self):
        self.leftClick(By.XPATH, BP.operationAddOREditCompanySubmit)

    # 取消
    def operationAddOREditConsigneeCompanyCancel(self):
        self.leftClick(By.XPATH, BP.operationAddOREditCompanyCancel)

    # 点击新增收/发货公司
    def entryOperationAddCompany(self):
        self.anotherWayToClick(By.XPATH, BP.operationAddShipperORConsignee)

    # 输入公司内容
    def operationAddCompanyContains(self, comChiName = None, comEngName = None):
        sleep(1)
        i = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        if comChiName is None:
            self.sendText(r'Chi_%s' % i, By.XPATH, BP.operationAddOREditCompanyName)
        else:
            self.sendText(comChiName, By.XPATH, BP.operationAddOREditCompanyName)
        if comEngName is None:
            self.sendText(r'Eng_%s' % i, By.XPATH, BP.operationAddOREditCompanyEnglishName)
        else:
            self.sendText(comEngName, By.XPATH, BP.operationAddOREditCompanyEnglishName)
        self.sendText(r'Add_%s' % i, By.XPATH, BP.operationAddOREditCompanyAddress)
        self.sendText(r'151%s' % (''.join(random.sample(string.digits, 8))), By.XPATH,
                      BP.operationAddOREditShipperConsigneePhone)

    # 查询已存在的收发货中英文名称
    def getExsitOCName(self):
        sleep(1)
        result = self.getElement(By.XPATH, BP.operationCompanyRepeat)
        text = (''.join(result.text).split("：")[1]).split("\n")
        return text[0], text[1]


    # 跳到尾页
    def jumpToLastPage(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.operationCompanyLastPage)
        sleep(1)
        self.rollToBottom()

    # 修改
    def editOperationCompany(self):
        self.leftClick(By.XPATH, BP.operationCompanyEditButton)

    # 删除
    def deleteOperationCompany(self):
        self.leftClick(By.XPATH, BP.operationCompanyDeleteButton)
        sleep(1)
        self.leftClick(By.XPATH, BP.operationCompanyDeleteSuccess)

    # 取消删除目的站维护数据
    def deletePlusCancelOperationCompany(self):
        self.leftClick(By.XPATH, BP.operationCompanyDeleteButton)
        sleep(1)
        self.leftClick(By.XPATH, BP.operationCompanyDeleteCancel)