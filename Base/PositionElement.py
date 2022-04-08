# =====已确认=====
# 登录用户名
usernamePath = r'//div[@class="ivu-input-wrapper ivu-input-wrapper-default ivu-input-type-text ivu-input-group ivu-input-group-default ivu-input-group-with-prepend"]/input'
# 登录密码
passwordPath = r'//div[@class="ivu-input-wrapper ivu-input-wrapper-default ivu-input-type-password ivu-input-group ivu-input-group-default ivu-input-group-with-prepend"]/input'
# 验证码
verificationCodePath = '//div[@class="content-from-input-input ivu-input-wrapper ivu-input-wrapper-default ivu-input-type-text ivu-input-group ivu-input-group-default ivu-input-group-with-prepend"]/input'
# 登录按钮
loginButtonPath = r'//button[@class="content-from-btn ivu-btn ivu-btn-primary"]'
# 客户账户管理 '//div[@class="user"]/span'
customerLogOutEnter = '//*[@id="app"]/div[1]/header/div/div/div[2]/div[3]/span'
# 退出登录 '//div[@class="user"]/div/span'
logOutPath = '//*[@id="app"]/div[1]/header/div/div/div[2]/div[3]/div/span'
# 博正账户管理 '//div[@class="user"]/span'
operationLogOutEnter = '//*[@id="container"]/div/div/div[1]/div/div[4]/div[3]/span'
# 博正退出系统 '//div[@class="user"]/div/span'
logOutOperationPath = '//*[@id="container"]/div/div/div[1]/div/div[4]/div[3]/div/span'

# =====   =====
# 委托信息管理 '//div[contains(text(),"委托管理")]'
entrustManagePath = '//*[@id="container"]/div/div[1]/div[2]/div[1]/div[1]'
# 货物委托
entrustInfoPath = '//div[contains(text(),"委托信息查询")]'
# 新增委托按钮
addEntrustButton = '//div[contains(text(),"新增委托信息 ")]'
# 查看详情按钮
Check_detail = '//ul[@class="card-lists"]/li[1]/div/div[2]/div[2]/span'

# =====   =====
# 基本信息
entrustBasicInfoPath = '//div[@class="container"]/div[2]/div/div/div/div/div/div/div/div[2]'
# 待审核-查看详情的基本信息和商品信息
BasicInfoPath = '//div[@class="container"]/div/div[3]/div/div/div/div/div/div/div[2]'
GoodInfoPath = '//div[@class="container"]/div/div[3]/div/div/div/div/div/div/div[3]'
# 基本信息 —— 大包装件数
bigPackPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[2]/div/div/div/div[2]/input'
# 基本信息 —— 包装种类
packTypePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[4]/div/div/div/div/div/input'
# 基本信息 —— 包装种类下拉列表
packTypeDownPath = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"]/ul[2]/li[1]'
# 基本信息 —— 总重量
totalWetPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div/div/input'
# 基本信息 —— 总金额
total_amountPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[8]/div/div/div/input'
# 基本信息 —— 总件数
totalNumberPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[10]/div/div/div/input'
# 基本信息 —— 发货公司
shipperCompanyNamePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[2]'
# 基本信息 —— 发货公司下拉列表
shipperCompanyNameDownPath = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][2]/ul[2]/li[1]'
# 基本信息 —— 发货地址
shipperAddressPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[4]'
# 基本信息 —— 发货人姓名
shipperNamePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[6]'
# 基本信息 —— 发货人联系电话
shipperPhonePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[8]'
# 基本信息 —— 发货人邮箱
shipperEmailPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[10]'
# 基本信息 —— 收货公司
consigneeCompanyNamePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td[2]'
# 基本信息 —— 收货公司下拉列表
consigneeCompanyNameDownPath = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][3]/ul[2]/li[1]'
# 基本信息 —— 收货地址
consigneeAddressPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td[4]'
# 基本信息 —— 收货人姓名
consigneeNamePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td[6]'
# 基本信息 —— 收货人联系电话
consigneePhonePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td[8]'
# 基本信息 —— 收货人邮箱
consigneeEmailPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td[10]'
# 基本信息 —— 合同号
contractNoPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td[2]/div/div/div/input'
# 基本信息 —— 线路
lineNamePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td[4]/div/div/div'
# 基本信息 —— 线路下拉列表
lineNameDownPath = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][4]/ul[2]/li[1]'
# 基本信息 —— 成交方式
clinchTypePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td[6]/div/div/div'
# 基本信息 —— 成交方式下拉列表
clinchTypeDownPath = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][5]/ul[2]/li[1]'
# 基本信息 —— 贸易方式
tradeTypePath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td[8]/div/div/div/input'
# 基本信息 —— 币制
currency = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td[10]/div/div/div'
# 基本信息 —— 币制下拉列表
currencyDown = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][6]/ul[2]/li[1]'
# 基本信息 —— 运费
freightPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td[2]/div/div/div/div[2]/input'
# 基本信息 —— 保费
premiumPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td[4]/div/div/div/div[2]/input'
# 基本信息 —— 发票号
invoiceNoPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td[6]/div/div/div/input'
# 基本信息 —— 贸易国
tradeCountryPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td[8]/div/div/div/input'
# 基本信息 —— 目的国
destinationCountryPath = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td[10]/div/div/div/input'
# 基本信息--客户编码
clientcode = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td[2]/div/div/div/input'
# 基本信息--出境关别
exitclearance = '//div[@class="container"]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td[4]/div/div/div/div/div/span'
# 基本信息--出境关别--下拉列表
exitclearanceDownPath = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][last()]/ul[2]/li[1]'
# 基本信息 —— 备注
remarkPath = '//div[@class="table-row-warp"]/div[2]/div/div/table/tbody/tr/td[2]/div/div/textarea'
# 商品信息
goodsInfoPath = '//div[@class="container"]/div[2]/div/div/div/div/div/div/div/div[3]'
# 商品信息 —— hs编码
hsNoPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[2]/div/div/div/input'
# 商品信息 —— 货物中文名称
goodsNamePath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[3]/div/div/div/input'
# 商品信息 —— 英文品名
englishNamePath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[7]/div/div/div/input'
# 商品信息 —— 单位
unitPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[8]/div/div/div/input'
# 商品信息 —— 净重kg
suttlePath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[9]/div/div/div/div[2]/input'
# 商品信息 —— 毛重kg（必填项）
mustpiecesWeightPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[4]/div/div/div/div[2]/input'
#  #商品信息 —— 毛重kg
# piecesWeightPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[7]/div/div/div/div[2]/input'
# 商品信息 —— 金额（必填项）
mustsumPieces = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[5]/div/div/div/div[2]/input'
# 商品信息 —— 单价
unitPricePath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[10]/div/div/div/div[2]/input'
# 商品信息 —— 数量
piecesNumberPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[11]/div/div/div/div[2]/input'
# 商品信息 —— 金额
amountPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[10]/div/div/div/div[2]/input'
# 商品信息 —— 件数
numberPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[12]/div/div/div/div[2]/input'
# 商品信息 —— 境内货源地（必填项）
mustcityNamePath = "//div[@class='ivu-tabs ivu-tabs-card ivu-tabs-no-animation']/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[6]/div/div/div/div/div[2]"
# 商品信息 —— 境内货源地下拉列表省（必填项）
mustcityNameDownProPath = '//div[@class="ivu-select-dropdown ivu-cascader-transfer"][last()]/div/span/ul/li[1]'
# 商品信息 —— 境内货源地下拉列表市（必填项）
mustcityNameDownCityPath = '//div[@class="ivu-select-dropdown ivu-cascader-transfer"][last()]/div/span/span/ul/li[1]'
# 商品信息 —— 境内货源地
cityNamePath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[12]/div/div/div/div'
# 商品信息 —— 境内货源地下拉列表省
cityNameDownProPath = '//div[@class="ivu-select-dropdown ivu-cascader-transfer"][last()]/div/span/ul/li[1]'
# 商品信息 —— 境内货源地下拉列表市
cityNameDownCityPath = '//div[@class="ivu-select-dropdown ivu-cascader-transfer"][last()]/div/span/span/ul/li[1]'
# 商品信息 —— 申报要素
declareElementsPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[13]/div/div/div/input'
# 商品信息 —— 唛头
markPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[14]/div/div/div/input'
# 商品信息 —— 体积(cbm)
volumePath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[15]/div/div/div/div[2]/input'
# 添加
addGoodsPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[1]/div'
# 删除
deleteGoodsPath = '//div[@class="ivu-tabs ivu-tabs-card ivu-tabs-no-animation"]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[last()]/td[16]/div/div/div/span'
# 提交
saveEntrustPath = '//button[@class="btn blue cvu-button cvu-button-default is-round"]/span'
# 提交（审核不通过修改货物的提交）
Refer_info = '//button[@class="btn blue cvu-button cvu-button-default is-round"]/span'
# 二次确认——确认
twoStepVerifyConfirm = '//div[@class="cvu-modal-btn"][1]'
# 二次确认——取消
twoStepVerifyCancel = '//div[@class="cvu-modal-btn"][2]'
# 取消
cancelEntrustPath = '//button[@class="btn blue cvu-button cvu-button-default is-round"]/../button[2]/span'
# 操作成功
operationSuccess = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 入库单导出
Warehousing_entry = '//*[@id="container"]/div/div[1]/div[3]/ul/li[1]/div[1]/div[2]/div[1]/button[2]/span'
# 报关资料上传
declareFile = '//ul[@class="card-lists"]/li[1]/div/div[2]/div/button[1]/span'
# 货主导出入库单入仓编号
customerWNo = '//ul[@class="card-lists"]/li[1]/div[3]/div[1]/span'

