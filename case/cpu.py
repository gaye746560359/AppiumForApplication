# coding=utf-8
import unittest
from base.MeThod import MeThod
from time import sleep


class WeiFuHua(unittest.TestCase):
    def setUp(self):
        self.driver = MeThod()
        self.driver.api.implicitly_wait(60)  # 查找元素超时，设置6秒

    def tearDown(self):
        self.driver.api.quit()

    def swipeToDown(self):
        width = self.driver.api.get_window_size()["width"]  # 屏幕宽度
        height = self.driver.api.get_window_size()["height"]  # 屏幕高度
        self.driver.api.swipe(width / 2, float(height / 1.02), width / 2, height / 8, 2000)  # 滑动轨迹

    def test_getCpuInfo(self):
        global count
        self.driver.findElement("xpath", "7").click()  # 点击资讯按钮
        for i in range(5):
            count = i + 1
            self.driver.findElement("xpath", "8").click()  # 进入资讯详情
            sleep(1)
            for n in range(2):  # 滑动资讯详情页面到底部
                self.swipeToDown()
            self.driver.api.keyevent(4)  # 点击返回按钮

        print "总共执行：%d 次" % count


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WeiFuHua)
    unittest.TextTestRunner(verbosity=2).run(suite)
