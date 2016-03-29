# coding=utf-8
import unittest
from base import HTMLTestRunner
import os
from base.MyLog import logger

logger.info("运行主程序")


def Creatsuite():
    # 定义单元测试容器
    caseunit = unittest.TestSuite()

    # 将测试用例加入测试容器中
    for case in unittest.defaultTestLoader.discover(".\\case", pattern="test_*.py", top_level_dir=None):
        logger.info("加入用例：%s" % case)
        caseunit.addTest(case)
    return caseunit


if __name__ == '__main__':
    case = Creatsuite()
    fp = open(os.path.join('.\\result', 'report.html'), 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例详情：')
    logger.info("开始运行所有case")
    runner.run(case)
    logger.info("关闭文件")
    fp.close()
