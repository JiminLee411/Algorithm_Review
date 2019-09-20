
def perm(k, n, m):
    if k == m:
        print(' '.join(order))
        return
    for i in range(N):
        if visit[i] or (order and int(order[-1]) >= i + 1): continue
        visit[i] = 1
        order.append(str(i+1))
        perm(k + 1, n, m)
        visit[i] = 0
        order.pop()


N, M = map(int, input().split())
visit = [0] * N
order = []
perm(0, N, M)