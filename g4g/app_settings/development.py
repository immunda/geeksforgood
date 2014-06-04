# -*- coding: utf-8 -*-
from g4g.app_settings.base import BaseConfig


class Config(BaseConfig):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
