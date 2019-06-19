#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

import unittest
import logging

from Args.ArgParser.ArgParser import ArgParser


class TestArgsParser(unittest.TestCase):

    def test_bool_type(self):
        self.assertFalse(ArgParser({}, '-b:bool:false').get_flag_value('-b'))
        self.assertTrue(ArgParser({'-b': ''}, '-b:bool:false').get_flag_value('-b'))
        self.assertEqual(ArgParser({'-b': 'test'}, '-b:bool:false').get_flag_value('-b'), 'bool value type no match')

    def test_int_type(self):
        self.assertEqual(ArgParser({}, '-p:int:0').get_flag_value('-p'), 0)
        self.assertEqual(ArgParser({'-p': '8080'}, '-p:int:0').get_flag_value('-p'), 8080)
        self.assertEqual(ArgParser({'-p': 'test'}, '-p:int:0').get_flag_value('-p'), 'int value type no match')

    def test_string_type(self):
        self.assertEqual(ArgParser({}, '-s:string:').get_flag_value('-s'), '')
        self.assertEqual(ArgParser({'-s': '/usr/logs'}, '-s:string:').get_flag_value('-s'), '/usr/logs')

    def test_type_combination_with_no_cmd(self):
        self.assertFalse(ArgParser({}, '-b:bool:false,-p:int:0,-s:string:').get_flag_value('-b'))
        self.assertEqual(ArgParser({}, '-b:bool:false,-p:int:0,-s:string:').get_flag_value('-p'), 0)
        self.assertEqual(ArgParser({}, '-b:bool:false,-p:int:0,-s:string:').get_flag_value('-s'), '')

    def test_type_combination_with_cmd(self):
        cmd_args = {'-b': '', '-p': '8080', '-s': '/usr/logs'}
        schema_args = '-b:bool:false,-p:int:0,-s:string:'
        self.assertEqual(ArgParser(cmd_args, schema_args).get_flag_value('-b'), True)
        self.assertEqual(ArgParser(cmd_args, schema_args).get_flag_value('-p'), 8080)
        self.assertEqual(ArgParser(cmd_args, schema_args).get_flag_value('-s'), '/usr/logs')

    def test_no_exist_type(self):
        cmd_args = {'-c': '', '-p': '8080', '-s': '/usr/logs'}
        schema_args = '-b:bool:false,-p:int:0,-s:string:'
        self.assertEqual(ArgParser(cmd_args, schema_args).get_flag_value('-c'), '')


if __name__ == '__main__':
    logging.config.fileConfig('logging.conf')

    logger = logging.getLogger(__name__)
    unittest.main()
    print('test success')
    logger.debug('debug message')
