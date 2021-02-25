def compress_str(txt):
    if not txt:
        return txt 

    res = {}
    
    for char in txt:
        tmp = 1
        if char in res:
            tmp = res[char] + 1

        res[char] = tmp

    txt = ''
    for key in res:
        txt = txt + str(res[key]) + key

    return txt