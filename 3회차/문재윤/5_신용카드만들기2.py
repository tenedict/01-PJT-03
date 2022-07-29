# import sys

# sys.stdin = open("_신용카드만들기2.txt")

g = int(input())
for j in range(1,g+1):


    n = list(input())
    if len(n) == 19 or len(n) == 16:
        if n[0] == '3' or n[0] == '4' or n[0] == '5' or n[0] == '6' or n[0] == '9':
            print(f'#{j} 1')
        else:
            print(f'#{j} 0')
    else:
        print(f'#{j} 0')
