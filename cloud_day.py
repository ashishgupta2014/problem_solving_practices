from collections import Counter


def getHouses(arr):
    for x, y in arr.items():
        yield (x, y, "H")


def getClouds(arr):
    t = 0
    for i in sorted(arr):
        t += arr[i]
        yield (i, t, "C")


def maximumPeople(p, x, y, r):
    a = Counter()
    b = Counter()
    c = Counter()
    for i, j in zip(p, x):
        a[j] += i
    for i, j in zip(y, r):
        b[i - j] += 1
        b[i + j + 1] -= 1
        c[i - j] = i + j + 1

    houses = getHouses(a)
    clouds = getClouds(b)

    cloudsAbove = 0
    currentCloud = -1
    sunnyCity = 0
    cloudyCity = Counter()
    for i, j, k in sorted(list(clouds) + list(houses)):
        if k == "C":
            cloudsAbove = j
            if currentCloud == -1 or (cloudsAbove == 1 and i >= c[currentCloud]):
                currentCloud = i
        elif cloudsAbove == 1:
            cloudyCity[currentCloud] += j
        elif cloudsAbove == 0:
            sunnyCity += j

    return sunnyCity + max(cloudyCity.values() or [0])

n = 2
p = [10, 100]
x = [5, 100]
m = 1
y = [4]
r = [1]
print(maximumPeople(p, x, y, r))