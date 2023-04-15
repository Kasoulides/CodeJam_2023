# read number of test cases
t = int(input())

# iterate over test cases
for i in range(1, t+1):
    # read input
    n = int(input())
    colors = list(map(int, input().split()))

    # initialize variables
    color_counts = {}
    next_integer = 1
    result = []
    impossible = False

    # iterate over colors
    for color in colors:
        # if color not seen before, assign next integer to it
        if color not in color_counts:
            color_counts[color] = next_integer
            next_integer += 1

        # append assigned integer to result
        result.append(color_counts[color])

    # check if integers are non-decreasing
    for j in range(1, n):
        if result[j] < result[j-1]:
            impossible = True
            break

    # output result
    if impossible:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        color_order = sorted(color_counts, key=color_counts.get)
        print("Case #{}: {}".format(i, " ".join(str(color) for color in color_order)))
