import sys


def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    INF = int(1e8)
    costs = [INF] * (n+1)
    costs[1] = 0
    edgs = []
    for _ in range(n+1):
        edgs.append([])
    for _ in range(m):
        a, b, c = map(int, input().split())
        edgs[a].append([b, c])
    for i in range(n+1):
        for now in range(1, n+1):
            if costs[now] != INF:
                for dist, cost in edgs[now]:
                    total = costs[now] + cost
                    if costs[dist] > total:
                        costs[dist] = total
                        if i == n:
                            return [-1]
    return costs[2:]


for num in solution():
    if num != int(1e8):
        print(num)
    else:
        print(-1)
