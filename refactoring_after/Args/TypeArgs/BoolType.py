#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

from TypeArgs.TypeArgs import TypeArgs


class BoolType(TypeArgs):

    def __init__(self, flag, default):
        self.flag = flag
        self.default = default

    def _is_type_value_correct(self, value):
        return True if value.lower() in ['true', 'false', ''] else False

    def get_flag(self):
        return self.flag

    def get_default(self):
        return True if self.default.lower() == 'true' else False

    def extract_value(self, value):
        if value is None:
            return self.get_default()
        if self._is_type_value_correct(value):
            return False if value.lower() == 'false' else True
        return "bool value type no match"
