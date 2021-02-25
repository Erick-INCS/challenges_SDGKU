def compress_str(txt):
    if not txt:
        return txt

    result = ''
    last_char = txt[0]
    times = 1

    for current_char in txt[1:]:
        if current_char != last_char:
            result = result + str(times) + last_char
            last_char = current_char
            times = 1
        else:
            times = times + 1

    return result + str(times) + last_char
