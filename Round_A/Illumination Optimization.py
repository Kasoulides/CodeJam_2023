# read number of test cases
t = int(input())

# iterate over test cases
for case in range(1, t+1):
    # read input values for this test case
    m, r, n = map(int, input().split())
    x = list(map(int, input().split()))

    # initialize variables
    i = 0  # leftmost streetlight without bulb
    count = 0  # number of bulbs needed
    j = -1  # rightmost bulb installed

    # iterate over streetlights
    while i < n:
        # find rightmost streetlight that can be illuminated by a new bulb
        while j + 1 < n and x[j+1] - x[i] <= r:
            j += 1

        # if no such streetlight exists, it is impossible to illuminate the entire freeway
        if j == i - 1:
            print("Case #{}: IMPOSSIBLE".format(case))
            break

        # install bulb at the rightmost streetlight found
        count += 1

        # find rightmost streetlight that can be illuminated by the new bulb
        k = j
        while k + 1 < n and x[k+1] - x[j] <= r:
            k += 1

        # check if we have covered the entire freeway
        if j == k and (x[i] - r <= 0 or x[j] + r >= m):
            print("Case #{}: {}".format(case, count))
            break

        # move to the next streetlight to be covered
        i = k + 1

        # check if we need to install another bulb to cover this next streetlight
        if i < n and x[i] - x[j] > r:
            count += 1
            j = k

        # if we don't need to install another bulb, we move the rightmost bulb to the end of the current range
        else:
            j = k

    # if we didn't break from the loop, it means we covered all streetlights and the entire freeway
    else:
        print("Case #{}: {}".format(case, count))
