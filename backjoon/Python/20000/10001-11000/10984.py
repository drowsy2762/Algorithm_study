T = int(input())
for t in range(T):
    N = int(input())
    get_sum = 0.0
    C_sum = 0
    for n in range(N):
        C, G = map(float, input().split())
        get_sum += C * G
        C_sum += C
    GPA = get_sum / C_sum
    print("%s %.1f" % (int(C_sum), GPA))