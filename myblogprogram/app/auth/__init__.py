#!usr/bin/env python
#coding=utf-8
"""
author:wubaichuan

"""

from flask import Blueprint


auth = Blueprint('auth',__name__)

from . import views