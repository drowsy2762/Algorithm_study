# 덱 : https://www.acmicpc.net/problem/10866 (python3)
import sys


class Deque:
    def __init__(self):
        self.deque = []
        self.size = 0

    def push_front(self, x):
        self.deque.insert(0, x)
        self.size += 1

    def push_back(self, x):
        self.deque.append(x)
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.deque.pop(0)

    def pop_back(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.deque.pop()

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.deque[0]

    def back(self):
        if self.size == 0:
            return -1
        else:
            return self.deque[-1]

    def size(self):
        return self.size


n = int(input())
deque = Deque()
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push_front":
        deque.push_front(order[1])
    elif order[0] == "push_back":
        deque.push_back(order[1])
    elif order[0] == "pop_front":
        print(deque.pop_front())
    elif order[0] == "pop_back":
        print(deque.pop_back())
    elif order[0] == "size":
        print(deque.size)
    elif order[0] == "empty":
        print(deque.empty())
    elif order[0] == "front":
        print(deque.front())
    elif order[0] == "back":
        print(deque.back())
