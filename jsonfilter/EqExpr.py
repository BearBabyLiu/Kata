#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'
from Expr import Expr


class EqExpr(Expr):
    def __init__(self, key, value):
        super().__init__(key)
        self.value = value

    def is_meet_condition(self, data):
        key1 = self.get_last_key()
        return True if str(data.get(key1, None)) in self.value.split(',') else False
