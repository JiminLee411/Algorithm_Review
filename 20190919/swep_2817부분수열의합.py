import sys

sys.stdin = open('swep_2817_input.txt')

def sumNum(k, tmp, used):
    global cnt
    if tmp == K:
        cnt += 1
        return
    for i in range(k, N):
        if used & 1<<i:
            continue
        res.append(arr[i])
        sumNum(i+1, tmp + arr[i], used|1<<i)
        res.pop()

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    res = []
    cnt = 0
    sumNum(0, 0, 0)
    print('#{} {}'. format(tc, cnt))