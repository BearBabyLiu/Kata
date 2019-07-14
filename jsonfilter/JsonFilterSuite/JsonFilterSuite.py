#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

import unittest
from JsonFilter import JsonFilter


class JsonFilterSuite(unittest.TestCase):

    def test_dict_is_meet_condition_expression_for_eq(self):
        dict_data = {"id": 123, "weight": 100, "parts": [{"id": 1,  "color": "red"}, {"id": 2, "color": "green"}]}
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('weight.eq=100,200'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('id.eq=123,100'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('weight.eq=100&id.eq=123'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('weight.eq=100&parts.id.eq=1&parts.color.eq=red'))
        self.assertFalse(JsonFilter(dict_data).is_meet_filter_expr('weight.eq=100&parts.id.eq=1&parts.color.eq=green'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('id.eq=123&parts.id.eq=2&parts.color.eq=green'))

    def test_dict_is_meet_condition_expression_for_neq(self):
        dict_data = {"id": 123, "weight": 100, "parts": [{"id": 1,  "color": "red"}, {"id": 2, "color": "green"}]}
        self.assertFalse(JsonFilter(dict_data).is_meet_filter_expr('weight.neq=100,123'))
        self.assertFalse(JsonFilter(dict_data).is_meet_filter_expr('id.neq=123'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('parts.id.neq=3&parts.color.neq=red'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('parts.id.neq=1'))

    def test_dict_is_meet_condition_expression_for_gt(self):
        dict_data = {"id": 123, "weight": 100, "parts": [{"id": 1,  "color": "red"}, {"id": 2, "color": "green"}]}
        self.assertFalse(JsonFilter(dict_data).is_meet_filter_expr('weight.gt=100'))
        self.assertFalse(JsonFilter(dict_data).is_meet_filter_expr('id.gt=123'))
        self.assertFalse(JsonFilter(dict_data).is_meet_filter_expr('parts.id.gt=1&weight.gt=100'))

    def test_dict_is_meet_one_condition_expression_for_gte(self):
        dict_data = {"id": 123, "weight": 100, "parts": [{"id": 1,  "color": "red"}, {"id": 2, "color": "green"}]}
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('weight.gte=100'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('id.gte=123'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('parts.id.gte=1&weight.gte=100'))

    def test_dict_is_meet_one_condition_expression_for_lt(self):
        dict_data = {"id": 123, "weight": 100, "parts": [{"id": 1,  "color": "red"}, {"id": 2, "color": "green"}]}
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('weight.lt=134'))
        self.assertFalse(JsonFilter(dict_data).is_meet_filter_expr('id.lt=101'))
        self.assertFalse(JsonFilter(dict_data).is_meet_filter_expr('parts.id.lt=1&weight.lt=200'))

    def test_dict_is_meet_one_condition_expression_for_lte(self):
        dict_data = {"id": 123, "weight": 100, "parts": [{"id": 1, "color": "red"}, {"id": 2, "color": "green"}]}
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('weight.lte=100'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('id.lte=123'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('parts.id.lte=1&weight.lte=100'))

    def test_dict_is_meet_one_condition_expression_for_cont(self):
        dict_data = {"id": 123, "weight": 100,
                     "parts": [{"id": 1, "color": ["red", "blue", "yellow"]}, {"id": 2, "color": "green"}]}
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('parts.color.cont=red'))
        self.assertTrue(JsonFilter(dict_data).is_meet_filter_expr('parts.color.cont=red,blue'))
