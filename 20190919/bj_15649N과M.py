N, M = map(int,input().split())

order = []
used = [0] * N

def perm(k, n, m):
    if k == m:
        print(' '.join(order))
        return

    for i in range(n):
        if used[i]: continue
        used[i] = 1
        order.append(str(i+1))
        perm(k + 1, n, m)
        used[i] = 0
        order.pop()

perm(0, N, M)
