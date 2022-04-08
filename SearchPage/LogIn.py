import time
from selenium.webdriver.common.by import By
from Base.BasePage import BasePage
import Base.PositionElement as BP


class LogIn(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 进入集拼系统
    def openSys(self):
        self.getURL()

    # 输入用户名
    def logInContent(self, text):
        self.openSys()
        self.sendText(text, By.XPATH, BP.usernamePath)
        self.sendText('123456', By.XPATH, BP.passwordPath)
        time.sleep(5)
        res = self.getVerification()
        self.sendText(res, By.XPATH, BP.verificationCodePath)
        self.clickSubmit()

        # randomVerCode = ''.join(random.sample(string.digits, 5))
        # response = requests.get("http://192.168.1.210:8010/api/authGate/captcha?key=%s" % randomVerCode).content
        # localRedis = redis.Redis(host="192.168.1.210", port=6379, password="adyl@123456#", decode_responses=True)
        # code = localRedis.get("framework.captcha.%s"%randomVerCode)
        # print(code)
        # self.sendText(code, By.XPATH, BP.verificationCodePath)
        # self.leftClick(By.XPATH, BP.verificationCodePath)

    # 提交
    def clickSubmit(self):
        self.leftClick(By.XPATH, BP.loginButtonPath)

    # 客户退出登录
    def logOutSys(self):
        self.leftClick(By.XPATH, BP.customerLogOutEnter)
        self.leftClick(By.XPATH, BP.logOutPath)

    # 博正账户退出系统
    def logOutSysOper(self):
        self.leftClick(By.XPATH, BP.operationLogOutEnter)
        self.leftClick(By.XPATH, BP.logOutOperationPath)
