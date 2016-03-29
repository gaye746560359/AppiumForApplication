# coding=utf-8
import unittest
from base.DataBase import *
from base.MeThod import MeThod
from base.MyLog import logger

class WeiFuHua(unittest.TestCase):
    def setUp(self):
        self.driver = MeThod()
        self.driver.api.implicitly_wait(6)

    def tearDown(self):
        self.driver.api.quit()

    def test_a(self):
        self.driver.out()
        try:
            self.driver.findElement("xpath", "4").send_keys(db_riche.select("number", "4"))
            self.driver.findElement("xpath", "5").send_keys(db_riche.select("number", "2"))
            self.driver.findElement("xpath", "6").click()
            logger.info("开始查找账号")
            text=self.driver.findElement("xpath","9").text
        except Exception:
            text=None
            self.assertIsNotNone(text, msg="没有找到账号")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WeiFuHua)
    unittest.TextTestRunner(verbosity=2).run(suite)