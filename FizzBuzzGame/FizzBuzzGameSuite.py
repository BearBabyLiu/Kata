#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'

import unittest
from FizzBuzzGame import FizzBuzzGame


class FizzBuzzGameSuite(unittest.TestCase):
    def test_should_say_fizz_when_number_be_divided_by_3(self):
        self.assertEqual(FizzBuzzGame().say(3), "Fizz")
        self.assertEqual(FizzBuzzGame().say(9), "Fizz")

    def test_should_say_buzz_when_number_be_divided_by_5(self):
        self.assertEqual(FizzBuzzGame().say(5), "Buzz")
        self.assertEqual(FizzBuzzGame().say(25), "Buzz")

    def test_should_say_fizzbuzz_when_number_be_divided_5_and_3(self):
        self.assertEqual(FizzBuzzGame().say(15), "FizzBuzz")
        self.assertEqual(FizzBuzzGame().say(45), "FizzBuzz")

    def test_should_say_self_when_number_not_be_divided_by_5_or_3(self):
        self.assertEqual(FizzBuzzGame().say(7), "7")
        self.assertEqual(FizzBuzzGame().say(11), "11")

    def test_should_say_fizz_when_number_contain_3(self):
        self.assertEqual(FizzBuzzGame().say(13), "Fizz")
        self.assertEqual(FizzBuzzGame().say(23), "Fizz")

    def test_should_say_buzz_when_number_contain_5(self):
        self.assertEqual(FizzBuzzGame().say(52), "Buzz")
        self.assertEqual(FizzBuzzGame().say(56), "Buzz")

    def test_all(self):
        test_data = {13: "Fizz", 23: "Fizz", 52: "Buzz", 56: "Buzz"}
        for key in test_data:
            self.assertEqual(FizzBuzzGame().say(key), test_data.get(key))


if __name__ == '__main__':
    unittest.main()
