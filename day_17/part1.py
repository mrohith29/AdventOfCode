# import collections as col

# def bfs(grid):
#     m, n, cost = len(grid), len(grid[0]), 0
#     queue = col.deque([(0, 0, 0)])  # (x, y, cost)
#     ansQueue = col.deque([(0, 0, 0)])
#     visited = set()
#     directions = [(0,1), (0,-1), (-1,0), (0,1)] # right, down, left, up

#     while queue:
#         # print(queue)
#         x, y, cost = queue.popleft()
#         x1, y1, finalcost = ansQueue[-1]
#         if (x, y) == (m-1, n-1):
#             print(finalcost)
#             return finalcost
#         for (a, b) in directions:
#             dx, dy = x + a, y + b
#             if 0<= dx < m and 0<=dy < n and (dx, dy) not in visited:
#                 visited.add((dx, dy))
#                 queue.append((dx, dy, cost + int(grid[dx][dy])))
#                 ansQueue.append((dx, dy, cost + int(grid[dx][dy])))
#     return -1



import heapq


def bfs(grid):
    path = heapq([(0, 0, 0)])  # (x, y, cost)
    x

with open('input.txt', 'r') as f:
    data = f.readlines()
    grid = [list(line.strip('\n')) for line in data]

print(bfs(grid))