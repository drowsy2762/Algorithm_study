class Sorter:
    def __init__(self, arr, N):
        self.array = arr
        self.size = N

    def printArray(self):
        for i in range(self.size):
            print(self.array[i], end=" ")
        print()

    def mergeSort_increase(self, l, r):
        # 원소가 1개 남을 때까지 반으로 계속 쪼개는 재귀 함수입니다.
        if l < r:
            m = (l + r) // 2  # 중간 지점 계산

            self.mergeSort_increase(l, m)  # 왼쪽 절반 정렬
            self.mergeSort_increase(m + 1, r)  # 오른쪽 절반 정렬
            self.merge_increase(l, m, r)  # 정렬된 두 절반을 하나로 병합

    def merge_increase(self, l, m, r):
        # 1. 원본 배열에서 병합할 두 구간을 임시로 복사합니다.
        L = self.array[l : m + 1]
        R = self.array[m + 1 : r + 1]

        i = 0  # 왼쪽 서브 배열(L)을 가리키는 인덱스
        j = 0  # 오른쪽 서브 배열(R)을 가리키는 인덱스
        k = l  # 원본 배열에 값이 채워질 위치를 가리키는 인덱스

        # 2. 두 서브 배열을 비교하며 작은 값부터 원본 배열에 채워 넣습니다 (오름차순)
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:  # 🌟 오름차순이므로 더 작은 값을 먼저 배치
                self.array[k] = L[i]
                i += 1
            else:
                self.array[k] = R[j]
                j += 1
            k += 1

        # 3. 한쪽 배열이 먼저 바닥나면, 남은 배열의 모든 원소를 뒤에 그대로 붙여줍니다.
        while i < len(L):
            self.array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            self.array[k] = R[j]
            j += 1
            k += 1

    def mergeSort_decrease(self, l, r):
        # 내림차순 분할 정렬 구조는 오름차순과 완벽히 동일합니다.
        if l < r:
            m = (l + r) // 2

            self.mergeSort_decrease(l, m)
            self.mergeSort_decrease(m + 1, r)
            self.merge_decrease(l, m, r)

    def merge_decrease(self, l, m, r):
        # 1. 원본 배열에서 병합할 두 구간을 임시로 복사합니다.
        L = self.array[l : m + 1]
        R = self.array[m + 1 : r + 1]

        i = 0
        j = 0
        k = l

        # 2. 두 서브 배열을 비교하며 큰 값부터 원본 배열에 채워 넣습니다 (내림차순)
        while i < len(L) and j < len(R):
            if (
                L[i] >= R[j]
            ):  # 🌟 내림차순이므로 더 큰 값을 먼저 배치 (부등호 방향 주목!)
                self.array[k] = L[i]
                i += 1
            else:
                self.array[k] = R[j]
                j += 1
            k += 1

        # 3. 남은 원소들 처리
        while i < len(L):
            self.array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            self.array[k] = R[j]
            j += 1
            k += 1


def main():
    N = 5
    arr = [12, 11, 13, 5, 6]
    sorter = Sorter(arr, N)
    sorter.printArray()  # 12 11 13 5 6
    sorter.mergeSort_increase(0, N - 1)
    sorter.printArray()  # 5 6 11 12 13
    sorter.mergeSort_decrease(0, N - 1)
    sorter.printArray()  # 13 12 11 6 5


if __name__ == "__main__":
    main()
