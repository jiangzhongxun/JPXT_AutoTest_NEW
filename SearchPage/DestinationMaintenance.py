import string
import random
from time import sleep
from selenium.webdriver.common.by import By
import Base.PositionElement as  BP
from Base.BasePage import BasePage

class DestinationMaintenance(BasePage):
    # 进入目的站维护
    def entryDestMaintenance(self):
        self.anotherWayToClick(By.XPATH, BP.homePage)
        self.anotherWayToClick(By.XPATH, BP.OCMaintenanceEntry)
        self.anotherWayToClick(By.XPATH, BP.OCDestinationMaintenanceEntry)

    # 点击新增目的站按钮
    def entryAddMaintenance(self):
        self.anotherWayToClick(By.XPATH, BP.OCDestinationMaintenanceNewButton)

    # 新增目的站
    def addDestMaintenanceContains(self, DCode = None, DName = None, DEName = None):
        i = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        if DCode is None:
            self.sendText(i, By.XPATH, BP.OCDestinationCode)
        else:
            self.sendText(DCode, By.XPATH, BP.OCDestinationCode)
        if DName is None:
            self.sendText(('目的站中文%s' % i), By.XPATH, BP.OCDestinationName)
        else:
            self.sendText(DName, By.XPATH, BP.OCDestinationName)
        if DEName is None:
            self.sendText(('DEN'+ i.upper()), By.XPATH, BP.OCDestinationEnglishName)
        else:
            self.sendText(DEName, By.XPATH, BP.OCDestinationEnglishName)

    # 获取已存在的目的站信息
    def getExistDC(self):
        result = self.getElement(By.XPATH, BP.OCDestinationRepeat)
        text = ''.join(result.text).split('：')[1]
        DCode = ''.join(text).split('|')[0].strip()
        DName = ''.join(text).split('|')[1].strip()
        DEName = ''.join(text).split('|')[2].strip()
        return DCode,DName,DEName



    # 保存目的站维护
    def saveDestMaintenance(self):
        self.leftClick(By.XPATH, BP.OCDestinationSubmit)

    # 取消目的站维护保存
    def cancelDestMaintenance(self):
        self.leftClick(By.XPATH, BP.OCDestinationCancel)

    # 修改目的站维护数据
    def editDestMaintenance(self):
        self.leftClick(By.XPATH, BP.OCDestinationEdit)

    # 删除目的站维护数据
    def deleteDestMaintenance(self):
        self.leftClick(By.XPATH, BP.OCDestinationDelete)
        sleep(1)
        self.leftClick(By.XPATH, BP.OCDestinationDeleteSuccess)

    # 取消删除目的站维护数据
    def deletePlusCancelDestMaintenance(self):
        self.leftClick(By.XPATH, BP.OCDestinationDelete)
        sleep(1)
        self.leftClick(By.XPATH, BP.OCDestinationDeleteCancel)

    # 跳到尾页
    def destinationLastPage(self):
        self.leftClick(By.XPATH, BP.OCDestinationLastPage)
        sleep(1)



