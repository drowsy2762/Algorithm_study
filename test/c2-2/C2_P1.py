class Heap:
    def __init__(self, n):
        self.heap = []
        self.max_size = n

    def insert(self, item):
        self.heap.append(item)
        self.upHeap(len(self.heap) - 1)

    def get_item(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        top_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.downHeap(0)
        return top_item

    def upHeap(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    def downHeap(self, index):
        size = len(self.heap)
        while 2 * index + 1 < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = left
            if right < size and self.heap[right] < self.heap[left]:
                smallest = right
            if self.heap[index] > self.heap[smallest]:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest
            else:
                break


class MedianHeap:
    def __init__(self, N):
        self.max_heap = Heap(N)
        self.min_heap = Heap(N)

    def insert(self, item):
        self.max_heap.insert(-item)
        if self.max_heap.heap and self.min_heap.heap:
            if (-self.max_heap.heap[0]) > self.min_heap.heap[0]:
                max_top = -self.max_heap.get_item()
                self.min_heap.insert(max_top)

        if len(self.max_heap.heap) > len(self.min_heap.heap) + 1:
            val = -self.max_heap.get_item()
            self.min_heap.insert(val)
        elif len(self.min_heap.heap) > len(self.max_heap.heap):
            val = self.min_heap.get_item()
            self.max_heap.insert(-val)

    def get_median(self):
        if not self.max_heap.heap:
            return None
        return -self.max_heap.heap[0]


def main():
    median_heap = MedianHeap(10)
    median_heap.insert(5)
    median_heap.insert(3)
    print(median_heap.get_median())  # 3
    median_heap.insert(8)
    median_heap.insert(1)
    median_heap.insert(4)
    print(median_heap.get_median())  # 4


if __name__ == "__main__":
    main()
