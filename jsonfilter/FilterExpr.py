#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

from EqExpr import EqExpr
from NeqExpr import NeqExpr
from GtExpr import GtExpr
from GteExpr import GteExpr
from LteExpr import LteExpr
from LtExpr import LtExpr
from ContExpr import ContExpr


class FilterExpr(object):

    type_factory = {
        '.eq=': lambda x: EqExpr(x.split('.eq=')[0], x.split('.eq=')[1]),
        '.neq=': lambda x: NeqExpr(x.split('.neq=')[0], x.split('.neq=')[1]),
        '.gt=': lambda x: GtExpr(x.split('.gt=')[0], x.split('.gt=')[1]),
        '.gte=': lambda x: GteExpr(x.split('.gte=')[0], x.split('.gte=')[1]),
        '.lt=': lambda x: LtExpr(x.split('.lt=')[0], x.split('.lt=')[1]),
        '.lte=': lambda x: LteExpr(x.split('.lte=')[0], x.split('.lte=')[1]),
        '.cont=': lambda x: ContExpr(x.split('.cont=')[0], x.split('.cont=')[1]),
    }

    def __init__(self, expr_str):
        self.expr_str = expr_str

    def _str_to_expr(self, expr):
        return [value for key, value in self.type_factory.items() if key in expr][0](expr)

    def extract_expr(self):
        expr = self.expr_str.split('&')
        return list(map(self._str_to_expr, expr))



