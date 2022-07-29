import sys

sys.stdin = open("_최빈수구하기.txt")
n = int(input())

for j in range(n):
    f = int(input())
    n = list(input().split())
    nn = set(n)
    a = 0
    answer1 = 0
    for i in nn:
        count_ = n.count(i)
        if int(count_) > a:
            a = count_
            answer = i
        elif int(count_) == a:
            if int(i) > int(answer):
                answer = i
        else:
            continue
        max(answer)
    print(f'#{f} {answer}')
    