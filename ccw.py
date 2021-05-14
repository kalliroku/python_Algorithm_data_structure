import sys
input = sys.stdin.readline

n = int(input())
x0, y0 = map(int, input().split())
xs = []
ys = []
for _ in range(n-1):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

res = 0

for i in range(n-2):
    x1 = xs[i]
    x2 = xs[i+1]
    y1 = ys[i]
    y2 = ys[i+1]
    res += ((x0*y1 + x1*y2 + x2*y0) - (x0*y2 + x2*y1 + x1*y0)) / 2

print(abs(res))
