#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

from TypeArgs.TypeArgs import TypeArgs


class StringType(TypeArgs):

    def __init__(self, flag, default):
        self.flag = flag
        self.default = default

    def _is_type_value_correct(self, value):
        return True

    def get_flag(self):
        return self.flag

    def get_default(self):
        return self.default

    def extract_value(self, value):
        if value is None:
            return self.get_default()
        return value
