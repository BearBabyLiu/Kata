#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

from TypeArgs.Schema import Schema


class ArgParser(object):

    def __init__(self, cmd_args, schema_args):
        self.cmd_args = cmd_args
        self.schema_args = schema_args

    def _args_to_schema(self, schema_arg):
        args = schema_arg.split(':')
        return Schema(args[0], args[1], args[2])

    def extract_schema(self, flag):
        schema_strs = self.schema_args.split(',')
        schemas = list(map(self._args_to_schema, schema_strs))
        schema = list(filter(lambda x: x.get_flag() == flag, schemas))
        if schema:
            return schema[0]
        else:
            return Schema(flag, 'null', '')

    def get_flag_value(self, flag):
        if self.cmd_args.get(flag) is None:
            return self.extract_schema(flag).get_default()
        else:
            return self.extract_schema(flag).extract_value(self.cmd_args.get(flag))