# =====   =====
# 第二行商品信息
# 输入HS编码
hsNo_Path = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div/div/input'
# 货物中文名称
goods_NamePath = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/input'
#  英文品名
english_NamePath = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[4]/div/div/div/input'
#  单位
unit_Path = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[5]/div/div/div/input'
#  净重kg
suttle_Path = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[6]/div/div/div/div[2]/input'
#  毛重kg
pieces_WeightPath = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[7]/div/div/div/div[2]/input'
#  单价
unit_PricePath = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[8]/div/div/div/div[2]/input'
#  数量
pieces_NumberPath = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[9]/div/div/div/div[2]/input'
#  件数
number_Path = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[11]/div/div/div/div[2]/input'
#  境内货源地
city_NamePath = "/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[12]/div/div/div/div/div[2]"
# 境内货源地天津
cityName_DownProPath = "/html/body/div[25]/div/span/ul/li[2]"
cityName_DownCityPath = "/html/body/div[25]/div/span/span/ul/li"
#  申报要素
declare_ElementsPath = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[13]/div/div/div/input'
#  唛头
mark_Path = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[14]/div/div/div/input'
#  体积(CBM)
volume_Path = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[15]/div/div/div/div[2]/input'
#  毛重kg
pieces_Weight = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[7]/div/div/div/div[2]/input'
#  单价
unit_Price = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[8]/div/div/div/div[2]/input'
#  数量
pieces_Number = '//*[@id="container"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[9]/div/div/div/div[2]/input'

# =====   =====
# 货主删除委托
# 点击查询
mustFind_hz = '//div[@class="container scrollPanel"]/div[2]/div[1]/div[2]'
# 点击货物状态
optEntrust_GoodsTypeSearch = '//span[contains(text(),"货物状态")]'
# 选择审核不通过的货物
optEntrust_ExamineFail = '//li[contains(text(),"审核不通过")]'
# 选择审核通过的货物
optEntrust_ExaminePass = '//li[contains(text(),"审核通过")]'
# 点击二次查询
optEntrust_SearchButton = '//span[contains(text(),"查询")]'
# 点击报关资料
customsdeclarationinformation = '//*[@id="container"]/div/div[1]/div[3]/ul/li[1]/div[1]/div[2]/div[1]/button[1]/span'
# 添加合同附件
appendicescontract = "//div[@class='btn btn-confirm']/../../div[1]/div/div[2]/div/button"
# 添加其他附件
otheraccessories = "//div[@class='btn btn-confirm']/../../div[2]/div[1]/div/button"
# 点击提交
tijiao = "//div[@class='btn btn-confirm']"
# 点击修改按钮
Change_INFO = '//ul[@class="card-lists"]/li/div[1]/div[2]/div[1]/button[1]/span'
# 点击删除按钮
del_button = '//*[@id="container"]/div/div[1]/div[3]/ul/li[1]/div[1]/div[2]/div[1]/button[2]/span'
# 点击确定按钮
sur_button = '//div[@class="cvu-modal cvu-modal-show"]/div[2]/div[3]/div[1]'


