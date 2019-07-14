#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

import logging.config
from Args.TypeArgs.Schema import Schema
from os import path
import os


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


if __name__ == '__main__':
    cmd_args = {'-b': '', '-p': '8080', '-s': '/usr/logs'}
    schema_args = '-b:bool:false,-p:int:0,-s:string:'
    ArgParser(cmd_args, schema_args).get_flag_value('-b')
    log_path = r'D:\code\Kata\refactoring_before\Args\log'
    if os.path.exists(log_path) is False:
        os.makedirs(r'D:\code\Kata\refactoring_before\Args\log')

    log_file_path = path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)), 'resource\\logging.conf')
    print(log_file_path)
    logging.config.fileConfig(log_file_path)
    nihao = logging.getLogger('nihao')
    logger = logging.getLogger('simpleExample')

    logger.info('debug message')
    nihao.info('nihao1')
    nihao.info('nihao2')
    nihao.info('nihao3')
