#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

from TypeArgs.TypeArgs import TypeArgs


class IntType(TypeArgs):

    def __init__(self, flag, default):
        self.flag = flag
        self.default = default

    def _is_type_value_correct(self, value):
        return True if value.isdigit() else False

    def get_flag(self):
        return self.flag

    def get_default(self):
        return int(self.default)

    def extract_value(self, value):
        if value is None:
            return self.get_default()
        if self._is_type_value_correct(value):
            return int(value)
        return "int value type no match"
