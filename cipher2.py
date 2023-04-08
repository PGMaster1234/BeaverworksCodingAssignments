def encode_keyword(string, keyword):
    dic = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    dic2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    output = ""
    keyword_dic = []
    for char in keyword:
        if char != " ":
            if char not in keyword_dic:
                keyword_dic.append(char)
            if char in dic2:
                dic2.remove(char)
    for char in dic2:
        keyword_dic.append(char)

    for char in string:
        if char != " ":
            i = dic.index(char)
            output += keyword_dic[i]
        else:
            output += " "
    return output


print(encode_keyword("python rules", "beaverworks is cool"))
