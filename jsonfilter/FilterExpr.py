#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

from EqExpr import EqExpr
from NeqExpr import NeqExpr
from GtExpr import GtExpr


class FilterExpr(object):

    type_factory = {
        '.eq=': lambda x: EqExpr(x.split('.eq=')[0], x.split('.eq=')[1]),
        '.neq=': lambda x: NeqExpr(x.split('.neq=')[0], x.split('.neq=')[1]),
        '.gt=': lambda x: GtExpr(x.split('.gt=')[0], x.split('.gt=')[1]),
    }

    def __init__(self, expr_str):
        self.expr_str = expr_str

    def _str_to_expr(self, expr):
        return [value for key, value in self.type_factory.items() if key in expr][0](expr)

    def extract_expr(self):
        expr = self.expr_str.split('&')
        return list(map(self._str_to_expr, expr))



