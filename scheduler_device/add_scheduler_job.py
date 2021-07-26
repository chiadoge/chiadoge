#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
from pathlib import Path
from apscheduler.schedulers.blocking import BlockingScheduler
from threading import Timer
from config.config import Config
from scheduler_device import scheduler_swarm
from scheduler_device import node_notification


#repeat running always, unless you stop it by yourself
class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


#selftimer
class SelfTimer:
    def __init__(self, interval, function_name, *args, **kwargs):
        """
        :param interval:时间间隔
        :param function_name:可调用的对象
        :param args:args和kwargs作为function_name的参数
        """
        self.timer = RepeatingTimer(interval, function_name, *args, **kwargs)

    def timer_start(self):
        self.timer.start()

    def timer_cancle(self):
        self.timer.cancel()


def add_job_scheduler(config: Config, device_id):
    crypto_conf = config.get_crypto_config()
    for key in crypto_conf.keys():
        if crypto_conf[key]["enable"]:
            crypto_item_conf = crypto_conf.get(key)
            frequency_sync = crypto_item_conf.get("frequency_sync", 300)
            frequency_check_status = crypto_item_conf.get("frequency_check_status", 300)

            device_information_timer = SelfTimer(int(frequency_sync), scheduler_swarm.device_message_manager, args=(str(device_id), key, crypto_item_conf, config))
            device_information_timer.timer_start()

            node_status_timer = SelfTimer(int(frequency_check_status), node_notification.node_status_manager, args=(str(device_id), key, crypto_item_conf, config))
            node_status_timer.timer_start()


# if __name__ == '__main__':
#     conf = Config(Path("\\chiadoge\\config.yaml"))
#     add_job_scheduler(conf, "test")
