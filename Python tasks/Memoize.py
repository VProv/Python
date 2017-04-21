"""
Вам предлагается написать декоратор memoize для функций,
который будет запоминать все результаты вычисления функции
для принимаемых аргументов, и в случае повторного вызова функции
с этими аргументами будет отдавать ранее вычисленный результат.
"""

import functools
import sys


def memoize(function):
    function.cache = dict()

    @functools.wraps(function)
    def decorated(*args, **kwargs):
        arguments = (args, tuple(kwargs.items()))
        if arguments in function.cache:
            return function.cache[arguments]
        else:
            function.cache[arguments] = function(*args, **kwargs)
            return function.cache[arguments]
    return decorated

exec(sys.stdin.read())
