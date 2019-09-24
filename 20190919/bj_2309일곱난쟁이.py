res = 0
def perm(i, num):
    global res
    visit[i] = 1

    if num == 7:
        for i in sorted(cnt):
            print(i)
        return 1

    for j in range(9):
        if res == 1: break
        if visit[j] or sum(cnt) + smallMen[j] > 100:
            continue
        cnt.append(smallMen[i])
        res = perm(j, num + 1)
        if res == 1: break
        cnt.pop()
        visit[j] = 0

smallMen = [ int(input()) for _ in range(9)]
visit = [0 for _ in range(9)]
cnt = []
perm(0, 0)