# =====   =====
# 运营公司审核委托
# 业务委托
optEntrustMan = '//ul[@class="menu-items"]/div[2]/div/div'
# 入仓编号查询条件
optEntrustCodeSearch = '//div[@class="cvu-search-card-main"]/span/div/input'
# 申请单位查询条件
optEntrustCompanySearch = '//div[@class="cvu-search-card-main"]/span[2]/div/input'
# 货物状态查询条件
optEntrustGoodsTypeSearch = '//div[@class="cvu-search-card-main"]/span[3]/div/div'
# 待审核
optEntrustGoodsToBeReviewed = '//ul[@class="ivu-select-dropdown-list"]/li[1]'
# 申请时间查询条件
optEntrustApplyTimeSearch = '//div[@class="cvu-search-card-main"]/span[4]/div/div'
# 查询按钮
optEntrustSearchButton = '//div[@class="pages-component"]/div[1]/div[4]'
# 二次查询按钮
mustFind_gl = '//div[@class="cvu-search-card-footer"]/button[1]/span'
# 重置按钮
optEntrustResetButton = '//div[@class="cvu-search-card-footer"]/button[2]/span'
# 导出货物清单按钮
optEntrustGoodsListButton = '//div[@class="pages-component"]/div/div[3]'
# 审核按钮
optEntrustExamine = '//div[@class="content scrollBar"]/div/label[1]/div[1]/div[2]/div[1]/button/span'
# 查看详情
optEntrustDetails = "//div[@class='content scrollBar']/div/label[1]/div[1]/div[2]/div[2]/span"
# 点击作废
blankout = '//span[contains(text(),"作废")]'
# 首页
optEntrustHomePage = '//div[@class="cvu-paginator-warp"]/span'
# 审核通过
optEntrustExaminePass = '//div[@class="ivu-radio-group ivu-radio-group-default ivu-radio-default"]/label/span/span'
# 审核不通过
optEntrustExamineFail = '//div[@class="ivu-radio-group ivu-radio-group-default ivu-radio-default"]/label[2]/span/span'
# 审核不通过原因
optEntrustExamineFailReason = '//div[@class="item"]/div/div/textarea'
# 发车时间
optEntrustDepartureTimeBut = '//*[@id="pageDetail"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/input'
# 选择时间
optEntrustDepartureTime = '//div[@class="ivu-picker-panel-body"]/div[2]/div/span[last()]'
# 班次号
optEntrustShiftNumber = '//div[@class="ivu-tabs-content"]/div[3]/div/div/div[2]/div[2]/div/div/input'
# 提交
optEntrustSubmit = '//div[@class="footer"]/div/button[1]/span'
# 审核通过二次确认
mustSubmit = "//div[@class='cvu-modal cvu-modal-bigscreen cvu-modal-show']/div[2]/div[3]/div[1]"
# 取消
optEntrustCancel = '//div[@class="footer"]/div/button[2]/span'
# 基本信息
optEntrustBasicInfo = '//div[@class="ivu-tabs-nav"]/div[2]'
# 商品信息
optEntrustGoodsInfo = '//div[@class="ivu-tabs-nav"]/div[3]'
# 审核信息
optEntrustExamineInfo = '//div[@class="ivu-tabs-nav"]/div[4]'
# 附件信息
optEntrustEnclosure = '//div[@class="ivu-tabs-nav"]/div[5]'
# 提交成功
optEntrustExamineSuccessDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'


# =====   =====
# 进出场预约
# 进出场预约入口
customerEntryExitRes = '//div[contains(text(),"委托进场预约")]'
# 货物预约
customerEEEREntry = '//div[contains(text(),"货物预约进场")]'
# 查看详情
Examine_particulars = '//*[@id="container"]/div/div[1]/div[3]/ul/li[1]/div[1]/div[2]/div/span'
# 货物进场预约详情
Approach_order_detail = '//*[@id="container"]/div/div[2]/div[1]/div[1]'
# 预约进场
customerEEERIn = '//div[@id="app"]/div[2]/div/div/div[2]/div/div'
# 预约进场——车牌号输入
customerEEERInNum = '//div[@class="page"]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/span/div/input'
# 预约进场——进场日期
customerEEERInDay = '//div[@class="page"]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/span[2]/span/div/div/div/input'
# 预约进场——进场日期——选择最后一个时间
customerEEERInDaySel = '//div[@class="ivu-picker-panel-body-wrapper"]/div/div[2]/div/span[last()]'
# 预约进场——进场时间
customerEEERInTime = '//div[@class="ivu-select ivu-select-single ivu-select-default"]/div/div/span'
# 预约进场_进场时间——选择第一个时间
customerEEERInTimeSel = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"]/ul[2]/li[1]'
# 预约进场——提交
customerEEERInSubmit = '//div[@class="page"]/div[2]/div[2]/div[2]/div/button[1]'
# 预约进场——取消
customerEEERInCancel = '//div[@class="page"]/div[2]/div[2]/div[2]/div/button[2]'
# 待选货物位置
customerEntrustPositionNotSelected = '//div[@id="container"]/div/div[2]/div[2]/div/div/ul/li/div[3]/div/span'
# 已选货物位置
customerEntrustPositionSelected = '//*[@id="container"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul'
# 查看详情
customerEEERInSeeDetail = '//div[@class="page"]/div/div[3]/ul/li/div/div[2]/div/span'
# 查看详情返回
customerEEERInSeeDetailBack = '//div[@class="page"]/div[2]/div/div[4]/div/button/span'
# 操作成功回执
customerEEERSuccessDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'


# =====   =====
# 运营公司货物进场预约
# 货物进场预约入口
optEntryExitResEntry = '//div[@class="draw-box bigscreen v-transfer-dom"]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]'
# 修改
optEntryExitResEdit = '//div[@class="page"]/div/div[2]/div/div/div/div[3]/ul/li/div/div[2]/div/button/span'
# 修改——车牌号
optEEREditNum = '//div[@class="operation-body bigscreen"]/div/ul/li/div/div/input'
# 修改——预约日期
optEEREditDay = '//div[@class="operation-body bigscreen"]/div/ul/li[2]/div/div/div/div/div/input'
# 修改——预约日期——选择一个
optEEREditDaySec = '//div[@class="ivu-picker-panel-body-wrapper"]/div/div[2]/div/span[33]/em'
# 修改——预约时间
optEEREditTime = '//div[@class="operation-body bigscreen"]/div/ul/li[2]/div/div/div[2]/div/div/i'
# 修改——预约时间选择第一个
optEEREditTimeSec = '//ul[@class="ivu-select-dropdown-list"]/li[2]'
# 修改——修改申请人
optEEREditApply = '//div[@class="operation-body bigscreen"]/div/ul/li[3]/div/div/input'
# 修改——备注
optEEREditRemark = '//div[@class="operation-body bigscreen"]/div/ul/li[4]/div/textarea'
# 修改——提交
optEEREditSubmit = '//div[@class="operation-body bigscreen"]/div[2]/div/button/span'
# 修改——取消
optEEREditCancel = '/html/body/div[7]/div[2]/div/div/a/i'
# 删除
optEntryExitResDelete = '//div[@class="page"]/div/div[2]/div/div/div/div[3]/ul/li/div/div[2]/div/button[2]/span'
# 确认删除
optEERDeleteSubmit = '//div[@class="cvu-modal cvu-modal-bigscreen cvu-modal-show"]/div[2]/div[3]/div'
# 取消删除
optEERDeleteCancel = '//div[@class="cvu-modal cvu-modal-bigscreen cvu-modal-show"]/div[2]/div[3]/div[2]'
# 查看详情
optEERSeeDetail = '//div[@class="content"]/ul/li/div/div[2]/div[2]/span'
# 操作成功回执
optEEROptSubDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'


