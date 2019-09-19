import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

def DFS(r, c, cnt):
    global N
    map[r][c] = 0
    for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if 0<=r+y<N and 0<=c+x<N and map[r + y][c + x] == 1:
            cnt = DFS(r + y, c + x, cnt + 1)
    return cnt

map = [list(map(int, input())) for _ in range(N)]
res = []

for r in range(N):
    for c in range(N):
        if map[r][c] == 1:
            res.append(DFS(r, c, 1))

print(len(res))
for i in sorted(res):
    print(i)






