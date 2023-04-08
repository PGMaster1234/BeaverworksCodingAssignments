def run_length_decoder(in_list):
    output = []
    for c, char in enumerate(in_list):
        if type(char) == str:
            output.append(char)
        else:
            for i in range(char - 2):
                output.append(in_list[c - 1])

    outputStr = ""
    for letter in output:
        outputStr += letter

    return outputStr


# print(run_length_decoder(['H', 'e', 'l', 'l', 3, 'o', ' ', 'w', 'o', 'r', 'l', 'd']))
