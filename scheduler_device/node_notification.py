#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import os
from pathlib import Path
from config.config import Config
from log import log
from objdict import ObjDict
from datetime import datetime
from server_api.http_function import HttpFunction
from parsers import harvester_parser
import threading
import multiprocessing

config_all = ObjDict()
cmd_enum = {
    "restart_farmer": "  start --restart farmer-only",
    "restart_harvester": "  start --restart harvester"
}


# execute command, and return the output
def exec_cmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


# 控制重启并发送错误邮件
def is_restart(reboot, executable_full_path, name):
    if reboot:
        cmd_reboot_farmer = executable_full_path + cmd_enum[name]
        cmd_result = exec_cmd(cmd_reboot_farmer)
        log.debug_logger.logger.info(cmd_result)
        return "已帮您自动重启"


# 控制重启并发送错误邮件
def is_send_email(device_id, key, is_email, msg):
    if is_email:
        # 发送错误信息到服务器，用于邮件提醒
        result = HttpFunction(config_all).send_message_for_email(device_id, key, msg)
        if result is not None:
            log.debug_logger.logger.info(key+" sync email result:" +str(result["data"]))


def farmer_status(device_id, key, executable_full_path, farmer_reboot, farmer_email):
    log.debug_logger.logger.info("start check farmer status: "+key)


    # 判断farmer是否在正常工作
    # 1、节点是不是在同步，如果已经完成同步，判断是否在farming
    # 2、如果正在同步，不作任何处理
    # 3、如果没有同步或者不可用，通知用户进行同步
    cmd_get_farm = executable_full_path + ''' farm summary'''
    get_farm = exec_cmd(cmd_get_farm)
    cmd_name = "restart_farmer"
    if "Farming status: synced" in get_farm:
        print("to do")
        # result_farming = match_logfile.match()
        #
        #
        #
        # if result_farming is None or len(result_farming) <= 0:
        #     # 说明没有在farming
        #     msg = "Farmer没有在工作，请检查！"
        #     msg += is_restart(farmer_reboot, executable_full_path, cmd_name)
        #     is_send_email(device_id, key, farmer_email, msg)
        # else:
        #     # 提取匹配到的字符串
        #     dealLineRex = r"(.*) harvester .*(\d) plots .* farming (.*)\.\.\. Found (\d) .*me: (.*) s\. Total (.*) plots"
        #     linegroups = re.search(dealLineRex, result_farming)
        #     if linegroups is None:
        #         # 说明没有在farming
        #         msg = "Farmer没有在工作，请检查！"
        #         msg += is_restart(farmer_reboot, executable_full_path, cmd_name)
        #         is_send_email(device_id, key, farmer_email, msg)
        #         return
        #
        #     # 最新的plot时间
        #     plottime = datetime.strptime(linegroups.group(1), "%Y-%m-%dT%H:%M:%S.%f")
        #     # 判断plottime是不是最近10分钟内生成的（这里没有特殊含义，10分钟检查一次，如果在10分钟内没有plot信息，可以认定Farmer出现了问题）
        #     now_time = datetime.now()
        #     if ((now_time - plottime).total_seconds()) > 60 * 10:
        #         msg = "Farmer没有在工作，请检查！"
        #         msg += is_restart(farmer_reboot, executable_full_path, cmd_name)
        #         is_send_email(device_id, key, farmer_email, msg)

    elif "Farming status: Not synced or not connected to peers" in get_farm:
        msg = "节点未同步，请先同步节点！"
        msg += is_restart(farmer_reboot, executable_full_path, cmd_name)
        is_send_email(device_id, key, farmer_email, msg)

    elif "Farming status: Not available" in get_farm:
        msg = "节点未同步，请先同步节点！"
        msg += is_restart(farmer_reboot, executable_full_path, cmd_name)
        is_send_email(device_id, key, farmer_email, msg)


def harvester_status(device_id, key, crypto_item_conf, executable_full_path, harvester_reboot, harvester_email):
    log.debug_logger.logger.info("start check harvester status: "+key)


    # 判断harvester是否在正常工作
    # debug.log日志路径
    result_data = harvester_parser.harvester_parser(device_id, crypto_item_conf, key, executable_full_path, harvester_reboot, harvester_email)

    if not result_data.get("code"):
        cmd_name = "restart_harvester"
        restart_msg = is_restart(harvester_reboot, executable_full_path, cmd_name)

        msg = result_data.get("msg")
        is_send_email(device_id, key, harvester_email, msg + " " + restart_msg)


def node_status_manager(device_id, key, crypto_item_conf, config):
    # 判断farmer和harvester是否需要处理
    farmer_reboot = crypto_item_conf.get("farmer_restart", False)
    farmer_email = crypto_item_conf.get("farmer_send_email", False)
    harvester_reboot = crypto_item_conf.get("harvester_restart", False)
    harvester_email = crypto_item_conf.get("harvester_send_email", False)

    executable_path = crypto_item_conf.get("executable_path", "")
    executable_name = crypto_item_conf.get("executable_name", "")
    executable_full_path = executable_path + executable_name

    global config_all
    config_all = config

    threads = []
    farmer_thread = threading.Thread(target=farmer_status, name=key+"-farmer", args=(device_id, key, executable_full_path, farmer_reboot, farmer_email,))
    threads.append(farmer_thread)

    harvester_thread = threading.Thread(target=harvester_status, name=key + "-harvester",
                          args=(device_id, key, crypto_item_conf, executable_full_path, harvester_reboot, harvester_email,))
    threads.append(harvester_thread)
    for t in threads:
        # 启动线程
        t.start()

    # # farmer status monitor
    # farmer_status(device_id, key, executable_full_path, farmer_reboot, farmer_email)
    #
    # # harvester status monitor
    # harvester_status(device_id, key, crypto_item_conf, executable_full_path, harvester_reboot, harvester_email)


# if __name__ == '__main__':
#     conf = Config(Path("/home/root/PycharmProjects/chiadoge/config_linux.yaml"))
#     crypto_conf = conf.get_crypto_config()
#     key = "chia"
#     crypto_item_conf = crypto_conf.get(key)
#     node_status_manager("test", key, crypto_item_conf, conf)
