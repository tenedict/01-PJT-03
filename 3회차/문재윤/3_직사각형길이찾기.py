# import sys

# sys.stdin = open("_직사각형길이찾기.txt")
g = int(input())
for j in range(1,g+1):
    n = list(map(int,input().split()))
    nn = set(n)

    for i in nn:
        if n.count(i) == 1:
            print(f'#{j} {i}')
        elif n.count(i) == 3:
            print(f'#{j} {i}')
        else:
            continue
    