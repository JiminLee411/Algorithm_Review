def perm(k, n, m):
    if k == m:
        print(' '.join(order))
        return
    for i in range(N):
        # if order and int(order[-1]) > i + 1: continue
        order.append(str(i+1))
        perm(k + 1, n, m)
        order.pop()

N, M = map(int, input().split())
order = []
perm(0, N, M)