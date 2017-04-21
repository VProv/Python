"""
Напишите декоратор proﬁler, который при вызове функции будет сохранять в
её атрибуты время ее исполнения и количество рекусивных вызовов произошедших
при исполнении. Атрибуты назовите last_time_taken и calls.
Пользоваться глобальными переменными запрещено.
"""

import functools
import sys
import time


def profiler(function):

    call_number = 0

    @functools.wraps(function)
    def decorator(*args, **kwargs):

        beginning_time = time.time()

        nonlocal call_number
        flag = False
        if call_number == 0:
            flag = True
        call_number += 1

        result = function(*args, **kwargs)

        if flag is True:
            decorator.calls = call_number
            decorator.last_time_taken = time.time() - beginning_time
            call_number = 0
        
        return result

    decorator.last_time_taken = 0
    decorator.calls = 0
    return decorator

exec(sys.stdin.read())
