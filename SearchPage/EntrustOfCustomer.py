import time
from selenium.webdriver.common.by import By
from Base.BasePage import BasePage
import Base.PositionElement   as  BP
import os
from pywinauto.keyboard import send_keys
import random

class EntrustOfCustomer(BasePage):

    # 进入货物委托
    def entry_entrust(self):
        self.leftClick(By.XPATH, BP.entrustManagePath)  # 点击委托信息管理
        time.sleep(1)
        self.leftClick(By.XPATH, BP.entrustInfoPath)  # 点击委托信息

    # 新增委托信息按钮
    def Add_info(self):
        entrust = self.getElement(By.XPATH, BP.addEntrustButton)
        return entrust

    # 点击新增委托信息按钮
    def Add_info_click(self):
        self.leftClick(By.XPATH, BP.addEntrustButton)

    # 点击修改按钮（审核不通过-修改）
    def change_info(self):
        self.leftClick(By.XPATH, BP.Change_INFO)

    # 点击提交按钮（审核不通过-修改-提交）
    def Refer_INFO(self):
        self.leftClick(By.XPATH, BP.Refer_info)

    # 点击查看详情按钮（货主）
    def Check_detail_info(self):
        self.leftClick(By.XPATH, BP.Check_detail)

    # 点击查看详情按钮（管理）
    def EntrustDetail(self):
        self.leftClick(By.XPATH, BP.optEntrustDetails)

    #点击作废
    def BlankOut(self):
        self.leftClick(By.XPATH, BP.blankout)


    # 基本信息
    def BasicInfo(self):
        fp = self.getElement(By.XPATH, BP.BasicInfoPath)
        return fp

    # 商品信息
    def GOODInfo(self):
        pf = self.getElement(By.XPATH, BP.GoodInfoPath)
        return pf

    # 基本信息
    def Basic_info(self):
        entrustText = self.getElement(By.XPATH, BP.entrustBasicInfoPath)
        return entrustText

    # 商品信息
    def Goods_info(self):
        goodText = self.getElement(By.XPATH, BP.goodsInfoPath)
        return goodText

    # 大包装件数
    def BigPack(self):
        self.sendText(1, By.XPATH, BP.bigPackPath)

    # 包装种类选择
    def AddpackType(self):
        self.leftClick(By.XPATH, BP.packTypePath)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.packTypeDownPath)

    # 发货公司
    def ShipperCompany(self):
        self.leftClick(By.XPATH, BP.shipperCompanyNamePath)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.shipperCompanyNameDownPath)

    # 收货公司
    def consigneeCompany(self):
        self.leftClick(By.XPATH, BP.consigneeCompanyNamePath)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.consigneeCompanyNameDownPath)

    # 输入合同号
    def Contract_number(self):
        self.sendText("202100234", By.XPATH, BP.contractNoPath)

    # 选择线路
    def Line_choose(self):
        self.leftClick(By.XPATH, BP.lineNamePath)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.lineNameDownPath)

    # 选择成交方式
    def ClinchType(self):
        self.leftClick(By.XPATH, BP.clinchTypePath)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.clinchTypeDownPath)

    # 输入贸易方式
    def TradeType(self):
        self.sendText("一般贸易", By.XPATH, BP.tradeTypePath)

    # 输入币制
    def Curren(self):
        self.leftClick(By.XPATH, BP.currency)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.currencyDown)

    # 输入运费
    def Freight(self):
        self.sendText("4000", By.XPATH, BP.freightPath)

    # 输入保费
    def Premium(self):
        self.sendText("6000", By.XPATH, BP.premiumPath)

    # 输入发票号
    def InvoiceNo(self):
        self.sendText("00000001", By.XPATH, BP.invoiceNoPath)

    # 输入贸易国
    def TradeCountry(self):
        self.sendText("中国", By.XPATH, BP.tradeCountryPath)

    # 输入目的国
    def DestinationCountry(self):
        self.sendText("英国", By.XPATH, BP.destinationCountryPath)

    # 输入客户编码
    def Clientcode (self):
        self.sendText("KHBM20220234", By.XPATH, BP.clientcode)

     # 输入出境关别
    def Exitclearance(self):
        self.leftClick(By.XPATH, BP.exitclearance)
        time.sleep(1)
        self.leftClick(By.XPATH, BP.exitclearanceDownPath)


    # 备注
    def Remark(self):
        self.sendText("重量一致", By.XPATH, BP.remarkPath)

    # 第一行商品信息
    # 商品信息
    def GoodsInfo(self):
        self.leftClick(By.XPATH, BP.goodsInfoPath)

    # 输入HS编码
    def Hscode(self):
        self.sendText("5462168657", By.XPATH, BP.hsNoPath)

    # 输入货物中文名称
    def GoodsName(self):
        self.sendText("苹果", By.XPATH, BP.goodsNamePath)

    # 输入英文品名
    def EnglishName(self):
        self.sendText("apple", By.XPATH, BP.englishNamePath)

    # 输入单位
    def UnitP(self):
        self.sendText("个", By.XPATH, BP.unitPath)

    # 输入净重
    def Suttle(self):
        self.sendText("300", By.XPATH, BP.suttlePath)

    # 输入毛重（必填项）
    def MustPiecesWeight(self):
        self.sendText("500", By.XPATH, BP.mustpiecesWeightPath)

    # 输入金额（必填项）
    def MustsumPieces(self):
        self.sendText("1000", By.XPATH, BP.mustsumPieces)

    # 输入毛重(全部)
    def PiecesWeight(self):
        self.sendText("500", By.XPATH, BP.piecesWeightPath)

    # 输入单价
    def UnitPrice(self):
        self.sendText("10", By.XPATH, BP.unitPricePath)

    # 输入数量
    def PiecesNumber(self):
        self.sendText("1000", By.XPATH, BP.piecesNumberPath)

    # 输入件数
    def Uumber(self):
        self.sendText("50", By.XPATH, BP.numberPath)

    # 点击境内货源地(必填项)
    def MustCityName(self):
        time.sleep(1)
        self.leftClick(By.XPATH, BP.mustcityNamePath)  # 点击境内货源地
        time.sleep(1)
        self.leftClick(By.XPATH, BP.mustcityNameDownProPath)  # 点击境内货源地下拉列表省
        time.sleep(1)
        self.leftClick(By.XPATH, BP.mustcityNameDownCityPath)  # 点击境内货源地下拉列表市

    # 点击境内货源地（全部）
    def CityName(self):
        time.sleep(1)
        self.leftClick(By.XPATH, BP.cityNamePath)  # 点击境内货源地
        time.sleep(1)
        self.leftClick(By.XPATH, BP.cityNameDownProPath)  # 点击境内货源地下拉列表省
        time.sleep(1)
        self.leftClick(By.XPATH, BP.cityNameDownCityPath)  # 点击境内货源地下拉列表市

    # 输入申报要素
    def DeclareElements(self):
        self.sendText("4|0|2层|不带元器件|KINSUS牌|T7P52-048", By.XPATH, BP.declareElementsPath)

    # 输入唛头
    def Mark(self):
        self.sendText("Q-SEAN-SG", By.XPATH, BP.markPath)

    # 输入体积
    def Volume(self):
        self.sendText("2", By.XPATH, BP.volumePath)

    # 点击显示合计金额
    def Dianji(self):
        self.leftClick(By.XPATH, BP.piecesWeightPath)  # 点击毛重
        self.leftClick(By.XPATH, BP.unitPricePath)  # 点击单价
        self.leftClick(By.XPATH, BP.piecesNumberPath)  # 点击数量

    # 点击提交
    def SaveEntrust(self):
        self.leftClick(By.XPATH, BP.saveEntrustPath)

    # 第二行商品信息
    # 点击添加
    def AddGoods(self):
        self.leftClick(By.XPATH, BP.addGoodsPath)

    # 输入HS编码
    def HsNo_Path(self):
        self.sendText("3245632456", By.XPATH, BP.hsNo_Path)

    # 输入货物中文名称
    def Goods_NamePath(self):
        self.sendText("葡萄", By.XPATH, BP.goods_NamePath)

    # 输入英文品名
    def English_NamePath(self):
        self.sendText("grape", By.XPATH, BP.english_NamePath)

    # 输入单位
    def Unit_Path(self):
        self.sendText("个", By.XPATH, BP.unit_Path)

    # 输入净重
    def Suttle_Path(self):
        self.sendText("300", By.XPATH, BP.suttle_Path)

    # 输入毛重
    def Pieces_WeightPath(self):
        self.sendText("500", By.XPATH, BP.pieces_WeightPath)

    # 输入单价
    def Unit_PricePath(self):
        self.sendText("10", By.XPATH, BP.unit_PricePath)

    # 输入数量
    def Pieces_NumberPath(self):
        self.sendText("1000", By.XPATH, BP.pieces_NumberPath)

    # 输入件数
    def Number_Path(self):
        self.sendText("50", By.XPATH, BP.number_Path)

    # 点击境内货源地
    def City_NamePath(self):
        self.leftClick(By.XPATH, BP.city_NamePath)  # 点击境内货源地
        time.sleep(1)
        self.leftClick(By.XPATH, BP.cityName_DownProPath)  # 点击境内货源地下拉列表省
        time.sleep(1)
        self.leftClick(By.XPATH, BP.cityName_DownCityPath)  # 点击境内货源地下拉列表市

    # 输入申报要素
    def Declare_ElementsPath(self):
        self.sendText("4|0|2层|不带元器件|KINSUS牌|T7P52-048", By.XPATH, BP.declare_ElementsPath)

    # 输入唛头
    def Mark_Path(self):
        self.sendText("Q-SEAN-SG", By.XPATH, BP.mark_Path)

    # 输入体积
    def Volume_Path(self):
        self.sendText("20", By.XPATH, BP.volume_Path)

    # 点击显示合计金额
    def Dianji_h(self):
        self.leftClick(By.XPATH, BP.unit_Price)  # 点击毛重
        self.leftClick(By.XPATH, BP.pieces_Number)  # 点击单价
        self.leftClick(By.XPATH, BP.saveEntrustPath)  # 点击数量

    # 删除商品
    def DeleteGoods(self):
        self.leftClick(By.XPATH, BP.deleteGoodsPath)

    # 获取被理货货物的入仓编号
    def getWNo(self):
        result = self.getElement(By.XPATH, BP.customerWNo)
        text = ''.join(result.text).split('：')[1]
        return text

    # 获取货主/博正登录账户
    def getUserOnLoad(self):
        try:
            result = self.getElement(By.XPATH, BP.customerLogOutEnter)
            text = ''.join(result.text)
            return text
        except:
            result = self.getElement(By.XPATH, BP.operationLogOutEnter)
            text = ''.join(result.text)
            return text


    # 点击查询
    def MustFind_hz(self):
        time.sleep(1)
        self.leftClick(By.XPATH, BP.mustFind_hz)

    # 点击货物状态
    def Goods_stu(self):
        time.sleep(1)
        self.leftClick(By.XPATH, BP.optEntrust_GoodsTypeSearch)

    # 货物状态-审核通过
    def optEntrust_Pass(self):
        self.leftClick(By.XPATH, BP.optEntrust_ExaminePass)

    # 点击入库单导出
    def Warehousing_entry_derive(self):
        time.sleep(1)
        self.leftClick(By.XPATH, BP.Warehousing_entry)
        time.sleep(4)
        self.renameFile((self.getWNo() + '入库单.docx'), (self.getWNo() + '入库单' + '-' + self.getUserOnLoad() + '-' + self.timeStrftime() + '.docx'))
        time.sleep(1)

    # 新增基本信息(所有基本信息)
    def Base_info(self):
        self.Add_info_click()  # 点击新增委托信息
        time.sleep(1)
        self.BigPack()  # 输入大包装件数
        time.sleep(1)
        self.AddpackType()  # 点击包装种类
        self.ShipperCompany()  # 选择发货公司
        time.sleep(1)
        self.consigneeCompany()  # 选择收货公司
        time.sleep(1)
        self.Contract_number()  # 输入合同号
        self.Line_choose()  # 选择路线
        time.sleep(1)
        self.ClinchType()  # 选择成交方式
        time.sleep(1)
        self.TradeType()  # 输入贸易方式
        self.Curren()  # 选择币制
        time.sleep(1)
        self.Freight()  # 输入运费
        self.Premium()  # 输入保费
        self.InvoiceNo()  # 输入发票号
        self.TradeCountry()  # 输入贸易国
        self.DestinationCountry()  # 输入目的国
        self.Clientcode()          #输入客户编码
        self.Exitclearance()       #输入出境关别
        self.Remark()  # 输入备注

    # 新增第一行商品信息(必填项)
    def Mustfirst_goodf_info(self):
        self.GoodsInfo()  # 点击商品信息
        self.Hscode()  # 输入HS编码
        self.GoodsName()  # 输入货物中文名称
        self.MustPiecesWeight()  # 输入毛重
        self.MustsumPieces()  # 输入金额
        self.MustCityName()  # 点击境内货源地下拉列表市

    # 新增第一行商品信息(所有商品信息)
    def first_goodf_info(self):
        self.GoodsInfo()  # 点击商品信息
        self.Hscode()  # 输入HS编码
        self.GoodsName()  # 输入货物中文名称
        self.MustPiecesWeight()  # 输入毛重
        self.MustsumPieces()  # 输入金额
        self.MustCityName()  # 点击境内货源地下拉列表市
        self.EnglishName()  # 输入英文品名
        self.UnitP()  # 输入单位
        self.Suttle()  # 输入净重
        self.UnitPrice()  # 输入单价
        self.PiecesNumber()  # 输入数量
        self.Uumber()  # 输入件数
        self.DeclareElements()  # 输入申报要素
        self.Mark()  # 输入唛头
        self.Volume()  # 输入体积


    # 审核不通过（管理）
    # 业务委托
    def Business_Delegate(self):
        time.sleep(5)
        self.leftClick(By.XPATH, BP.optEntrustMan)


    # 货物状态待审核(管理)
    def Goods_wait_audit(self):
        self.leftClick(By.XPATH, BP.optEntrustGoodsToBeReviewed)

    # 导出货物清单
    def GoodsListButton(self):
        self.leftClick(By.XPATH, BP.optEntrustGoodsListButton)

    # 查询
    def Find_gl(self):
        time.sleep(1)
        self.leftClick(By.XPATH, BP.optEntrustSearchButton)

    # 二次查询
    def MustFind_gl(self):
        time.sleep(1)
        self.leftClick(By.XPATH, BP.mustFind_gl)


    # 审核
    def Audit_button(self):
        self.leftClick(By.XPATH, BP.optEntrustExamine)

    # 基本信息
    def EntrustBasicInfo(self):
        jiben = self.getElement(By.XPATH, BP.optEntrustBasicInfo)
        return jiben

    # 商品信息
    def EntrustGoodsInfo(self):
        shangpin = self.getElement(By.XPATH, BP.optEntrustGoodsInfo)
        return shangpin

    # 审核信息
    def EntrustExamineInfo(self):
        shenhe = self.getElement(By.XPATH, BP.optEntrustExamineInfo)
        return shenhe

    # 附件信息
    def EntrustEnclosure(self):
        fujian = self.getElement(By.XPATH, BP.optEntrustEnclosure)
        return fujian

    # 选择“否”
    def No_button(self):
        self.leftClick(By.XPATH, BP.optEntrustExamineFail)

    # 输入审核不通过原因
    def FailReason(self):
        self.sendText("货物信息不完整", By.XPATH, BP.optEntrustExamineFailReason)

    # 选择“是”
    def Yes_button(self):
        self.leftClick(By.XPATH, BP.optEntrustExaminePass)

    # 点击发车时间
    def Timetable(self):
        self.leftClick(By.XPATH, BP.optEntrustDepartureTimeBut)

    # 选择时间
    def Last_time(self):
        self.leftClick(By.XPATH, BP.optEntrustDepartureTime)

    # 班次号
    def Train_shift(self):
        self.sendText("G345", By.XPATH, BP.optEntrustShiftNumber)

    # 提交
    def Submit(self):
        self.leftClick(By.XPATH, BP.optEntrustSubmit)

    #审核通过的二次确认
    def MustSubmit(self):
        self.leftClick(By.XPATH, BP.mustSubmit)

    # 删除审核不通过的货物(货主)
    # 选择审核不通过
    def Auditing_fail(self):
        self.leftClick(By.XPATH, BP.optEntrust_ExamineFail)

    # 点击查询
    def Find_hz(self):
        self.leftClick(By.XPATH, BP.optEntrust_SearchButton)

    #点击报关资料
    def CustomsDeclarationInformation(self):
        self.leftClick(By.XPATH, BP.customsdeclarationinformation)

    #添加合同附件
    def AppendicesContract(self):
        ele = self.driver.find_element_by_xpath(
            "//div[@class='btn btn-confirm']/../../div[1]/div/div[2]/div/button")  # 点击加号
        ele.click()
        time.sleep(2)
        # send_keys(r"%s%s.jpg" % ('%s\File\ImportFile\\' % sys.path[0], random.randint(1, 16)))
        send_keys(r"%sFile\ImportFile\%s.jpg" % ((os.path.abspath(os.getcwd()) + os.path.sep), random.randint(1, 16)))
        send_keys("{VK_RETURN}")

    # 添加其他附件
    def OtherAccessories(self):
        ele = self.driver.find_element_by_xpath(
            "//div[@class='btn btn-confirm']/../../div[2]/div[1]/div/button")  # 点击加号
        ele.click()
        time.sleep(2)
        # send_keys(r"%s%s.jpg" % ('%s\File\ImportFile\\' % sys.path[0], random.randint(1, 16)))
        send_keys(r"%sFile\ImportFile\%s.jpg" % ((os.path.abspath(os.getcwd()) + os.path.sep), random.randint(1, 16)))
        send_keys("{VK_RETURN}")

    # 添加其他附件
    def TiJiao(self):
        self.leftClick(By.XPATH, BP.tijiao)




    # 点击删除
    def Delete_Goods(self):
        self.leftClick(By.XPATH, BP.del_button)

    # 点击确定
    def Delete_Sure(self):
        self.leftClick(By.XPATH, BP.sur_button)

    # 确认理货正常（货主）
    # 点击理货状态
    def Freight_forward_Stu(self):
        self.leftClick(By.XPATH, BP.Tally_stu)

    # 选择理货异常
    def Tally_abnorma_path(self):
        self.leftClick(By.XPATH, BP.Tally_abnormal)

    # 点击查询
    def tally_query(self):
        self.leftClick(By.XPATH, BP.Tally_query)

    # 点击理货信息
    def tally_info(self):
        self.leftClick(By.XPATH, BP.Tally_info)

    # 点击理货确认
    def tally_sure(self):
        self.leftClick(By.XPATH, BP.Tally_sure)



