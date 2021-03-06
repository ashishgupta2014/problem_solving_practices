def solve(n, k):
    s = [1, 2, 2]
    i = 2
    while len(s) < n+1:
        x = s[i]+s[i-1]
        s.append(x)
        if len(s) < n+1:
            s.append(s[i])
        if len(s) < n+1:
            s.append(x)
        if len(s) < n+1:
            s.append(x)
        i += 2
    print(s)