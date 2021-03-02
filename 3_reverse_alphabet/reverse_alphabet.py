def traspose(txt):
    if not txt or not isinstance(txt, str):
        return txt

    max_upper = ord('Z')
    min_upper = ord('A')
    max_lower = ord('z')
    min_lower = ord('a')

    txt = list(txt)
    for index, char in enumerate(txt):
        char_code = ord(char)

        if char_code >= min_upper and char_code <= max_upper:
            txt[index] = chr(max_upper - (char_code - min_upper))

        elif char_code >= min_lower and char_code <= max_lower:
            txt[index] = chr(max_lower - (char_code - min_lower))

    return ''.join(txt)


