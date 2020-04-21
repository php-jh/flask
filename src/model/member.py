# -*- coding: utf-8 -*-
from src.model.base import Base


class Member(Base):

    def get_member_list(self):
        return self.db.table('common_member_center').first()

