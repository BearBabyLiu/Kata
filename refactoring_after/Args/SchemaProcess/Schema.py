#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

from TypeArgs.BoolType import BoolType
from TypeArgs.NullType import NullType
from TypeArgs.StringType import StringType
from TypeArgs.IntType import IntType


class Schema(object):

    type_factory = {
        'bool': lambda x, y: BoolType(x, y),
        'int': lambda x, y: IntType(x, y),
        'string': lambda x, y: StringType(x, y),
        'null': lambda x, y: NullType(x, y)
    }

    def __init__(self, schema_args):
        self.schemas = self._schema_parser(schema_args)

    def _args_to_schema(self, schema_arg):
        args = schema_arg.split(':')
        return self.type_factory.get(args[1], "null")(args[0], args[2])

    def _schema_parser(self, schema_args):
        schema_str = schema_args.split(',')
        return list(map(self._args_to_schema, schema_str))

    def extract_schema(self, flag):
        schema = list(filter(lambda x: x.get_flag() == flag, self.schemas))
        return schema[0] if schema else NullType(flag, '')







