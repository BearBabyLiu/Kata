#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'
from itertools import groupby
from JsonParser import JsonParser
from FilterExpr import FilterExpr


class JsonFilter(object):
    def __init__(self, dict_data):
        self.dict_data = dict_data

    def process_dict(self, dict_data, expr_inst_list):
        result = [False for value in expr_inst_list if value.is_meet_condition(dict_data) is False]
        return True if False not in result else False

    def process_list(self, list_data, expr_inst_list):
        for dict_data in list_data:
            if self.process_dict(dict_data, expr_inst_list):
                return True
        return False

    def is_meet_group_expr(self, group):
        for key in group:
            value = group[key]
            data = JsonParser().process_dict(key, self.dict_data)
            return self.process_dict(data, value) if isinstance(data, dict) else self.process_list(data, value)

    def is_meet_filter_expr(self, filter_expr):
        expr_inst = FilterExpr(filter_expr).extract_expr()
        groups = [{k: list(g)} for k, g in groupby(expr_inst, key=lambda x: x.get_pre_key())]
        return False if False in list(map(self.is_meet_group_expr, groups)) else True





