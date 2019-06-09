#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'


class Schema(object):

    def __init__(self, flag, flag_type, default):
        self.flag = flag
        self.flag_type = flag_type
        self.default = default

    def _check_type_value(self, value):
        if self.flag_type == 'bool':
            if value.lower() != 'true' and value.lower() != 'false' and value != '':
                return False
            else:
                return True
        elif self.flag_type == 'int':
            if value.isdigit():
                return True
            else:
                return False
        elif self.flag_type == 'string':
            return True

    def get_flag(self):
        return self.flag

    def get_default(self):
        if self.flag_type == 'bool':
            return True if self.default.lower() == 'true' else False
        elif self.flag_type == 'int':
            return int(self.default)
        elif self.flag_type == 'string':
            return self.default
        else:
            return ''

    def get_type(self):
        return self.flag_type

    def extract_value(self, value):
        if self.flag_type == 'bool':
            if self._check_type_value(value):
                return False if value.lower() == 'false' else True
            else:
                return "bool value type no match"
        elif self.flag_type == 'int':
            if self._check_type_value(value):
                return int(value)
            else:
                return "int value type no match"
        elif self.flag_type == 'string':
            return value
        else:
            return ''