# =====   =====
# 待卸货理货
# 点击卸货理货管理
Unloading_tally_management = '//p[contains(text(),"卸货理货管理")]'
# 点击待卸货理货卡片
Tally_tobe_unloaded = "//ul[@class='card-lists']/li/div[1]"
# 输入体积
Volume = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[1]/div/div/div/div[2]/input'
# 输入总重量
Total_weight = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[2]/div/div/div/div[2]/input'
# 输入总件数
Total_package = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[3]/div/div/div/div[2]/input'
# 选择包装种类
Packages = "//input[@placeholder='请选择']"
# 加大保护编制坛
Protect = '//li[contains(text(),"加保护编织坛")]'
# 输入长
Len = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/table/tbody/tr/td[2]/div/div/div/div[2]/input'
# 输入宽
Wid = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/table/tbody/tr/td[3]/div/div/div/div[2]/input'
# 输入高
High = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/table/tbody/tr/td[4]/div/div/div/div[2]/input'
# 输入重量
Weig = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/table/tbody/tr/td[5]/div/div/div/div[2]/input'
# 输入件数
Piece = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/table/tbody/tr/td[6]/div/div/div/div[2]/input'
# 输入有无损坏及异常
Damage_unusual = '//div[@class="detail-box"]/div/textarea'
# 点击照片信息
Photograph = '//span[contains(text(),"照片信息")]'
# 点击理货确认/点击运抵申报
Cargo_arrived = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/button/span'


# =====   =====
# 已卸货理货
# 点击已卸货理货卡片
Tally_loaded = '//div[contains(text(),"已卸货理货")]'
# 选择申报运抵
Declare_stu = '//span[contains(text(),"请选择运抵申报状态")]'
# 选择未申报运抵
UnDeclare = '//li[contains(text(),"未申报运抵")]'
# 点击查询
Inquiry = '//*[@id="container"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[3]/button[1]'
# 点击入库单信息
Godownentry_info = '//span[contains(text(),"入库单信息")]'
# 点击入库单下载
Godownentry_down = '//span[contains(text(),"入库单下载")]'
# 选择理货状态
Tally_status = '//div[@class="cvu-search-card-main"]/span[4]/div/div/div/span'
# 选择理货正常
Tally_normal = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"]/ul[2]/li[1]'


# =====   =====
# 确认理货异常
# 点击理货状态
Tally_stu = "//span[contains(text(),'理货状态')]"
# 选择理货异常
Tally_abnormal = "/html/body/div[6]/ul[2]/li[2]"
# 点击查询
Tally_query = "//span[contains(text(),'查询')]"
# 点击理货信息
Tally_info = '//*[@id="container"]/div/div[1]/div[3]/ul/li[1]/div[1]/div[2]/div[1]/button[2]/span'
# 点击理货确认
Tally_sure = "//div[@class='ivu-drawer-wrap']/div/div/div[2]/div/div[3]/div"
# 被理货货物入仓编号
Tally_WNo = '//li[@class="active card-list"]/div[3]/div[2]/div/div/span'


# 首页 '//*[@id="container"]/div/div/div[3]/div/div/div/div/ul/div[1]/div/div'
homePage = '//div[@class="layout-footer"]/div/div/div/div/ul/div/div/div[1]'


# =====已确认=====
# 客户收发货公司维护
# 收发货公司维护
customerCompanyManage = '//div[contains(text(),"收发货公司维护")]'
# 收发货公司查询
customerCompany = '//*[@id="app"]/div[1]/header/div/div/div[1]/div[4]/div/div/div'
# 发货公司
shipperCompany = '//*[@id="container"]/div/div/div[1]/div[1]'
# 收货公司
consigneeCompany = '//*[@id="container"]/div/div/div[1]/div[2]'
# 客户收发货公司维护——公司名称查询条件
CompanyNameSearch = '//*[@id="container"]/div/div/div[2]/div[2]/div[1]/span[1]/div/input'
# 客户收发货公司维护——收发货人查询条件
shipperORConsigneeName = '//*[@id="container"]/div/div/div[2]/div[2]/div[1]/span[2]/div/input'
# 客户收发货公司维护——查询展开按钮
shipperORConsigneeSearch = '//*[@id="container"]/div/div/div[3]/didv/div[2]'
# 客户收发货公司维护——查询点击按钮
shipperORConsigneeSearchClick = '//*[@id="container"]/div/div/div[2]/div[2]/div[3]/button[1]/span'
# 客户收发货公司维护——重置按钮
shipperORConsigneeReset = '//*[@id="container"]/div/div/div[2]/div[2]/div[3]/button[2]/span'
# 客户收发货公司维护——新增收发货信息
addShipperORConsignee = '//*[@id="container"]/div/div/div[3]/didv/div'
# 客户收发货公司维护——新增收发货信息——公司名称
addOREditCompanyName = '/html/body/div[10]/div[2]/div/div/div[2]/div/div[1]/ul/li[1]/div/div/input'
# 客户收发货公司维护——新增收发货信息——公司地址
addOREditCompanyAddress = '/html/body/div[10]/div[2]/div/div/div[2]/div/div[1]/ul/li[2]/div/div/input'
# 客户收发货公司维护——新增收发货信息——收发货人姓名
addOREditShipperConsigneeName = '/html/body/div[10]/div[2]/div/div/div[2]/div/div[1]/ul/li[3]/div/div/input'
# 客户收发货公司维护——新增收发货信息——收发货人电话
addOREditShipperConsigneePhone = '/html/body/div[10]/div[2]/div/div/div[2]/div/div[1]/ul/li[4]/div/div/input'
# 客户收发货公司维护——新增收发货信息——收发货人邮箱
addOREditShipperConsigneeEmail = '/html/body/div[10]/div[2]/div/div/div[2]/div/div[1]/ul/li[5]/div/div/input'
# 客户收发货公司维护——新增收发货信息——提交按钮
addOREditCompanySubmit = '/html/body/div[10]/div[2]/div/div/div[2]/div/div[2]/div/button/span'
# 客户收发货公司维护——新增收发货信息——取消按钮
addOREditCompanyCancel = '/html/body/div[10]/div[2]/div/div/a/i'
# 新增收发货公司操作成功反馈
customerCompanyNameOperationSuccess = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 跳到尾页
customerCompanyLastPage = '//*[@id="container"]/div/div/div[3]/div/div/span[4]'
# 修改按钮
customerCompanyEditButton = '//*[@id="container"]/div/div/div[4]/ul/li[1]/div[1]/div[2]/div/button[1]/span'
# 删除按钮
customerCompanyDeleteButton = '//*[@id="container"]/div/div/div[4]/ul/li[1]/div[1]/div[2]/div/button[2]/span'
# 删除确定
customerCompanyDeleteSuccess = '/html/body/div[11]/div[2]/div[3]/div[1]'
# 删除取消
customerCompanyDeleteCancel = '/html/body/div[11]/div[2]/div[3]/div[2]'
# 删除成功提示
customerCompanyDeleteSuccessDetail = '/html/body/div[43]/div/div/div[1]/div/span'
# 用于重复校验(定位已存在的公司名称)
customerCompanyRepeat = '//*[@id="container"]/div/div/div[4]/ul/li[1]/div[3]/div[1]/span/div[1]/div'


