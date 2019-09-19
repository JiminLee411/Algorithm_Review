import sys

sys.stdin = open('input.txt', 'r')

def DFS(v):
    visit[v] = 1
    cnt = 1
    for w in G[v]:
        if not visit[w]:
            cnt += DFS(w)
    return cnt

pcNum = int(input())
netNum = int(input())

G = [[] for _ in range(pcNum + 1)]
visit = [0 for _ in range(pcNum + 1)]

for _ in range(netNum):
    u, V = map(int, input().split())
    G[u].append(V)
    G[V].append(u)

res = DFS(1) - 1
print(res)