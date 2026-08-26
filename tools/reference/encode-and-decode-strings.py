def codec(strs):
    return decode(encode(strs))


def encode(strs):
    return "".join("{}#{}".format(len(word), word) for word in strs)


def decode(data):
    out = []
    i = 0
    while i < len(data):
        j = data.index("#", i)
        length = int(data[i:j])
        out.append(data[j + 1:j + 1 + length])
        i = j + 1 + length
    return out
