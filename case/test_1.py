# coding=utf-8
import unittest
from time import sleep
from base.MyDriver import nox
from base.MyLog import logger

class WeiFuHua(unittest.TestCase):
    def setUp(self):
        self.driver = nox.driver()
        self.driver.implicitly_wait(6)

    def tearDown(self):
        self.driver.quit()

    #@unittest.skip("这是case1")
    def test_a(self):
        logger.info("case1")
        self.driver.find_element_by_xpath("//android.widget.Button[@text='我的']").click()
        sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WeiFuHua)
    unittest.TextTestRunner(verbosity=2).run(suite)