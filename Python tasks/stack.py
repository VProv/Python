import sys


class Stack:
    def __init__(self, iter_obj):
        self.list = [x for x in iter_obj]

    def push(self, x):
        self.list.append(x)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1]

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return ' '.join([str(x) for x in self.list])

exec(sys.stdin.read())
