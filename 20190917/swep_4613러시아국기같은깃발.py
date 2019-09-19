import sys

sys.stdin = open('4613_input.txt', 'r')

def DFS(r):
    cnt = 0xffffff

    for w in range(N - 2):
        for r in range(w + 2, N):
            tmp = 0
            for i in range(N):
                if i <= w:
                    tmp += origin[i].count('R')
                    tmp += origin[i].count('B')
                elif i >= r:
                    tmp += origin[i].count('W')
                    tmp += origin[i].count('B')
                else:
                    tmp += origin[i].count('R')
                    tmp += origin[i].count('W')

            cnt = min(cnt,tmp)

    return cnt


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    origin = [input() for _ in range(N)]

    res = DFS(1)

    print('#{} {}'. format(tc, res))