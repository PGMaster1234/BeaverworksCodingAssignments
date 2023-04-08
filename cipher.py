def encode_caesar(string, shift_amt):
    output = ""
    temp_shift = 0
    dic = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i, char in enumerate(string):
        if i + shift_amt > 26:
            temp_shift = i + shift_amt - 26
            output += str(dic[temp_shift])
        else:
            output += str(dic[i + shift_amt])
    return output


print(encode_caesar("abc", 2))
