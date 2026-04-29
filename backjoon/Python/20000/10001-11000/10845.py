# 큐 : https://www.acmicpc.net/problem/10845 (python3)
import sys


class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, x):
        self.queue.append(x)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.queue.pop(0)

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if self.size == 0:
            return -1
        else:
            return self.queue[-1]


n = int(input())
queue = Queue()
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        queue.push(order[1])
    elif order[0] == "pop":
        print(queue.pop())
    elif order[0] == "size":
        print(queue.size)
    elif order[0] == "empty":
        print(queue.empty())
    elif order[0] == "front":
        print(queue.front())
    elif order[0] == "back":
        print(queue.back())