# =====   =====
# 运营公司维护入口
OCMaintenanceEntry = '/html/body/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[4]/img'
# 目的站维护入口
OCDestinationMaintenanceEntry = '//div[contains(text(),"目的站维护")]'
# 目的站维护的查询条件
OCDestinationMaintenanceSearch = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/span/div/div/div/input'
# 目的站维护查询按钮
OCDestinationMaintenanceSearchButton = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/button[1]/span'
# 目的站维护重置按钮
OCDestinationMaintenanceResetButton = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/button[2]/span'
# 目的站维护新增目的站
OCDestinationMaintenanceNewButton = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div'
# 目的站维护——新增/修改目的站——目的站代码
OCDestinationCode = '//div[@class="form_row"]/div[1]/div/div[1]/input'
# 目的站维护——新增/修改目的站——目的站中文名称
OCDestinationName = '//div[@class="form_row"]/div[2]/div/div[1]/input'
# 目的站维护——新增/修改目的站——目的站英文名称
OCDestinationEnglishName = '//div[@class="form_row"]/../div[2]/div/div/input'
# 目的站维护——新增/修改目的站——提交
OCDestinationSubmit = '//div[contains(text(),"提交")]'
# 目的站维护——新增/修改目的站——取消
OCDestinationCancel = '//div[@class="ivu-drawer-wrap"]/div/div/a/i'
# 目的站维护——跳到尾页
OCDestinationLastPage = '//div[@class="cvu-paginator-warp"]/span[4]'
# 目的站维护修改
OCDestinationEdit = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/ul/li[last()]/div[1]/div[2]/div/button[1]/span'
# 目的站维护删除
OCDestinationDelete = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/ul/li[last()]/div[1]/div[2]/div/button[2]/span'
# 确定删除目的站维护数据
OCDestinationDeleteSuccess = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[1]'
# 取消对目的站数据的删除
OCDestinationDeleteCancel = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[2]'
# 删除成功
OCDestinationDeleteSuccessDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 用于重复校验
OCDestinationRepeat = '//div[@class="page"]/div/div[2]/div/div/div/div[3]/ul/li/div[3]/div/span'


# =====   =====
# 入库单维护
# 入库单入口
inBoundEntry = '//div[contains(text(),"入库单维护")]'
# 入仓地址
inBoundAddress = '//div[@class="aside_left"]/div[1]/div/textarea'
# 联系方式
inBoundPhone = '//div[@class="aside_left"]/div[2]/div/textarea'
# 备注
inBondRemark = '//div[@class="aside_left"]/div[3]/div/textarea'
# 客户须知
inBondMust = '//div[@class="aside_right"]/div/div/textarea'
# 修改保存按钮
inBondBut = '//*[@id="container"]/div/div/div[2]/div/div/div/div[3]/div/button/span'
# 操作成功回执
inBondDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'


# =====   =====
# 线路维护
# 线路维护入口
lineMaintenanceEntry = '//div[@class="shrink-menu"]/div[3]/div[2]/div/div/div[3]'
# 线路维护新增按钮
newLineMain = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div'
# 线路维护——始发地搜索框
lineStartSearch = '//div[@class="cvu-search-card-main"]/span/div/input'
# 线路维护——目的地搜索框
lineEndSearch = '//div[@class="cvu-search-card-main"]/span/div[2]/input'
# 线路维护——新增/编辑——始发地
lineMainStart = '//div[@class="form_row"]/div/div/div/input'
# 线路维护——新增/编辑——目的地
lineMainEnd = '//div[@class="form_row"]/div[2]/div/div/input'
# 线路维护——新增/编辑——线路代码
lineMainCode = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[2]/div/div/input'
# 线路维护——新增/编辑——提交
lineMainSubmit = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[3]/div'
# 线路维护——新增/编辑——取消
lineMainCancel = '//div[@class="ivu-drawer-wrap"]/div/div/a/i'
# 线路维护——停用/启用
lineMainStop = '//ul[@class="card-lists"]/li/div/div[2]/div/button/span'
# 线路维护——修改
lineMainEdit = '//ul[@class="card-lists"]/li/div/div[2]/div/button[2]/span'
# 线路维护——删除
lineMainDelete = '//ul[@class="card-lists"]/li/div/div[2]/div/button[3]/span'
# 线路维护——删除——确定
lineMainDeleteSuccess = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div'
# 线路维护——删除——取消
lineMainDeleteCancel = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[2]'
# 线路维护——操作回执
lineMainDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 用于重复校验——线路
lineMainRepeatLine = '//div[@class="page bigscreen"]/div/div[3]/ul/li[2]/div[3]/div/span'
# 用于重复检验——线路代码
lineMainRepeatCode = '//div[@class="page bigscreen"]/div/div[3]/ul/li[2]/div[1]/div[1]/div[2]/span'


