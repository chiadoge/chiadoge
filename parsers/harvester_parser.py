#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
from datetime import datetime
from objdict import ObjDict
from parsers import match_logfile
from log import log


# 获取最新一笔数据，
def harvester_parser(device_id, crypto_item_conf, key, executable_full_path, harvester_reboot, harvester_email):
    # 开始读取日志时，记录时间
    start_match_time = datetime.now()

    # 开始遍历日志
    debug_log_file = crypto_item_conf.get("debug_log_file", "")
    last_matched_groups = match_logfile.harvester_info_match(debug_log_file)

    # 遍历结束时间
    end_match_time = datetime.now()

    # 遍历日志花费的时间
    match_time = (end_match_time - start_match_time).total_seconds()
    log.debug_logger.logger.info("日志处理所需时间：" + str(match_time))

    result_data = ObjDict()
    # 提取匹配到的字符串
    if last_matched_groups:
        # 最新的plot时间
        timestamp = datetime.strptime(last_matched_groups.group(1), "%Y-%m-%dT%H:%M:%S.%f")

        frequency_check_status = crypto_item_conf.get("frequency_check_status", 300)

        # 判断plottime是不是最近 frequency_check_status 秒内生成的
        # 遍历开始的时间减去plot的时间，表示plot后，等待定时任务启动所花费的时间
        # 减去定时任务的 frequency_check_status 秒，如果结果小于等于0，表示这个plot是在 frequency_check_status 秒内新产生的
        if ((start_match_time - timestamp).total_seconds() - frequency_check_status) <= 0:
            result_data.eligible_plots_count = int(last_matched_groups(2))
            result_data.challenge_hash = str(last_matched_groups.group(3))
            result_data.found_proofs_count = int(last_matched_groups.group(4))
            result_data.search_time_seconds = float(last_matched_groups.group(5))
            result_data.total_plots_count = int(last_matched_groups.group(6))
            result_data.code = True
        else:
            # 长时间内没有最新plot信息，说明harvester有问题，没正常工作
            msg = "Harvester长时间未plot，请检查!"
            result_data.code = False
            result_data.msg = msg
    else:
        # debug日志里没有plot信息，说明harvester有问题，没正常工作
        msg = "Harvester长时间未plot，请检查!"
        result_data.code = False
        result_data.msg = msg

    return result_data


# if __name__ == '__main__':
#     harvester_parser(debug_log_file="\\.chia\\mainnet\\log\\debug.log")
