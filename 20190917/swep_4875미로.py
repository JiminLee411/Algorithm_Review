# import sys
# sys.stdin = open('input.txt', 'r')

# def DFS(r, c, n):
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     visit[r][c] = True
#     for i in range(4):
#         if (r == N - 1 and i == 3) or (r == 0 and i == 1) or (c == N - 1 and i == 2) or (c == 0 and i == 0):
#             continue
#         elif maze[r + dy[i]][c + dx[i]] == '3':
#             return 1
#         elif (visit[r + dy[i]][c + dx[i]] == False) and maze[r + dy[i]][c + dx[i]] == '0':
#             if DFS(r + dy[i], c + dx[i], n) == 1:
#                 return 1
#     return 0

# for t in range(1, int(input()) + 1):
#     res = 0
#     N = int(input())
#     maze = [input() for _ in range(N)]
#     visit = [[False] * N for _ in range(N)]
#     for i in range(N):
#         if '2' in maze[i]:
#             column = maze[i].find('2')
#             row = i
#             break
#     res = DFS(row, column, N)
#     print('#{} {}'. format(t, res))

for i in range(1, -1):
    print(i)
print(3)