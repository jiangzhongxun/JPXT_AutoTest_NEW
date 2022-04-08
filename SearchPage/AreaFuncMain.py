import random
import string
from time import sleep
from selenium.webdriver.common.by import By
import Base.PositionElement as  BP
from Base.BasePage import BasePage


class AreaFuncMain(BasePage):
    # 进入功能区维护
    def entryAreaFunc(self):
        self.anotherWayToClick(By.XPATH, BP.homePage)
        self.anotherWayToClick(By.XPATH, BP.OCMaintenanceEntry)
        self.anotherWayToClick(By.XPATH, BP.areaFunction)

    # 点击新增功能区
    def clickAddAreaFunc(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.addAreaFunctionBut)

    # 获取已存在的功能区名称
    def getACName(self):
        sleep(1)
        result = self.getElement(By.XPATH, BP.areFunctionRepeatName)
        text = ''.join(result.text).split('：')[1]
        return text

    # 填写功能区内容
    def areaFuncContainsNoRemark(self, text=None):
        sleep(1)
        if text is None:
            self.sendText(r'功能区%d' % random.randint(1, 100), By.XPATH, BP.areaFunctionName)
        else:
            self.sendText(text, By.XPATH, BP.areaFunctionName)
        self.leftClick(By.XPATH, BP.areaFunctionType)
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionTypeSec)

    # 填写备注信息
    def areaFuncRemark(self):
        sleep(1)
        self.sendText(u'这是一个没有意义的备注信息', By.XPATH, BP.areaFunctionRemark)

    # 编辑功能区
    def areaFuncContainsEdit(self, text=None):
        self.jumpToLastPage()
        sleep(1)
        if text is None:
            self.sendText(r'功能区%d' % random.randint(1, 100), By.XPATH, BP.areaFunctionName)
        else:
            self.sendText(text, By.XPATH, BP.areaFunctionName)

    # 保存功能区
    def areaFuncSub(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionBut)

    # 取消区域操作
    def areaFuncCancel(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionCancel)

    # 点击作业区信息
    def clickAreaFunctionInfo(self):
        self.jumpToLastPage()
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionInfo)

    # 添加作业区
    def clickAreaFuncInfoNew(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFuncInfoNew)

    # 获取已存在的作业区名称
    def getACInfoName(self):
        sleep(1)
        result = self.getElement(By.XPATH, BP.areaFuncInfoRepeatName)
        text = ''.join(result.text).strip()
        return text

    # 新增放行区
    def areaFuncInfoRelContains(self, AFNameText=None, NumberName=None):
        if AFNameText is None:
            self.sendText(u'区域名称%s' % ((''.join(random.sample(string.ascii_letters, 1))).upper()), By.XPATH,
                          BP.areaFuncInfoAreaName)
        else:
            self.sendText(AFNameText, By.XPATH, BP.areaFuncInfoAreaName)
        self.sendText('10', By.XPATH, BP.areaFuncInfoMaxCol)
        self.sendText('16', By.XPATH, BP.areaFuncInfoMaxRow)
        self.leftClick(By.XPATH, BP.areaFuncInfoAreaType)
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFuncInfoAreaRel)
        if NumberName is None:
            NumName = (''.join(random.sample(string.ascii_letters, 1))).upper() + ''.join(
                random.sample(string.digits, 2))
            self.sendText(NumName, By.XPATH, BP.areaFuncInfoAreaNum)
        else:
            self.sendText(NumberName, By.XPATH, BP.areaFuncInfoAreaNum)

    # 编辑放行区
    def areaFuncInfoRelEdit(self):
        self.sendText(u'区域名称%s' % ((''.join(random.sample(string.ascii_letters, 1))).upper()), By.XPATH,
                      BP.areaFuncInfoAreaName)
        self.sendText('2', By.XPATH, BP.areaFuncInfoMaxCol)
        self.sendText('16', By.XPATH, BP.areaFuncInfoMaxRow)

    # 新增查验区
    def areaFuncInfoCheckContains(self):
        self.sendText(u'区域名称%s' % ((''.join(random.sample(string.ascii_letters, 1))).upper()), By.XPATH,
                      BP.areaFuncInfoAreaName)
        self.sendText('9', By.XPATH, BP.areaFuncInfoMaxCol)
        self.sendText('1', By.XPATH, BP.areaFuncInfoMaxRow)
        self.leftClick(By.XPATH, BP.areaFuncInfoAreaType)
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFuncInfoAreaCheck)
        self.sendText('%s%s' % (((
            ''.join(random.sample(string.ascii_letters, 1))).upper()), (''.join(random.sample(string.digits, 2)))),
                      By.XPATH,
                      BP.areaFuncInfoAreaNum)

    # 编辑查验区
    def areaFuncInfoCheckEdit(self, text=None):
        if text is None:
            self.sendText(u'区域名称%s' % ((''.join(random.sample(string.ascii_letters, 1))).upper()), By.XPATH,
                          BP.areaFuncInfoAreaName)
        else:
            self.sendText(text, By.XPATH, BP.areaFuncInfoAreaName)
        self.sendText('9', By.XPATH, BP.areaFuncInfoMaxCol)
        self.sendText('1', By.XPATH, BP.areaFuncInfoMaxRow)

    # 编辑/保存作业区
    def areaFuncInfoSub(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionInfoEdit)

    # 取消编辑作业区
    def areaFunctionInfoCancel(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionInfoEditCancel)

    # 删除作业区
    def areaFuncInfoDelete(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionInfoDelete)

    # 配置放行区行列信息
    def areaFuncInfoRelMatrix(self):
        sleep(2)
        rowNumList = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                      'X', 'Y', 'Z']
        sampleLetter = ''.join(random.sample(rowNumList, 1))
        self.sendText('%s01' % sampleLetter, By.XPATH, BP.areaFunctionInfoFirst)
        self.sendText('%s02' % sampleLetter, By.XPATH, BP.areaFunctionInfoSecond)
        self.sendText('%s03' % sampleLetter, By.XPATH, BP.areaFunctionInfoThird)
        self.sendText('%s04' % sampleLetter, By.XPATH, BP.areaFunctionInfoForth)
        self.sendText('%s05' % sampleLetter, By.XPATH, BP.areaFunctionInfoFifth)
        self.sendText('%s06' % sampleLetter, By.XPATH, BP.areaFunctionInfoSixth)
        self.sendText('%s07' % sampleLetter, By.XPATH, BP.areaFunctionInfoSeventh)
        self.sendText('%s08' % sampleLetter, By.XPATH, BP.areaFunctionInfoEighth)
        self.sendText('%s09' % sampleLetter, By.XPATH, BP.areaFunctionInfoNinth)
        self.sendText('%s10' % sampleLetter, By.XPATH, BP.areaFunctionInfoTenth)
        self.sendText('%s11' % sampleLetter, By.XPATH, BP.areaFunctionInfoEleventh)
        self.sendText('%s12' % sampleLetter, By.XPATH, BP.areaFunctionInfoTwelfth)
        self.sendText('%s13' % sampleLetter, By.XPATH, BP.areaFunctionInfoThirteen)
        self.sendText('%s14' % sampleLetter, By.XPATH, BP.areaFunctionInfoFourteenth)
        self.sendText('%s15' % sampleLetter, By.XPATH, BP.areaFunctionInfoFifteenth)
        self.sendText('%s16' % sampleLetter, By.XPATH, BP.areaFunctionInfoSixteenth)

    # 保存作业区行列信息
    def areaFuncInfoMatrixSub(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionInfoSave)

    # 取消作业区行列信息配置
    def areaFuncInfoMatrixCan(self):
        self.leftClick(By.XPATH, BP.areaFunctionInfoCancel)
        sleep(1)

    # 修改功能区
    def editAreaFunc(self):
        self.jumpToLastPage()
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionEdit)

    # 删除功能区
    def deleteAreaFunc(self):
        self.jumpToLastPage()
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFunctionDelete)

    # 确认删除
    def deleteAreaFuncConfirm(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFuncDelConfirm)

    # 取消删除
    def deleteAreaFuncCancel(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areaFuncDelCancel)

    # 跳到尾页
    def jumpToLastPage(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.areFunctionLastPage)
