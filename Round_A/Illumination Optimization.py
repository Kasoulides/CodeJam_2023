def solve_case(m, r, x):
    n = len(x)
    i, j = 0, 0
    count = 0

    while i < n:
        j = i
        while j < n and x[j] - x[i] <= r:
            j += 1

        if j == i:
            return "IMPOSSIBLE"

        k = j - 1
        count += 1

        if k == n - 1:
            return count

        while k < n - 1 and x[k + 1] - x[j - 1] <= r:
            k += 1

        if k == n - 1 and x[k] + r >= m:
            return count

        if j == k + 1 and x[i] - r <= 0 and (k == n - 1 or x[k + 1] - x[k] > r) or x[k] + r >= m:
            return count

        i = k + 1

    return count


t = int(input())
for case in range(1, t + 1):
    m, r, n = map(int, input().split())
    x = list(map(int, input().split()))
    result = solve_case(m, r, x)
    print("Case #{}: {}".format(case, result))
