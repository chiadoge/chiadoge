# std
import argparse
from argparse import Namespace, ArgumentParser
from pathlib import Path
from typing import Tuple
import uuid

from config.config import Config
from log import log
from scheduler_device import add_scheduler_job


def parse_arguments() -> Tuple[ArgumentParser, Namespace]:
    parser = argparse.ArgumentParser(
        description="ChiaFarmWatch: Watch your crops " "with a piece in mind for the yield."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--config', type=str, help="path to config.yaml")
    return parser, parser.parse_args()


def init(config: Config):
    log.debug_logger.logger.info(f"Starting Chiadoge")

    # 生成设备ID
    device_id = uuid.uuid1()
    log.debug_logger.logger.info(f"Your Device ID: " + str(device_id))

    add_scheduler_job.add_job_scheduler(config, str(device_id))


if __name__ == "__main__":
    # Parse config and configure logger
    argparse, args = parse_arguments()

    if args.config:
        conf = Config(Path(args.config))
        init(conf)
