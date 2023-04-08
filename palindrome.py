def student_func(x):
    palindrome = 0
    letters = []
    x.replace(" ", "")
    for letter in x:
        if letter != " ":
            letters.append(letter)
    for i in range(len(letters)//2):
        if (letters[i]).lower() == (letters[-i-1]).lower():
            palindrome += 1
    return palindrome == len(letters)//2


print(student_func("rAce Car"))
