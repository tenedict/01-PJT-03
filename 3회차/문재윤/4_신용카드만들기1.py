# import sys

# sys.stdin = open("_신용카드만들기1.txt")
g = int(input())
for j in range(1,g+1):

    n = list(map(int,input().split()))


    c = 0
    sss = 0
    for i in n:
        c += 1
        if c%2 != 0:
            sss += i*2
        else:
            sss += i
    if sss%10 != 0:
        answer = 10 - (sss%10)
    else:
        answer = 0
    print(f'#{j} {answer}')
