import os
import random
import string
import ddddocr
import pandas
import re
import pymysql
import yaml
from PIL import Image
from pymouse import PyMouse
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver, baseURL='http://192.168.1.211:8010/login'):
        self.driver = driver
        self.baseURL = baseURL

    # 进入网址
    def getURL(self):
        self.driver.get(self.baseURL)

    #  元素定位
    def getElement(self, *locator):
        return self.driver.find_element(*locator)

    # 点击事件
    def leftClick(self, *locator):
        ActionChains(self.driver).click(self.getElement(*locator)).perform()

    # 输入事件
    def sendText(self, text, *locator):
        self.clearText(*locator)
        self.driver.find_element(*locator).send_keys(text)

    def setClassText(self, className):
        return self.driver.find_elements_by_class_name(className)

    # 清除事件
    def clearText(self, *locator):
        self.driver.find_element(*locator).clear()

    # 表单切换
    def switchIframe(self, *locator):
        self.driver.switch_to.frame(self.driver.find_element(*locator))

    # 窗口切换
    def switch_window(self, n):
        self.driver.switch_to_window(self.driver.window_handles[n])

    # 退出浏览器
    def quitBroswer(self):
        self.driver.quit()

    # 读取excel内委托信息
    @classmethod
    def readExcel(cls, excelPath):
        sheet = pandas.read_excel(excelPath, sheet_name=None, keep_default_na=False)
        entrustDict = {}
        v = 0
        for k, v in sheet.items():
            v = (v.to_dict(orient='records'))
            entrustDict[k] = v
        return entrustDict, len(v)

    # 点击空白区域关闭抽屉窗口
    @classmethod
    def clickEmptyToCancel(cls):
        time.sleep(1)
        PyMouse().click(400, 400)  # 移动并且在(x,y)位置左击

    # 获取时间戳
    @classmethod
    def timeStrftime(cls):
        return time.strftime('%Y-%m-%d_%H-%M-%S')

    # 等待按钮出现并点击
    def webDriverWaitCustomClick(self, *locator):
        WebDriverWait(self.driver, 5, 1).until(EC.element_to_be_clickable((By.XPATH, *locator))).click()

    # 滑到顶部
    def rollBackTop(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    # 当按钮被覆盖无法点击使用JS形式
    def anotherWayToClick(self, *locator):
        js = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", js)

    # 滑到底部
    def rollToBottom(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    # 生成随机车牌号
    @classmethod
    def generateRegistNum(cls):
        char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
        char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
        char2 = '1234567890ABCDEFGHJKLMNPQRSTUVWXYZ'
        char3 = '1234567890'
        while True:
            code = ''
            code += char0[random.randint(1, len(char0) - 1)]
            code += char1[random.randint(1, len(char1) - 1)]
            for i in range(1, 5):
                code += char2[random.randint(1, len(char2) - 1)]
            code += char3[random.randint(1, len(char3) - 1)]
            test = re.match(
                '^\\w.[A-Z]{1}\\d{4}$|^\\w.\\d[A-Z]{2}\\d{3}$|^\\w.\\d{2}[A-Z]{1}\\d{2}$|^\\w.\\d{3}[A-Z]{1}\\d$|^\\w.\\d{5}$',
                code)
            if test:
                continue
            else:
                break
        return code

    # 随机生成集装箱号
    @staticmethod
    def generateContainerNum():
        code = ''.join(random.sample(string.ascii_uppercase, 4)) + ''.join(random.sample(string.digits, 7))
        return code

    # 获取图片导出路径
    def exportImagePath(self, fileName):
        # 本地调试路径
        # screenShotSavePath = u'%s\images\%s_%s.png' % ((sys.path[0], fileName, self.timeStrftime()))
        # TestRunner联跑路径
        screenShotSavePath = u'%s\\images\\%s_%s.png' % (
            (os.path.abspath(os.getcwd()) + os.path.sep + '.'), fileName, self.timeStrftime())
        return screenShotSavePath

    # 连接数据库并执行sql
    @staticmethod
    def connectMySQL(sql):
        # f = open((os.path.abspath(os.getcwd()) + os.path.sep + '..' + 'Data\config.yaml'), 'r', encoding='utf-8')
        currebtPath = os.path.dirname(__file__)
        filePath = os.path.join(currebtPath, "..", "Data")
        f = open((filePath + '\\config.yaml'), 'r', encoding='utf-8')
        cont = f.read()
        d = (yaml.safe_load(cont))['DB']
        db_object = pymysql.connect(user=d["User"], password=d["Password"], host=d["Host"], database=d["DatabaseName"], port=int(d["Port"]), charset="utf8")
        cursor = db_object.cursor()
        cursor.execute(sql)  # D)在数据库的游标中来执行sql语句；（任何一个sql语句）可以是select或可以是update或可以是insert等等
        db_object.commit()  # E)如果是dml语句，要提交数据库的事务。Commit操作
        selectData = cursor.fetchall()  # F)从游标中获取查询结果（select语句是有查询结果的）
        cursor.close()  # G)关闭数据库游标
        db_object.close()  # H)关闭数据库（断开数据库）
        f.close()
        return selectData  # I)把获取到的查询结果，返回出去（因为在tearDown中要用）

    # 货主登录
    def hz_login(self, user, password, code, submit):
        self.driver.find_element(By.XPATH, user).send_keys("huozhu")
        self.driver.find_element(By.XPATH, password).send_keys("123456")
        time.sleep(5)
        res = self.getVerification()
        self.driver.find_element(By.XPATH, code).send_keys(res)
        self.driver.find_element(By.XPATH, submit).click()
        time.sleep(3)

    # 管理登录
    def gl_login(self, user, password, code, submit):
        self.driver.find_element(By.XPATH, user).send_keys("admin")
        self.driver.find_element(By.XPATH, password).send_keys("123456")
        time.sleep(5)
        res = self.getVerification()
        self.driver.find_element(By.XPATH, code).send_keys(res)
        self.driver.find_element(By.XPATH, submit).click()
        time.sleep(3)

    # 报关行登录
    def bgh_login(self, user, password, code, submit):
        self.driver.find_element(By.XPATH, user).send_keys("李四")
        self.driver.find_element(By.XPATH, password).send_keys("123456")
        time.sleep(5)
        res = self.getVerification()
        self.driver.find_element(By.XPATH, code).send_keys(res)
        self.driver.find_element(By.XPATH, submit).click()
        time.sleep(3)

    # 重命名文件
    @staticmethod
    def renameFile(oldFileName, newFileName):
        filePath = os.path.abspath(os.getcwd()) + os.path.sep + 'File\\ExportFile\\'
        print("filePath: ", filePath)
        os.rename(filePath + oldFileName, filePath + newFileName)

    # 获取验证码
    def getVerification(self):
        # 获取当前文件的位置、并获取保存截屏的位置
        current_location = os.path.dirname(__file__)
        screenshot_path = os.path.join(current_location, "..", "VerificationCode")

        # 截取当前网页并放到自定义目录下，并命名为printscreen，该截图中有我们需要的验证码
        time.sleep(1)
        self.driver.save_screenshot(screenshot_path + '//' + 'printscreen.png')
        time.sleep(1)

        # 定位验证码
        imgelement = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/'
                                                        'div[2]/div/div[2]/form/div[3]/div/div[2]/img')

        # 获取验证码x,y轴坐标
        location = imgelement.location
        # print(location)  # {'x': 885, 'y': 415}

        # 获取验证码的长宽
        size = imgelement.size
        # print(size)  # {'height': 34, 'width': 128}

        # 写成我们需要截取的位置坐标
        rangle = (int(location['x'] + 430),
                  int(location['y'] + 200),
                  int(location['x'] + size['width'] + 530),
                  int(location['y'] + size['height'] + 250))

        # 打开截图
        i = Image.open(screenshot_path + '//' + 'printscreen.png')

        # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4 = i.crop(rangle)
        frame4 = frame4.convert('RGB')

        # 保存我们截下来的验证码图片 进行打码
        frame4.save(screenshot_path + '//' + 'code.png')
        ocr = ddddocr.DdddOcr()
        with open(screenshot_path + '//' + 'code.png', 'rb') as f:
            img_bytes = f.read()

        res = ocr.classification(img_bytes)
        print('识别出的验证码为：' + res)
        return res
