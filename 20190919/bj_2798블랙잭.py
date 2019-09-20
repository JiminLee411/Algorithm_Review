RES = 0
def Find(k, tmp, n, m):
    global RES
    if k == 3:
        if RES < tmp:
            RES = tmp
        return
    for i in range(N):
        if visit[i] == 1 or tmp + cards[i] > m: continue
        visit[i] = 1
        order.append(cards[i])
        tmp += cards[i]
        Find(k + 1, tmp, n, m)
        visit[i] = 0
        order.pop()
        tmp -= cards[i]

N, M = map(int, input().split())
cards = list(map(int, input().split()))
visit = [0] * N
order = []
tmp = 0
Find(0, tmp, N, M)
print(RES)