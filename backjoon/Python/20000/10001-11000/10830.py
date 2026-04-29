# https://www.acmicpc.net/problem/10830 : 행렬제곱 (python3)


# 제곱을 분할해서 하는 함수(제곱을 분할해 연산 과정을 줄임)
def divide(x, y):
    if y == 1:
        return x
    elif y % 2 == 0:
        temp = divide(x, y // 2)
        return matmul(temp, temp)
    else:
        temp = divide(x, y // 2)
        return matmul(matmul(temp, temp), x)


# 행열곱 함수 (x와 y 행렬을 곱함)
def matmul(x, y):
    size = len(x)
    r = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            e = 0
            for k in range(size):
                e += x[i][k] * y[k][j]
            r[i][j] = e % 1000

    return r


n, square = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# 행렬 제곱 연산
matrix = divide(matrix, square)

# 출력 (마지막에 1000으로 나머지를 구하는 이유는 1000이하의 자연수이기 때문)
for i in range(n):
    for j in range(n):
        print(matrix[i][j] % 1000, end=" ")
    print()
