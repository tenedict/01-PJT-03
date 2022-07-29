# import sys

# sys.stdin = open("_소득불균형.txt")
n = int(input())
g = 0
for j in range(n):
    g += 1
    f = int(input())
    money = list(map(int,input().split()))
    average_ = sum(money)/len(money)
    co = 0
    for i in money:
        if i <= average_:
            co += 1
    print(f'#{g} {co}')