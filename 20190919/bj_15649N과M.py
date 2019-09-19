

def perm():
    for i in range(N):
        if visit[i]: continue

        visit[i] = 1
        perm(i + 1, N)
        visit[i] = 0


N, M = map(int, input().split())
visit = [0]*N

