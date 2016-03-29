# coding=utf-8
import unittest
from time import sleep
from base.MyDriver import nox1
from base.MyLog import logger

class WeiFuHua(unittest.TestCase):
    def setUp(self):
        self.driver = nox1.driver()
        self.driver.implicitly_wait(6)

    def tearDown(self):
        self.driver.quit()

    def test_b(self):
        logger.info("case2")
        self.driver.find_element_by_xpath("//android.widget.Button[@text='活动']").click()
        sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WeiFuHua)
    unittest.TextTestRunner(verbosity=2).run(suite)