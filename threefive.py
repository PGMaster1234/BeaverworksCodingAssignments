def student_func(x):
    th, fi = False, False
    if x % 3 == 0:
        th = True
    if x % 5 == 0:
        fi = True

    if th and fi:
        return "threefive"
    if th:
        return "three"
    if fi:
        return "five"

    return x


print(student_func(150))