# =====   =====
# 运营公司收发货公司维护
# 收发货公司维护
operationCompany = '//div[contains(text(),"收发货公司维护")]'
# 发货公司
operationShipperCompany = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]'
# 收货公司
operationConsigneeCompany = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]'
# 博正收发货公司维护——公司英文名称查询条件
operationCompanyNameSearch = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/span[1]/div/input'
# 博正收发货公司维护——公司中文名称查询条件
operationCompanyEnglishNameSearch = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/span[1]/div/input'
# 博正收发货公司维护——收发货人查询条件
operationShipperORConsigneeName = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/span[2]/div/input'
# 博正收发货公司维护——查询按钮
operationShipperORConsigneeSearch = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/button[1]/span'
# 博正收发货公司维护——重置按钮
operationShipperORConsigneeReset = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/button[2]/span'
# 博正收发货公司维护——新增收发货信息
operationAddShipperORConsignee = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div[1]/div'
# 博正收发货公司维护——新增收发货信息——公司中文名称
operationAddOREditCompanyName = '//div[@class="content_wrap modal-warp"]/form/div/div/div/div/input'
# 博正收发货公司维护——新增收发货信息——公司英文名称
operationAddOREditCompanyEnglishName = '//div[@class="content_wrap modal-warp"]/form/div/div[2]/div/div/input'
# 博正收发货公司维护——新增收发货信息——公司地址
operationAddOREditCompanyAddress = '//div[@class="content_wrap modal-warp"]/form/div[2]/div/div/div/input'
# 博正收发货公司维护——新增收发货信息——收发货人电话
operationAddOREditShipperConsigneePhone = '//div[@class="content_wrap modal-warp"]/form/div[2]/div[2]/div/div/input'
# 博正收发货公司维护——新增收发货信息——提交按钮
operationAddOREditCompanySubmit = '//div[contains(text(),"提交")]'
# 博正收发货公司维护——新增收发货信息——取消按钮
operationAddOREditCompanyCancel = '//div[@class="ivu-drawer-wrap"]/div/div/a/i'
# 新增收发货公司操作成功反馈
operationCompanyNameOperationSuccess = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 跳到尾页
operationCompanyLastPage = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div[2]/div/span[4]'
# 修改按钮
operationCompanyEditButton = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/ul/li[last()]/div[1]/div[2]/div/button[1]/span'
# 删除按钮
operationCompanyDeleteButton = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/ul/li[last()]/div[1]/div[2]/div/button[2]/span'
# 删除确定
operationCompanyDeleteSuccess = '//div[@class="cvu-modal-btn"]'
# 删除取消
operationCompanyDeleteCancel = '//div[@class="cvu-modal-btn"][2]'
# 删除成功提示
operationCompanyDeleteSuccessDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 用于重复校验
operationCompanyRepeat = '//div[@class="page bigscreen"]/div/div[4]/ul/li/div[3]/div/span'


# =====   =====
# 功能区维护
# 功能区维护入口
areaFunction = '//div[contains(text(),"功能区维护")]'
# 新增功能区
addAreaFunctionBut = '//div[@class="pages-component"]/div[1]/div'
# 新增功能区——功能区名称
areaFunctionName = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div/div/div/div/input'
# 新增功能区——功能区类型
areaFunctionType = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div/div[2]/div/div/div/div/span'
# 新增功能区——下拉选择第一个
areaFunctionTypeSec = '//ul[@class="ivu-select-dropdown-list"]/li[1]'
# 新增功能区——备注
areaFunctionRemark = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[2]/div/div/textarea'
# 新增功能区——提交
areaFunctionBut = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[3]/div'
# 新增功能区——取消
areaFunctionCancel = '//div[@class="ivu-drawer-wrap"]/div/div/a/i'
# 作业区信息按钮
areaFunctionInfo = '//div[@class="page bigscreen"]/div/div[3]/ul/li[last()]/div/div[2]/div/button/span'
# 作业区信息——新增作业区
areaFuncInfoNew = '//button[@class="add_btn"]'
# 作业区信息——区域名称
areaFuncInfoAreaName = '//div[@class="drawerTable cardForm ivu-table-wrapper ivu-table-wrapper-with-border"]/div/div[2]/table/tbody/tr[last()]/td[2]/div/div/div/div/input'
# 作业区信息——列数最大值
areaFuncInfoMaxCol = '//div[@class="drawerTable cardForm ivu-table-wrapper ivu-table-wrapper-with-border"]/div/div[2]/table/tbody/tr[last()]/td[3]/div/div/div/div/input'
# 作业区信息——行数最大值
areaFuncInfoMaxRow = '//div[@class="drawerTable cardForm ivu-table-wrapper ivu-table-wrapper-with-border"]/div/div[2]/table/tbody/tr[last()]/td[4]/div/div/div/div/input'
# 作业区信息——类型
areaFuncInfoAreaType = '//div[@class="drawerTable cardForm ivu-table-wrapper ivu-table-wrapper-with-border"]/div/div[2]/table/tbody/tr[last()]/td[5]/div/div/div/div/div/div/span'
# 作业区信息——类型——放行
areaFuncInfoAreaRel = '//body[@class="bigscreen"]/div[last()]/ul[2]/li[2]'
# 作业区信息——类型——查验
areaFuncInfoAreaCheck = '//body[@class="bigscreen"]/div[last()]/ul[2]/li[1]'
# 作业区信息——编号
areaFuncInfoAreaNum = '//div[@class="drawerTable cardForm ivu-table-wrapper ivu-table-wrapper-with-border"]/div/div[2]/table/tbody/tr[last()]/td[6]/div/div/div/div/input'
# 作业区信息——修改
areaFunctionInfoEdit = '//div[@class="drawerTable cardForm ivu-table-wrapper ivu-table-wrapper-with-border"]/div/div[2]/table/tbody/tr[last()]/td[7]/div/div/div/button/span'
# 取消按钮
areaFunctionInfoEditCancel = '//div[@class="ivu-drawer-wrap"]/div/div/a/i'
# 作业区信息——删除
areaFunctionInfoDelete = '//div[@class="drawerTable cardForm ivu-table-wrapper ivu-table-wrapper-with-border"]/div/div[2]/table/tbody/tr[last()]/td[7]/div/div/div/button[2]/span'
# 作业区信息——修改——暂存区——第一行位置
areaFunctionInfoFirst = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第二行位置
areaFunctionInfoSecond = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第三行位置
areaFunctionInfoThird = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第四行位置
areaFunctionInfoForth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[4]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第五行位置
areaFunctionInfoFifth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[5]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第六行位置
areaFunctionInfoSixth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[6]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第七行位置
areaFunctionInfoSeventh = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[7]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第八行位置
areaFunctionInfoEighth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[8]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第九行位置
areaFunctionInfoNinth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第十行位置
areaFunctionInfoTenth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第十一行位置
areaFunctionInfoEleventh = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[3]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第十二行位置
areaFunctionInfoTwelfth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[4]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第十三行位置
areaFunctionInfoThirteen = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[5]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第十四行位置
areaFunctionInfoFourteenth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[6]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第十五行位置
areaFunctionInfoFifteenth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[7]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——第十六行位置
areaFunctionInfoSixteenth = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[8]/td[2]/div/div/div/input'
# 作业区信息——修改——暂存区——保存
areaFunctionInfoSave = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[3]/div'
# 作业区信息——修改——暂存区——取消
areaFunctionInfoCancel = '//div[@class="cvu-modal cvu-modal-bigscreen rule-modal cvu-modal-show"]/div[2]/div[3]/div[2]'
# 修改
areaFunctionEdit = '//div[@class="page bigscreen"]/div/div[3]/ul/li/div/div[2]/div/button[2]/span'
# 删除
areaFunctionDelete = '//div[@class="page bigscreen"]/div/div[3]/ul/li[last()]/div/div[2]/div/button[3]/span'
# 确认删除
areaFuncDelConfirm = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[1]'
# 取消删除
areaFuncDelCancel = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[2]'
# 尾页
areFunctionLastPage = '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/span[4]'
# 操作回执
areFunctionDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 为验证重复功能区名，取最新名称
areFunctionRepeatName = '//div[@class="page bigscreen"]/div/div[3]/ul/li[1]/div[3]/div/span'
# 为验证重复作业区信息，取已存在的名称
areaFuncInfoRepeatName = '//div[@class="drawerTable cardForm ivu-table-wrapper ivu-table-wrapper-with-border"]/div/div[2]/table/tbody/tr[1]/td[2]/div/div/div'


