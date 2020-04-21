# -*- coding: utf-8 -*-

from src.model.member import Member as MemberModel


class MemberService:

    @staticmethod
    def get_list():
        return MemberModel().get_member_list()
