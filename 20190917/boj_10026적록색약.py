import sys
# sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
cnt = [0, 0]

def Find(i):
    for r in range(N):
        for c in range(N):
            if visit[r][c] == 0:
                DFS(r, c)
                cnt[i] += 1
def DFS(r,c):
    global stage
    visit[r][c] = 1
    for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if 0 <= r + y < N and 0 <= c + x < N and visit[r + y][c + x] == 0:
            if stage[r][c] == stage[r + y][c + x]:
                DFS(r + y, c + x)
            elif (stage[r][c] == 'R' and stage[r + y][c + x] == 'G') or (stage[r][c] == 'G' and stage[r + y][c + x] == 'R'):
                stage[r + y] = stage[r + y][:c + x] + stage[r][c] + stage[r + y][c + x + 1:]

N = int(input())
stage = [input() for _ in range(N)]
visit = [[0]*N for _ in range(N)]
Find(0)
visit = [[0]*N for _ in range(N)]
Find(1)
print('{} {}'. format(cnt[0], cnt[1]))