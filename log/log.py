#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import logging
from logging import handlers
import os
from config import log_config


# 创建目录
def mkdir(filename):
    path = os.path.dirname(filename)
    path = path.strip()
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)


# 日志输出
class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=5, fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        mkdir(filename)
        self.logger = logging.getLogger(filename)

        # 清空上次logging，防止出现重复输出
        self.logger.handlers = []
        # 然后再次移除当前文件logging配置
        self.logger.removeHandler(self.logger.handlers)

        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        if not self.logger.handlers:
            # 往文件里写入#指定间隔时间自动生成文件的处理器
            # 实例化TimedRotatingFileHandler
            # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
            # S 秒
            # M 分
            # H 小时、
            # D 天、
            # W 每星期（interval==0时代表星期一）
            # midnight 每天凌晨
            th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding='utf-8')

            th.setFormatter(format_str)#设置文件里写入的格式
            self.logger.addHandler(sh) #把对象加到logger里
            self.logger.addHandler(th)
            sh.close()
            th.close()


debug_logger = Logger(log_config.all_path, level='debug')
err_logger = Logger(log_config.err_path, level='error')

# if __name__ == '__main__':
#     log = Logger('all.log',level='debug')
#     log.logger.debug('debug')
#     log.logger.info('info')
#     log.logger.warning('警告')
#     log.logger.error('报错')
#     log.logger.critical('严重')
#     Logger('error.log', level='error').logger.error('error')