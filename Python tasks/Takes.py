"""
Напишите декоратор takes, который принимает список типов и проверяет аргументы
на соответствие этим типам. Если хотя бы один аргумент не соответствует
указанному типу, но необходимо бросить исключение TypeError.
"""

import functools
import sys


def takes(*arg_t, **kwargs_t):
    def outer_decor(function):
        @functools.wraps(function)
        def internal_decor(*args, **kwargs):
            for cur_type, arg in zip(arg_t, args):
                if not isinstance(arg, cur_type):
                    raise TypeError

            for arg_name, cur_type in kwargs.items():
                if not isinstance(cur_type, kwargs_t[arg_name]):
                    raise TypeError
            return function(*args, **kwargs)

        return internal_decor

    return outer_decor

exec(sys.stdin.read())
