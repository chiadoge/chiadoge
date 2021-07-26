#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import functools
from log import log
import requests
import json
from objdict import ObjDict


class HttpFunction:
    def __init__(self, config):
       self._monitor_server = config.get_monitor_server()

    # 判断当前机器码是否绑定了用户
    def had_bind_user(self, device_id):
        self_url = "/chia/open/api/selectUserByDeviceId/" + str(device_id)
        try:
            request_result = requests.get(self._monitor_server + self_url)
            content = request_result.content
            content_json = json.loads(content)
            return content_json
        except Exception as e:
            log.err_logger.logger.error("Cannot connect to the Server,Please check the internet and monitor server!")


    # 同步chia数据到server
    def sync_chia_information(self, information_all):
        self_url = "/chia/open/api/updateDeviceInfo"
        head = {
            'content-type': 'application/json'
        }
        try:
            request_result = requests.post(self._monitor_server + self_url, headers=head, data=json.dumps(information_all))
            content = request_result.content
            content_json = json.loads(content)
            code = int(content_json['data'])
            if code > 0:
                log.debug_logger.logger.info("sync information successfully:" + str(information_all))
            else:
                log.err_logger.logger.error("sync information error:" + str(information_all))
        except Exception as e:
            log.err_logger.logger.error("Cannot connect to the Server,Please check the internet and monitor server!" + str(e) + str(information_all))

    def get_node_properties(self, device_id):
        self_url = "/chia/open/api/getNodePropertiesByDeviceId/" + str(device_id)
        try:
            request_result = requests.get(self._monitor_server + self_url)
            content = request_result.content
            content_json = json.loads(content)
            return content_json['data']

        except Exception as e:
            log.err_logger.logger.error("Cannot connect to the Server,Please check the internet and monitor server!")
            return None

    def send_message_for_email(self, device_id, type, msg):
        self_url = "/chia/open/api/sendMessageForEmail"
        head = {
            'content-type': 'application/json'
        }
        try:
            data = ObjDict()
            data.deviceId = device_id
            data.type = type
            data.msg = "Device ID: " + device_id + " " + msg

            request_result = requests.post(self._monitor_server + self_url, headers=head, data=json.dumps(data))
            content = request_result.content
            content_json = json.loads(content)
            return content_json
        except Exception as e:
            log.err_logger.logger.error("Cannot connect to the Server,Please check the internet and monitor server!" + str(e) + str(data))