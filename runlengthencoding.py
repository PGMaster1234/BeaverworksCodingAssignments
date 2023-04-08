def run_length_encoder(in_string):
    chars = []
    for char in in_string:
        chars.append(char)

    counter = 0
    current_char = chars[0]
    output = []
    for i, c in enumerate(chars):
        if counter < 2:
            output.append(c)
        print(c, current_char, counter)
        if c == current_char:
            counter += 1
        else:
            if counter >= 2:
                chars.insert(i, counter)
                output.append(counter)
            counter = 0
        current_char = c

    return output


def run_length_encoder2(in_string):
    output = []
    counter = 0
    prev_char = ""
    for i, char in enumerate(in_string):
        if in_string[i] == prev_char:
            counter += 1
        else:
            if in_string[i - 1] == " ":
                if counter >= 1:
                    output.append(counter + 1)
            else:
                if counter >= 1:
                    output.append(counter + 1)
            counter = 0
        if in_string[i] == " ":
            if counter < 2:
                output.append(in_string[i])
        else:
            if counter < 2:
                output.append(in_string[i])
        # print(char, prev_char, counter)
        prev_char = in_string[i]

    if counter >= 1:
        output.append(counter + 1)

    return output


# print(run_length_encoder2('Hello world'))
