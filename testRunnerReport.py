import unittest
import time
import os
import sys
import HTMLTestRunner


sys.path.append(r'E:\\Cache\\PyCharm\\JPXT')

# 获取当前py文件路径地址，并进行路径分割（分割成目录路径和文件名称）
dirName, fileName = os.path.split(os.path.abspath(sys.argv[0]))
print(dirName, fileName)
casePath = r'./Case/'
result = dirName + "./Report/"


def createSuite():
    # 定义单元测试容器
    testUnit = unittest.TestSuite()

    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(casePath, pattern='*.py', top_level_dir=None)

    # 将测试用例加入测试容器中
    for test_suite in discover:
        for caseName in test_suite:
            testUnit.addTest(caseName)
    return testUnit


testCase = createSuite()

# 获取系统当前时间
currentTime = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
currentDay = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 定义个报告存放路径，支持相对路径
tdResult = result + currentDay

# if os.path.exists(tdResult):  # 检验文件夹路径是否已经存在
#     fileName = tdResult + "\\" + currentTime + "_result.html"
#     fp = open(fileName, 'wb')
#     # 定义测试报告
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Selenium测试报告', description='执行情况：')
#
#     # 运行测试用例
#     runner.run(testCase)
#     fp.close()  # 关闭报告文件
# else:
#     os.mkdir(tdResult)  # 创建测试报告文件夹
#     fileName = tdResult + "\\" + currentTime + "_result.html"
#     fp = open(fileName, 'wb')
#     # 定义测试报告
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Selenium测试报告', description='执行情况：')
#
#     # 运行测试用例
#     runner.run(testCase)
#     fp.close()  # 关闭报告文件


if os.path.exists(tdResult):  # 检验文件夹路径是否已经存在
    print('报告文件夹存在······\n正在生成测试报告······')
else:
    print('报告文件夹不存在!\n正在创建报告文件夹······')
    os.mkdir(tdResult)  # 创建测试报告文件夹
    print('报告文件夹创建完成······')

fileName = tdResult + "\\" + currentTime + "_result.html"
fp = open(fileName, 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Selenium测试报告', description='执行情况：')

# 运行测试用例
print('正在执行测试用例······\n正在生成测试报告······')
runner.run(testCase)
# 关闭报告文件
fp.close()
print('测试报告已生成！')
