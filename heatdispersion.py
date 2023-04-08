import numpy as np


def evolve_heat_slow(u):
    output = np.copy(u)
    v = [False, False, False, False]  # Left, right, top, bottom
    left = 0
    right = 0
    bottom = 0
    top = 0
    for i, row in enumerate(u):
        for j, tile in enumerate(row):
            if j != len(row) - 1:
                right = u[i][j + 1]
                v[1] = True
            if j != 0:
                left = u[i][j - 1]
                v[0] = True
            if i != len(u) - 1:
                bottom = u[i + 1][j]
                v[3] = True
            if i != 0:
                top = u[i - 1][j]
                v[2] = True

            if v[3] and v[1]:
                output[i][j] = (bottom + right) / 2
            if v[3] and v[1] and v[0]:
                output[i][j] = (bottom + right + left) / 3
            if v[3] and v[0]:
                output[i][j] = (bottom + left) / 2

            if v[0] and v[2]:
                output[i][j] = (left + top) / 2
            if v[0] and v[2] and v[3]:
                output[i][j] = (left + bottom + top) / 3
            if v[0] and v[3]:
                output[i][j] = (left + bottom) / 2

            if v[1] and v[2]:
                output[i][j] = (right + top) / 2
            if v[1] and v[2] and v[3]:
                output[i][j] = (right + bottom + top) / 3
            if v[1] and v[3]:
                output[i][j] = (right + bottom) / 2

            if v[2] and v[1]:
                output[i][j] = (top + right) / 2
            if v[2] and v[1] and v[0]:
                output[i][j] = (top + right + left) / 3
            if v[2] and v[0]:
                output[i][j] = (top + left) / 2

            if v[0] and v[1] and v[2] and v[3]:
                output[i][j] = (top + right + left + bottom) / 4

            v = [False, False, False, False]

    return output


def evolve_heat_slow2(u):
    output = np.copy(u)
    directions = [None, None, None, None]
    for y, row in enumerate(u):
        for x, tile in enumerate(row):
            # print(u[y][x])
            if x != 0:
                directions[0] = u[y][x - 1]  # left
            if x != len(row) - 1:
                directions[1] = u[y][x + 1]  # right
            if y != 0:
                directions[2] = u[y - 1][x]  # top
            if y != len(u) - 1:
                directions[3] = u[y + 1][x]  # bottom

            count = 0
            total = 0
            for i in directions:
                if i is not None:
                    total += i
                    count += 1

            if x != 0:
                if x != len(row) - 1:
                    if y != len(u) - 1:
                        if y != 0:
                            output[y][x] = total / count
            directions = [None, None, None, None]

    return output


ar = np.array([1, 7, 2, 1, 1, 1, 3, 1, 2, 3, 7, 1, 2, 0, 0, 0, 0, 0, 0, 0], dtype=float).reshape(4, 5)
print(ar)
print("\n")
print(evolve_heat_slow2(ar))