# =====   =====
# 摄像头维护
# 摄像头维护入口
cameraMain = '//div[contains(text(),"摄像头维护")]'
# 新建摄像头
newCameraMainBut = '//div[@class="page bigscreen"]/div/div[2]/div/div'
# 新建摄像头——功能区名称
cameraMainAFName = '//div[@class="ivu-drawer-wrap"]/div/div/div[2]/div/form/div/div[1]/div/div/div/div/span'
# 新建摄像头——功能区名称——选择第一个功能区
cameraMainAFN1 = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"]/ul[2]/li[1]'
# 新建摄像头——区域名称
cameraMainAFAreaName = '//div[@class="ivu-drawer-wrap"]/div/div/div[2]/div/form/div/div[2]/div/div/div/div/span'
# 新建摄像头——区域名称——选择第一个区域
cameraMainAFAN1 = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][2]/ul[2]/li[1]'
# 新建摄像头——摄像头名称
cameraMainCName = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[2]/div[1]/div/div/input'
# 新建摄像头——IP地址
cameraMainIP = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[2]/div[2]/div/div/input'
# 新建摄像头——通道号
cameraMainChannel = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[3]/div[1]/div/div/input'
# 新建摄像头——设备编号
cameraMainEquipment = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[3]/div[2]/div/div/input'
# 新建摄像头——用户名
cameraMainUserName = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[4]/div[1]/div/div/input'
# 新建摄像头——密码
cameraMainPassword = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[4]/div[2]/div/div/input'
# 新建摄像头——提交
cameraMainSubmit = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[5]/div'
# 新建摄像头——取消
cameraMainCancel = '//div[@class="ivu-drawer-wrap"]/div/div/a/i'
# 修改
cameraMainEdit = '//div[@class="page bigscreen"]/div/div[3]/ul/li/div/div[2]/div/button/span'
# 删除
cameraMainDelete = '//div[@class="page bigscreen"]/div/div[3]/ul/li/div/div[2]/div/button[2]/span'
# 查看详情
cameraMainDetail = '//div[@class="page bigscreen"]/div/div[3]/ul/li/div/div[2]/div[2]/span'
# 删除确定
cameraMainDeleteConfirm = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[1]'
# 取消删除
cameraMainDeleteCancel = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[2]'
# 操作成功回执
cameraMainOptDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 用于重复的原始数据位置
cameraRepeatName = '//div[@class="page bigscreen"]/div/div[3]/ul/li[2]/div[3]/div[2]/span'


# =====已确认=====
# 预约时间维护
# 预约时间维护入口 /html/body/div[2]/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[7]
resTimeEntry = '//div[contains(text(),"预约时间维护")]'
# 提前预约时间
resTimeBeforeIn = '//div[@class="container"]/div[2]/div/span/div/div/div/span'
# 提前预约时间——选择48小时
resTimeBeforeInSec48 = '//ul[@class="ivu-select-dropdown-list"]/li[2]'
# 提前预约时间——保存
resTimeBeforeInSave = '//div[@class="save_container"]/div[2]/button/span'
# 新增预约时间
resTimeNew = '//button[@class="add_btn"]'
# 触发进场时间控件
resTimeBut = '//div[@class="ivu-input-wrapper ivu-input-wrapper-default ivu-input-type-text ivu-date-picker-editor"]'
# 预约时间开始时间
resTimeStart = '//div[@class="ivu-picker-panel-content ivu-picker-panel-content-left"]/div[2]/div/ul/li[1]'
# 预约时间开始时间2
resTimeStart2 = '//div[@class="ivu-picker-panel-content ivu-picker-panel-content-left"]/div[2]/div/ul/li[2]'
# 预约时间结束时间
resTimeEnd = '//div[@class="ivu-picker-panel-content ivu-picker-panel-content-right"]/div[2]/div/ul/li[2]'
# 预约时间结束时间2
resTimeEnd2 = '//div[@class="ivu-picker-panel-content ivu-picker-panel-content-right"]/div[2]/div/ul/li[3]'
# 预约时间提交
resTimeSub = '//div[@class="btn btn-confirm"]'
# 预约时间取消
resTimeCancel = '//div[@class="ivu-drawer-wrap"]/div/div/a/i'
# 启用/停用
resTimeEnOrDisable = '//div[@class="content"]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/div/button/span'
# 修改
resTimeEdit = '//div[@class="content"]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/div/button[2]/span'
# 删除
resTimeDelete = '//div[@class="content"]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/div/button[3]/span'
# 确认删除
resTimeDeleteConfirm = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[1]'
# 取消删除
resTimeDeleteCancel = '//div[@class="cvu-modal-bigscreen cvu-modal cvu-modal-show"]/div[2]/div[3]/div[2]'
# 操作回执
resTimeDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'


# =====已确认=====
# 集装箱规格维护
# 集装箱规格维护入口
containerType = '//div[contains(text(),"集装箱规格维护")]'
# 新增箱型入口
containerTypeNewBut = '//*[@id="container"]/div/div/div[2]/div/div/div/div[2]/div[1]/div'
# 新增箱型——规格
conSpecifications = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div/div/div/div/input'
# 新增箱型——配货毛重
containerWeight = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div/div[2]/div/div/input'
# 新增箱型——体积
containerVolume = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[2]/div/div/div/input'
# 新增箱型——皮重
containerTare = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[2]/div[2]/div/div/input'
# 新增箱型——提交
containerSubmit = '//form[@class="cardForm ivu-form ivu-form-label-right"]/div[3]/div'
# 新增箱型——取消
containerCancel = '//div[@class="ivu-drawer-wrap"]/div/div/a/i'
# 修改箱型
containerEditBut = '//*[@id="container"]/div/div/div[2]/div/div/div/div[3]/ul/li[8]/div[1]/div[2]/div/button/span'
# 操作成功回执
containerDetail = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
# 用于重复校验的集装箱箱型
containerRepeat = '//div[@class="page bigscreen"]/div/div[3]/ul/li[1]/div[3]/div[1]/span'

