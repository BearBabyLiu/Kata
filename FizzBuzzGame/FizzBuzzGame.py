#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Liu Huang'


class FizzBuzzGame(object):

    def is_match(self, num, mode):
        return True if num % mode == 0 or str(mode) in str(num) else False

    def is_fizz(self, num):
        return self.is_match(num, 3)

    def is_buzz(self, num):
        return self.is_match(num, 5)

    def is_fizzbuzz(self, num):
        return True if self.is_fizz(num) and self.is_buzz(num) else False

    def say(self, num):
        if self.is_fizzbuzz(num):
            return "FizzBuzz"
        if self.is_fizz(num):
            return "Fizz"
        if self.is_buzz(num):
            return "Buzz"
        return str(num)
