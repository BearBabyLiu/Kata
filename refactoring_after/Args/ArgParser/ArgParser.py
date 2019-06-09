#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

from SchemaProcess.Schema import Schema


class ArgParser(object):

    def __init__(self, cmd_args, schema_args):
        self.cmd_args = cmd_args
        self.schema = Schema(schema_args)

    def get_flag_value(self, flag):
        return self.schema.extract_schema(flag).extract_value(self.cmd_args.get(flag))