# 堆存管理
# 入口
entryStorageMan = '//p[contains(text(), "堆存管理")]'
# 装箱计划确认
packagePlanConfirm = '//div[@class="item aside_right"]/div/button[2]'
# 装箱计划确认的集装箱号输入框
packPlanConfirmConNum = '//div[@class="cvu-modal cvu-modal-bigscreen detail-body bigscreen cvu-modal-show"]/div[2]/div[2]/div/div/div/input'
# 装箱计划确认的查询按钮
packPlanConfirmSearch = '//div[@class="cvu-modal cvu-modal-bigscreen detail-body bigscreen cvu-modal-show"]/div[2]/div[2]/div/div/button/span'
# 实际装箱区
packActualArea = '//div[@class="ivu-select ivu-select-single ivu-select-default"]/div/div/span'
# 实际装箱区下拉列表——装箱区1
packActualAreaIndex1 = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"]/ul[2]/li[1]'
# 实际装箱区下拉列表——装箱区2
packActualAreaIndex2 = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"]/ul[2]/li[2]'
# 实际装箱区下拉列表——装箱区3
packActualAreaIndex3 = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"]/ul[2]/li[3]'
# 装箱计划确认
packPlanConfirmSubmit = '//div[@class="cvu-modal cvu-modal-bigscreen detail-body bigscreen cvu-modal-show"]/div[2]/div[2]/div[3]/div/div/div[2]/table/tbody/tr//td[5]/div/div/button/span'
# 取消计划确认
packPlanConfirmCancel = '//div[contains(text(),"装箱区堆存确认")]/../div[2]/i'
# 移位计划导出
shiftPlan = '//button[contains(text(), "移位计划导出")]'
# 移位计划导出界面集装箱号查询条件
packMovePlanExportConNum = '//div[@class="cvu-modal cvu-modal-bigscreen detail-body bigscreen cvu-modal-show"]/div[2]/div[2]/div/div/div/input'
# 移位计划导出的查询按钮
packMovePlanExportConNumSearch = '//div[@class="cvu-modal cvu-modal-bigscreen detail-body bigscreen cvu-modal-show"]/div[2]/div[2]/div/div/button/span'
# 移位计划导出
packMovePlanExport = '//div[@class="cvu-modal cvu-modal-bigscreen detail-body bigscreen cvu-modal-show"]/div[2]/div[2]/div[3]/div/div/div[2]/table/tbody/tr/td[4]/div/div/button/span'
# 取消导出移位计划
movePlanCancel = '//div[@class="cvu-modal cvu-modal-bigscreen detail-body bigscreen cvu-modal-show"]/div[2]/div/div[2]/i'


# 装箱管理
# 入口
entryPackageMan = '//p[contains(text(), "装箱管理")]'
# 待装箱货物第一个
waitForPackage = '//div[@class="body-left"]/ul[1]/li[1]'
# 计划入箱货物
planToPackage = '//div[@class="card-lists-body"]/ul[1]/li[1]'
# 货物装箱区域
planArea = '//div[@class="card-lists-body"]'
# 保存装箱计划
savePackPlan = '//div[@class="body-center"]/div[2]/div[2]/button/span'
# 保存装箱报告
savePackReport = '//div[@class="body-center"]/div[2]/div[2]/button[2]/span'
# 集装箱类型
containerTypePack = '//div[@class="form-items"]/div/div/span/div/div/div/span'
# 集装箱类型下拉选
containerTypePackIndex = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][1]/ul[2]/li[1]'
# 集装箱号
containerNum = '//div[@class="form-items"]/div[2]/div/span/div/input'
# 装箱区域
packageArea = '//div[@class="form-items"]/div[3]/div/span/div/div/div/span'
# 装箱区域下拉选
packageAreaIndex = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][2]/ul[2]/li[1]'
# 计划/报告状态查询
planOrReportStatus = '//div[@class="body-right"]/div[2]/div/div[2]/div/div/div/span'
# 计划/报告状态查询下拉选已申报
planOrReportStatusAlready = '//li[contains(text(),"已申报")]'
# 查询按钮
planOrReportSearchBut = '//div[@class="body-right"]/div[2]/div[2]/div/button/span'
# 装箱计划/导出修改
packPlanOrReportEdit = '//div[@class="body-right"]/ul/li[1]/div[1]/div[2]/div/span[1]/button/span'
# 装箱计划/装箱报告导出
packPlanOrReportExport = '//div[@class="body-right"]/ul/li[1]/div[1]/div[2]/div/span[3]/button/span'
# 装箱计划/装箱报告申报
planOrReportDeclare = '//div[@class="body-right"]/ul/li[1]/div[1]/div[2]/div/span[2]/button/span'
# 装箱计划查询页签切换
planPage = '//span[contains(text(),"装箱计划查询")]'
# 装箱报告查询页签切换
reportPage = '//span[contains(text(),"装箱报告查询")]'
# 装箱计划/装箱报告查询界面定位元素
planOrReportAssert = '//div[@class="container"]/div[3]/div[3]/div'
# 上传装箱照片按钮
reportPhotoUpLoad = '//span[contains(text(),"上传照片")]'
# 添加装箱照片
reportPhotoUpLoadAdd = '//div[@class="upload-body operation-body detail-body bigscreen"]/div/div[2]/ul/li/div/i'
# 上传照片提交
reportPhotoUpLoadSubmit = '//div[@class="upload-body operation-body detail-body bigscreen"]/div[2]/div/button/span'
# 已计划/报告的集装箱号
conNumPlanedOrReported = '//div[@class="container"]/div[3]/div[3]/ul/li/div/div/div/span'
# 随车附件弹窗
withTrainAccessor = '//div[@class="body-right"]/ul/li[1]/div[1]/div[2]/div/span[4]/button/span'
# 收货——公司英文名称
consigneeEngAddress = '//div[@class="table-row-warp"]/div/div/div/table/tbody/tr[4]/td[3]/div/div/div/div/div/div/input'
# 收货——公司英文名称——选择第一个
consigneeEngAddressFirst = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][2]/ul[2]/li[1]'
# 发票号
invoiceNo = '//div[@class="table-row-warp"]/div/div/div/table/tbody/tr[4]/td[5]/div/div/div/div/input'
# 集装箱卸货站
containerDestineStation = '//div[@class="table-row-warp"]/div[2]/div/div/table/tbody/tr/td[7]/div/div/div/div/div/div/input'
# 集装箱卸货站——第一个选项
containerDestineStationFirst = '//div[@class="ivu-select-dropdown ivu-select-dropdown-transfer"][3]/ul[2]/li[1]'
# 随车附件——保存
saveWithTrainAccessor = '//div[@class="boardlist-body detail-body bigscreen"]/div/div[3]/div/button[1]/span'
# 导出随车单据
exportAccessor = '//div[@class="boardlist-body detail-body bigscreen"]/div/div[3]/div/button[2]/span'
# 导出stuffing-list
exportStuffingList = '//div[@class="boardlist-body detail-body bigscreen"]/div/div[3]/div/button[3]/span'
# 操作回执
optionBack = 'body > div.ivu-message > div > div > div:nth-child(1) > div > span'
