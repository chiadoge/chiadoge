#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import os
import re
from datetime import datetime

from log import log


def harvester_info_match(debug_log_file):
    try:
        file_content = open(debug_log_file, 'r')
    except Exception as err:
        log.err_logger.logger.error("debug日志不存在，请确保打开INFO配置")
        return None

    # 记录最后一条匹配的数据
    last_matched_groups = None
    # 遍历所有行，取出最后一个符合正则表达式的行
    for file_line in file_content:
        linegroups = re.search(r"(.*) harvester .*(\d) plots .* farming (.*)\.\.\. Found (\d) proofs.*Time: (.*) s\. Total (.*) plots", file_line)
        if linegroups:
            last_matched_groups = linegroups

    return last_matched_groups

# print(harvester_info_match())