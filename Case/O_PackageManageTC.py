import unittest
from time import sleep
import os
import sys
import Base.PositionElement as  BP
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SearchPage.LogIn import LogIn
from SearchPage.PackageManage import PackageManage


class PackageManageTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": "%s\File\ExportFile" % sys.path[0]}
        # prefs = {"profile.default_content_settings.popups": 0,
        #          "download.default_directory": "%s\File\ExportFile" % os.path.abspath(os.getcwd()) + os.path.sep}
        options.add_experimental_option("prefs", prefs)
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        logInEntity = LogIn(cls.driver)
        logInEntity.logInContent('admin')

    '''
    # 进入装箱计划界面
    def test01_entryIntoPlan(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.planOrReportAssert)))).text), "装箱计划查询列表")
        sleep(1)

    # 只拖拽一票货物生成装箱计划
    def test02_entryPackageManage(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.planHead()
        packMan.planBodyAdd(1)  # 拖入两票货物则给参数2
        packMan.submitPackagePlan()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "操作成功")
        sleep(1)

    # 将计划中的货物数量修改为0
    def test03_editToNone(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.clickPackPlanOrReportEdit()
        packMan.planBodyEdit()  # 编辑货物
        packMan.clickDeclare()  # 点击申报按钮
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "请添加委托信息!")
        sleep(1)
        packMan.planBodyAdd(1)
    '''
    # 堆存确认前点击申报
    def test04_beforeConfirmPlanDeclare(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.clickDeclare()  # 点击申报按钮
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "堆存未确认!")
        sleep(1)

    # 未导出移位计划点击计划确认
    def test05_planConfirm(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        conNum = packMan.getPackConNum()
        packMan.switchToStorageMan()  # 切换到堆存管理界面
        packMan.confirmPackagePlan(conNum)  # 堆存确认
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "请先导出移位计划!")
        packMan.cancelConfirmOrExport()
        sleep(1)
    
    # 导出移位计划
    def test06_exportMovePlan(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        conNum = packMan.getPackConNum()
        packMan.switchToStorageMan()  # 切换到堆存管理界面
        packMan.exportPackMovePlan(conNum)  # 导出移位计划
        packMan.cancelMovePlan()
        sleep(1)


    # 导出移位计划后进行堆存确认
    def test07_AfterExpMovePlanConfirmPlan(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        conNum = packMan.getPackConNum()
        packMan.switchToStorageMan()  # 切换到堆存管理界面
        packMan.confirmPackagePlan(conNum)  # 堆存确认
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "操作成功")
        sleep(10)
        packMan.cancelConfirmOrExport()
        sleep(1)

    # 堆存确认后不可修改
    def test08_AfterConfirmPlanCannotEdit(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        self.assertFalse(packMan.editButtonNotFound())  # 堆存确认后没有修改按钮
        sleep(1)

    # 申报装箱计划
    def test09_declarePackPlan(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.clickDeclare()  # 点击申报按钮
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "操作成功")
        sleep(1)

    # 导出装箱计划
    def test10_exportPackPlan(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.searchDeclaredPlanOrReport()
        packMan.clickPackPlanOrReportExport()
        sleep(1)

    # 切换到装箱报告
    def test11_switchToPackReport(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.switchToReport()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, BP.planOrReportAssert)))).text), "装箱报告查询列表")
        sleep(1)

    # 不上传装箱照片申报装箱报告
    def test12_declareReportWithoutPhoto(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.switchToReport()
        packMan.clickDeclare()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "请上传装箱照片")
        sleep(1)

    # 上传装箱照片之后申报装箱报告
    def test13_declareReportWithPhoto(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.switchToReport()
        packMan.clickPackPlanOrReportEdit()
        packMan.uploadReportPhoto()
        packMan.saveReportPhoto()
        packMan.submitPackageReport()
        packMan.clickDeclare()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "操作成功")
        sleep(1)

    # 导出装箱报告
    def test14_exportPackReport(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.switchToReport()
        packMan.searchDeclaredPlanOrReport()
        packMan.clickPackPlanOrReportExport()

    # 填写随车数据
    def test15_trainAccessorContains(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.switchToReport()
        packMan.searchDeclaredPlanOrReport()
        packMan.entryTrainAccessor()
        packMan.withTrainAccessorContains()
        self.assertEqual(((WebDriverWait(self.driver, 5, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, BP.optionBack)))).text), "操作成功")
        sleep(1)

    # 导出随车单据和stuffing-list
    def test16_exportTrainAccessor(self):
        packMan = PackageManage(self.driver)
        packMan.entryPackageMan()
        packMan.switchToReport()
        packMan.searchDeclaredPlanOrReport()
        packMan.entryTrainAccessor()
        packMan.exportWithTrainAccessor()






    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__name__":
    unittest.main()
