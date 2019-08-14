n = 6
v = [4, 3, 1, 6, 2, 7]


def rec(i, j, t):
    if (t - i == t/2) or (t - j == 0):
        print(f"{i} {j}")
    if i > j:
        rec(i+1, j, t)
    rec(i, j+1, t)


rec(0, int(n/2), 6)

