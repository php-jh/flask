# coding=utf-8


class Config:
    # 密匙
    SECRET_KEY = '123'

    # 环境 development, production
    ENV = 'development'

    # 调试模式
    DEBUG = True

    # orator 数据库配置
    ORATOR_DATABASES = {
        'default': 'mysql',
        'mysql': {
            'driver': 'mysql',
            'host': '127.0.0.1',
            'database': 'member',
            'user': 'root',
            'password': '123123',
            'prefix': ''
        }
    }

    # 超级管理员
    SYS_SUPERS = [1]