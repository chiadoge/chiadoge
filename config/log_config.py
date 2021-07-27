#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import os
from config.config import is_win_platform


path = ""
if is_win_platform():
    path = os.environ['USERPROFILE']+"\\chiadoge\\log\\"
else:
    path = os.environ['HOME']+"/chiadoge/log/"

all_path = path + "all.log"
err_path = path + "error.log"
