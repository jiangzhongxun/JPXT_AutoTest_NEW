import random
import string
from time import sleep
from selenium.webdriver.common.by import By
from Base.BasePage import BasePage
import Base.PositionElement as  BP


class LineMaintenance(BasePage):
    lineAndCode = [["af", "阿富汗"], ["al", "阿尔巴尼亚"], ["dz", "阿尔及利亚"], ["us", "美国"], ["ad", "安道尔"], ["ao", "安哥拉"], ["ag", "安提瓜和巴布达"], ["ae", "阿联酋"], ["ar", "阿根廷"], ["am", "亚美尼亚"], ["au", "澳大利亚"], ["at", "奥地利"], ["az", "阿塞拜疆"], ["bs", "巴哈马"], ["bh", "巴林"], ["bd", "孟加拉"], ["bb", "巴巴多斯"], ["by", "白俄罗斯"], ["be", "比利时"], ["bz", "伯利兹"], ["bj", "贝宁"], ["bt", "不丹"], ["bo", "玻利维亚"], ["ba", "波斯尼亚"], ["bw", "博茨瓦纳"], ["br", "巴西"], ["bn", "文莱"], ["bg", "保加利亚"], ["bf", "布基纳法索"], ["bi", "布隆迪"], ["kh", "柬埔寨"], ["cm", "喀麦隆"], ["ca", "加拿大"], ["cf", "中非"], ["td", "乍得"], ["cl", "智利"], ["co", "哥伦比亚"], ["km", "科摩罗"], ["cd", "刚果布"], ["cg", "刚果金"], ["cr", "哥斯达黎加"], ["ci", "科特迪瓦"], ["hr", "克罗地亚"], ["cy", "塞浦路斯"], ["cz", "捷克"], ["dk", "丹麦"], ["dj", "吉布提"], ["dm", "多米尼克"], ["do", "多米尼加"], ["ec", "厄瓜多尔"], ["eg", "埃及"], ["sv", "萨尔瓦多"], ["gb", "英国"], ["gq", "赤道几内亚"], ["er", "厄立特里亚"], ["ee", "爱沙尼亚"], ["et", "埃塞俄比亚"], ["fj", "斐济"], ["fi", "芬兰"], ["fr", "法国"], ["ga", "加蓬"], ["gm", "冈比亚"], ["ge", "格鲁吉亚"], ["de", "德国"], ["gh", "加纳"], ["gr", "希腊"], ["gd", "格林纳达"], ["gt", "危地马拉"], ["cu", "古巴"], ["gn", "几内亚"], ["gw", "几内亚比绍"], ["gy", "圭亚那"], ["ht", "海地"], ["nl", "荷兰"], ["hn", "洪都拉斯"], ["hu", "匈牙利"], ["is", "冰岛"], ["in", "印度"], ["id", "印尼"], ["ir", "伊朗"], ["iq", "伊拉克"], ["ie", "爱尔兰"], ["il", "以色列"], ["it", "意大利"], ["jm", "牙买加"], ["jp", "日本"], ["jo", "约旦"], ["kz", "哈萨克斯坦"], ["ke", "肯尼亚"], ["kg", "吉尔吉斯"], ["ki", "基里巴斯"], ["kr", "韩国"], ["kw", "科威特"], ["la", "老挝"], ["lv", "拉脱维亚"], ["lb", "黎巴嫩"], ["ls", "莱索托"], ["lr", "利比里亚"], ["ly", "利比亚"], ["li", "列支敦士登"], ["lt", "立陶宛"], ["lu", "卢森堡"], ["mk", "马其顿"], ["mg", "马达加斯加"], ["mw", "马拉维"], ["my", "马来西亚"], ["mv", "马尔代夫"], ["ml", "马里"], ["mt", "马耳他"], ["mh", "马绍尔群岛"], ["mr", "毛里塔尼亚"], ["mu", "毛里求斯"], ["mx", "墨西哥"], ["fm", "密克罗尼西亚"], ["md", "摩尔多瓦"], ["mc", "摩纳哥"], ["mn", "蒙古"], ["me", "黑山共和国"], ["ma", "摩洛哥"], ["mz", "莫桑比克"], ["mm", "缅甸"], ["na", "纳米比亚"], ["nr", "瑙鲁"], ["np", "尼泊尔"], ["nz", "新西兰"], ["ni", "尼加拉瓜"], ["ne", "尼日尔"], ["ng", "尼日利亚"], ["kp", "朝鲜"], ["no", "挪威"], ["om", "阿曼"], ["pk", "巴基斯坦"], ["pw", "帕劳"], ["ps", "巴勒斯坦"], ["pa", "巴拿马"], ["pg", "新几内亚"], ["py", "巴拉圭"], ["pe", "秘鲁"], ["ph", "菲律宾"], ["pl", "波兰"], ["pt", "葡萄牙"], ["qa", "卡塔尔"], ["ro", "罗马尼亚"], ["ru", "俄罗斯"], ["rw", "卢旺达"], ["kn", "圣基茨和尼维斯"], ["vc", "圣文森特和格林纳丁斯"], ["lc", "圣卢西亚"], ["ws", "萨摩亚"], ["sm", "圣马力诺"], ["st", "圣多美和普林西比"], ["sa", "沙特"], ["sn", "塞内加尔"], ["rs", "塞尔维亚"], ["sc", "塞舌尔"], ["sl", "塞拉利昂"], ["sg", "新加坡"], ["sk", "斯洛伐克"], ["si", "斯洛文尼亚"], ["sb", "所罗门群岛"], ["so", "索马里"], ["ss", "南苏丹"], ["za", "南非"], ["es", "西班牙"], ["lk", "斯里兰卡"], ["sd", "苏丹"], ["sr", "苏里南"], ["sz", "斯威士兰"], ["se", "瑞典"], ["ch", "瑞士"], ["sy", "叙利亚"], ["tj", "塔吉克斯坦"], ["tz", "坦桑尼亚"], ["th", "泰国"], ["tl", "东帝汶"], ["tg", "多哥"], ["to", "汤加"], ["tt", "特立尼达和多巴哥"], ["tn", "突尼斯"], ["tr", "土耳其"], ["tm", "土库曼斯坦"], ["tv", "图瓦卢"], ["ug", "乌干达"], ["ua", "乌克兰"], ["uy", "乌拉圭"], ["uz", "乌兹别克斯坦"], ["vu", "瓦努阿图"], ["ve", "委内瑞拉"], ["cv", "佛得角"], ["vn", "越南"], ["ye", "也门"], ["zm", "赞比亚"], ["zw", "津巴布韦"], ["tw", "台湾"], ["va", "梵蒂冈"]]
    # 进入线路维护
    def entryLineMain(self):
        self.rollBackTop()
        self.anotherWayToClick(By.XPATH, BP.OCMaintenanceEntry)
        self.anotherWayToClick(By.XPATH, BP.lineMaintenanceEntry)
        self.driver.implicitly_wait(10)

    # 保存
    def saveLineMain(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.lineMainSubmit)

    # 取消
    def cancelLineMain(self):
        self.leftClick(By.XPATH, BP.lineMainCancel)

    # 点击新增线路
    def entryNewLine(self):
        self.anotherWayToClick(By.XPATH, BP.newLineMain)

    # 默认起始地为西安
    def addLineDFXA(self):
        sleep(1)
        self.clearText(By.XPATH, BP.lineMainStart)
        self.sendText(u'西安', By.XPATH, BP.lineMainStart)
        lineEndRandom = random.sample(self.lineAndCode, 1)
        self.clearText(By.XPATH, BP.lineMainEnd)
        self.sendText(r'%s' % lineEndRandom[0][1], By.XPATH, BP.lineMainEnd)
        self.clearText(By.XPATH, BP.lineMainCode)
        self.sendText(r'XA%s' % lineEndRandom[0][0].upper(), By.XPATH, BP.lineMainCode)

    # 输入线路内容
    def addLineContains(self, lineMainStart = None, lineMainEnd = None, lineMainCode = None):
        sleep(1)
        lineRandom = random.sample(self.lineAndCode, 2)
        if lineMainStart is None:
            self.sendText(r'%s'%lineRandom[0][1], By.XPATH, BP.lineMainStart)
        else:
            self.sendText(lineMainStart, By.XPATH, BP.lineMainStart)
        if lineMainEnd is None:
            self.sendText(r'%s'%lineRandom[1][1], By.XPATH, BP.lineMainEnd)
        else:
            self.sendText(lineMainEnd, By.XPATH, BP.lineMainEnd)
        if lineMainCode is None:
            self.sendText(r'%s%s'%(lineRandom[0][0].upper(),lineRandom[1][0].upper()), By.XPATH, BP.lineMainCode)
        else:
            self.sendText(lineMainCode, By.XPATH, BP.lineMainCode)

    # 获取已经存在的线路信息
    def getExistLineData(self):
        line = self.getElement(By.XPATH, BP.lineMainRepeatLine)
        code = self.getElement(By.XPATH, BP.lineMainRepeatCode)
        lineText = (''.join(line.text).split("：")[1]).split("\n")
        codeText = ''.join(code.text).split("：")[1]
        return lineText[0], lineText[1], codeText


    # 修改
    def editLineMain(self, text = None):
        sleep(1)
        self.leftClick(By.XPATH, BP.lineMainEdit)
        if text is None:
            self.sendText('%s' % (''.join(random.sample(string.ascii_letters, 2))).upper(),By.XPATH, BP.lineMainCode)
        else:
            self.sendText(text, By.XPATH, BP.lineMainCode)

    # 删除
    def deleteLineMain(self):
        self.leftClick(By.XPATH, BP.lineMainDelete)
        sleep(1)
        self.leftClick(By.XPATH, BP.lineMainDeleteSuccess)

    # 取消删除
    def deletePlusCancelLineMain(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.lineMainDelete)
        sleep(1)
        self.leftClick(By.XPATH, BP.lineMainDeleteCancel)

    # 线路启用/停用
    def disableOREnable(self):
        sleep(1)
        self.leftClick(By.XPATH, BP.lineMainStop)




