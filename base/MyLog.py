# coding=utf-8
import logging
import os

class Log:
    def __init__(self, logPath, loglevel, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        """
        # 用字典保存日志级别,级别越高表示打出来的日志越详细
        level_dict = {
            1: logging.CRITICAL,
            2: logging.ERROR,
            3: logging.WARNING,
            4: logging.INFO,
            5: logging.DEBUG
        }

        #如果result文件夹存在log文件则删除
        if os.path.exists(logPath) is True:
            os.remove(logPath)

        #接受自定义级别
        level = level_dict[int(loglevel)]

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logPath)
        fh.setLevel(level)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlogger(self):
        return self.logger

logger = Log(logPath="D:\\PycharmProject\\Appium\\result\\outLog.log", loglevel=5, logger=None).getlogger()
if __name__ == '__main__':
    logger.info("我是info")
    logger.debug("我是debug")
    logger.error("我是error")
    logger.warning("我是warning")
    logger.critical("我是critical")