# -*- coding: utf-8 -*-
from flask import render_template
from src.service.member import MemberService

from src.module.bio import bp_bio


@bp_bio.route('/index', methods=['GET'])
def index_index():
    member_list = MemberService().get_list()
    print(member_list)
    return render_template('bio/index.html')
