def steps(x, y, dx, dy, count):
    if x > dx or y > dy:
        return -1
    if x == dx and y == dy:
        return count
    count += 1
    d1 = steps(x, x+y, dx, dy, count)
    d2 = steps(x+y, y, dx, dy, count)
    return max(d1, d2)
print(steps(1, 1, 2, 2, 0))