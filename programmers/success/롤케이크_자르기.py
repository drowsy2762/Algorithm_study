from collections import Counter

def solution(topping):
    answer = 0
    right_dict = Counter(topping)
    left_set = set()
    for t in topping:
        left_set.add(t)
        right_dict[t] -= 1
        if right_dict[t] == 0:
            del right_dict[t]
            
        if len(left_set) == len(right_dict):
            answer += 1
            
    return answer
'''
경우의 수 문제
어떻게 topping 리스트를 짤라내야 똑같은 숫자의 토핑을 나눠 가질 수 있는지
방법 1) 리스트의 길이-1 만큼 새로운 리스트를 생성 후 그 부분에서 짜르면 좌우가 몇으로 나뉘는지 확인
방법 2) 하나 하나 잘라가면서 양옆 토핑을 확인

'''