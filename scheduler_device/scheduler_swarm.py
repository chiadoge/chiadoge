#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import os
from config.config import Config
from log import log
from objdict import ObjDict
from pathlib import Path
from server_api.http_function import HttpFunction


def exec_cmd(cmd):
    r = os.popen(cmd, 'r')
    text = r.read()
    r.close()
    return text


# 屏蔽部分不需要的提示
def block_key(key):
    key_array = ["Note", ""]
    return key in key_array


# 获取数据
def get_chia_information(key, executable_full_path, crypto_item_conf):
    # 开始获取并组装数据
    information_array = []

    cmd_get_farm = executable_full_path + ''' farm summary'''
    get_farm = exec_cmd(cmd_get_farm)
    # 获取到的数据是文本，这里需要提取出来
    farm_message_array = get_farm.split("\n")
    # 提取处来的数据格式name:value，需要转换成json对象
    for farm_message_item_string in farm_message_array:
        if farm_message_item_string is not None and farm_message_item_string.count(":")>0:
            farm_message_item_array = farm_message_item_string.split(":")
            farm_message_item = ObjDict()
            farm_message_name = farm_message_item_array[0]
            if block_key(farm_message_name):
                continue
            farm_message_item.name = farm_message_name
            farm_message_item.value = farm_message_item_array[1]
            information_array.append(farm_message_item)

    # cmd_get_wallet_address = cmd_cd_chia_dir + '''chia.exe wallet get_address'''
    # get_wallet_address = exec_cmd(cmd_get_wallet_address)

    # 获取Crypto安装版本
    cmd_get_chia_version = executable_full_path + ''' version'''
    get_chia_version = exec_cmd(cmd_get_chia_version)
    chia_version_data = ObjDict()
    chia_version_data.name = 'version'
    chia_version_data.value = get_chia_version.split("\n")[0]

    information_array.append(chia_version_data)
    return information_array


# 获取最新一笔节点数据，
def device_message_manager(device_id, key, crypto_item_conf, config):
    log.debug_logger.logger.info("start sync: "+key)
    executable_path = crypto_item_conf.get("executable_path", "")
    executable_name = crypto_item_conf.get("executable_name", "")
    executable_full_path = executable_path + executable_name
    executable = Path(executable_full_path)

    # 判断可执行文件是否存在
    if not executable.is_file():
        log.err_logger.logger.error(key+" does not install.Please install First!")
        return

    # 通过device_id查找数据，是否存在绑定的数据
    result_data = HttpFunction(config).had_bind_user(device_id)
    if result_data is not None and 200 == result_data["code"]:
        # 如果存在绑定的用户数据，把当前机器上的数据通过api同步到该用户下
        information_all = ObjDict()
        information_all.type = key
        information_all.device_bind_id = result_data["device_bind_id"]
        information_all.information = get_chia_information(key, executable_full_path, crypto_item_conf)

        # 数据获取完毕，发送给api接口
        HttpFunction(config).sync_chia_information(information_all)

    else:
        log.debug_logger.logger.info(key + " Bind user Please！Device ID: "+device_id)
        # print("Bind user Please！Device ID:"+device_id)


# if __name__ == '__main__':
#     conf = Config(Path("/home/root/PycharmProjects/chiadoge/config_linux.yaml"))
#     crypto_conf = conf.get_crypto_config()
#     key = "chia"
#     crypto_item_conf = crypto_conf.get(key)
#     device_message_manager("test", key, crypto_item_conf, conf)
