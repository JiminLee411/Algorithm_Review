import sys

sys.stdin = open('1210_input.txt', 'r')

def DFS(r, c):
    ladder[r][c] = 0

    if r == 0:
        return c
    if c - 1 >= 0 and ladder[r][c - 1]:
        return DFS(r, c - 1)
    elif c + 1 < 100 and ladder[r][c + 1]:
        return DFS(r, c + 1)
    else:
        return DFS(r - 1, c)

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    c = ladder[99].index(2)

    print('#{} {}'. format(tc, DFS(99, c)))