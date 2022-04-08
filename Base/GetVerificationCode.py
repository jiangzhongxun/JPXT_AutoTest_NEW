import os
import ddddocr
from time import sleep
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By


class GetVerificationCode:

    def __init__(self):

        self.res = None
        url = 'http://192.168.1.211:8010/login?redirect=%252Fbusiness%252Fcustomer%252Fentrust%252Findex'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 将浏览器最大化
        self.driver.get(url)


    def getVerification(self):

        # 获取当前文件的位置、并获取保存截屏的位置
        current_location = os.path.dirname(__file__)
        screenshot_path = os.path.join(current_location, "..", "VerificationCode")

        # 截取当前网页并放到自定义目录下，并命名为printscreen，该截图中有我们需要的验证码
        sleep(1)
        self.driver.save_screenshot(screenshot_path + '//' + 'printscreen.png')
        sleep(1)

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

        self.res = ocr.classification(img_bytes)

        print('识别出的验证码为：' + self.res)


    def login(self):

        self.getVerification()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/'
                                           'div[2]/form/div[1]/div/div/input').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/'
                                           'div[2]/form/div[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/'
                                           'div[2]/form/div[3]/div/div[1]/input').send_keys(self.res)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/button').click()

        # sleep(5)
        # self.driver.quit()


if __name__ == '__main__':
    GetVerificationCode().login()
