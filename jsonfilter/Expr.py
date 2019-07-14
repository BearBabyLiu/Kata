#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'


class Expr(object):
    def __init__(self, key):
        self.key = key

    def get_pre_key(self):
        return '.'.join(self.key.split('.')[:-1])

    def get_last_key(self):
        return self.key.split('.')[-1]

    def is_meet_condition(self, data):
        pass
