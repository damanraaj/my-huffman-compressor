from fileutils import CODES_SEPERATOR, writeAsText


def getCodeTrie(codes: str):
    mapping = {}
    isValue = False
    curr = mapping
    for c in codes:
        if isValue:
            curr["V"] = c
            isValue = False
            curr = mapping
        elif c.isdigit():
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        elif c == ":":
            isValue = True
    return mapping


def readEncodedFile(path):
    with open(path, "rb") as file:
        content = file.read()
        codes, encodedBytes = content.split(b"$$\n", 1)
        encoded = map(chr, encodedBytes)
        return codes.decode(), encoded


def decodeText(tree, encoded):
    out = ""
    curr = tree
    data = list(encoded)
    last = data.pop()
    data = [bin(ord(b))[2:].zfill(8) for b in data]
    if ord(last) != 0:
        data.append(bin(ord(last))[2:].zfill(8))
    for byte in data:
        for c in byte:
            if c in curr:
                curr = curr[c]
            if "V" in curr:
                out += curr["V"]
                curr = tree
    if ord(last) == 0:
        while "V" not in curr:
            curr = curr["0"]
        out += curr["V"]

    return out


def decompress(path):
    codes, encoded = readEncodedFile(path)
    mapping = getCodeTrie(codes)
    decoded = decodeText(mapping, encoded)
    writeAsText(decoded, path + "extracted")
    return codes, decoded
