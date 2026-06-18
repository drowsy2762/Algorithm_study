class PriorityQueue:
    def __init__(self, N, K):
        self.heap = []
        self.capacity = N
        self.k = K

    def add(self, item):
        if len(self.heap) >= self.capacity:
            return

        self.heap.append(item)
        idx = len(self.heap) - 1

        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def removeMin(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()

        idx = 0
        size = len(self.heap)

        while 2 * idx + 1 < size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left

            if right < size and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[idx] > self.heap[smallest]:
                self.heap[idx], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[idx],
                )
                idx = smallest
            else:
                break

        return min_item

    def removeKthMin(self):
        if self.k <= 0 or self.k > len(self.heap):
            return None
        temp = []
        for _ in range(self.k):
            temp.append(self.removeMin())
        kth_min = temp[-1]
        for i in range(self.k - 1):
            self.add(temp[i])

        return kth_min


def main():
    queue = PriorityQueue(5, 2)
    queue.add(4)
    queue.add(5)
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print(queue.removeKthMin())  # 2
    for i in range(5):
        print(queue.removeMin(), end=" ")  # 1 3 4 5 None
    print()

    queue2 = PriorityQueue(5, 0)
    queue2.add(4)
    queue2.add(5)
    queue2.add(1)
    queue2.add(2)
    queue2.add(3)
    print(queue2.removeKthMin())  # None
    for i in range(5):
        print(queue2.removeMin(), end=" ")  # 1 2 3 4 5
    print()


if __name__ == "__main__":
    main()
