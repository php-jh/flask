# coding=utf-8

from flask import Flask, url_for, redirect
from src.config.setting import Config


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(Config)
    # app.add_template_global(lang,'lang') // 添加模版全局变量

    # 钩子（中间件）
    # @app.before_request
    # def before_request():
    #     print(1)

    # 蓝图（模块）
    from src.module.bio import bp_bio
    app.register_blueprint(bp_bio, url_prefix="/bio")

    # index
    @app.route('/')
    def system_index():
        return redirect(url_for("bio.index_index"))

    return app
