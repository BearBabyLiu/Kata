#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'
from itertools import groupby
from FilterExpr import FilterExpr


class JsonParser(object):

    def process_list(self, key, list_data):
        for value in list_data:
            if isinstance(value, dict):
                result = self.process_dict(key, value)
                if result is not None:
                    return result
            else:
                self.process_list(key, value)

    def __get_next_key(self, key):
        if '.' in key:
            return key.split('.')[0], '.'.join(key.split('.')[1:])
        else:
            return key, None

    def process_dict(self, key, dict_data):
        if key == "":
            return dict_data
        pre_key, next_key = self.__get_next_key(key)
        print('next_key:' + str(next_key))
        if pre_key in dict_data:
            value = dict_data[pre_key]
            if next_key is None:
                return value
            else:
                if isinstance(value, dict):
                    return self.process_dict(next_key, value)
                else:
                    return self.process_list(next_key, value)
        else:
            return None


if __name__ == '__main__':
    dic = {"id": 123, "weight": 100, "parts": [{"id1": 1,  "color": "red"}, {"id": 2, "color": "green"}]}
    data = 'parts.id&parts.color&id&weight'
    print('.'.join('weight'.split('.')[:-1]))
    a = [{k: list(g)} for k, g in groupby(data.split('&'), key=lambda x:'.'.join(x.split('.')[:-1]))]

    print(a)

    type_factory = {
        'eq=': lambda x: print(x),
    }
    data = 'nihao.eq=30'
    d_tmp = [value for key, value in type_factory.items() if key in data][0](data)
    print(d_tmp)
    dic = {"color": ["red", "blue", "yellow"]}
    a = True if "red,blue" in dic["color"] else False
    print(a)



