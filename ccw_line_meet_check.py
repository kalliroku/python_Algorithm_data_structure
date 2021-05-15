import sys
input = sys.stdin.readline


def find_d(x0, y0, x1, y1, x2, y2):
    return (x0*y1 + x1*y2 + x2*y0) - (x0*y2 + x2*y1 + x1*y0)


def is_meet(x1, y1, x2, y2, x3, y3):
    gx = max(x1, x2)
    gy = max(y1, y2)
    lx = min(x1, x2)
    ly = min(y1, y2)
    return lx <= x3 <= gx and ly <= y3 <= gy


def solution():
    res = 0
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    d1 = find_d(x1, y1, x2, y2, x3, y3)
    d2 = find_d(x1, y1, x2, y2, x4, y4)
    d3 = find_d(x3, y3, x4, y4, x1, y1)
    d4 = find_d(x3, y3, x4, y4, x2, y2)
    if not d1 and is_meet(x1, y1, x2, y2, x3, y3):
        return 1
    if not d2 and is_meet(x1, y1, x2, y2, x4, y4):
        return 1
    if not d3 and is_meet(x3, y3, x4, y4, x1, y1):
        return 1
    if not d4 and is_meet(x3, y3, x4, y4, x2, y2):
        return 1
    else:
        if d1 * d2 < 0 and d3 * d4 < 0:
            res = 1
    return res


print(solution())
