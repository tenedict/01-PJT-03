# import sys

# sys.stdin = open("_문자열의거울상.txt")



f = int(input())
for j in range(1,f+1):
    n = input()
    n = n[::-1]
    a = ''
    for i in n:
        if i == 'q':
            a += 'p'
        elif i == 'p':
            a += 'q'
        elif i == 'b':
            a += 'd'
        elif i == 'd':
            a += 'b'
    print(f'#{j} {a}')