from fileutils import CODES_SEPERATOR


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
    with open(path, "r") as file:
        content = file.read()
        codes, encodedBytes = content.split(CODES_SEPERATOR, 1)
        encoded = map(lambda n: bin(n)[2:], map(ord, encodedBytes))
        return codes, encoded


def decodeText(tree, encoded):
    out = ""
    curr = tree
    for byte in encoded:
        for c in byte:
            if "V" in curr:
                out += curr["V"]
                curr = tree
            if c in curr:
                curr = curr[c]
    if "V" in curr:
        out += curr["V"]
    return out


def decompress(path):
    codes, encoded = readEncodedFile(path)
    mapping = getCodeTrie(codes)
    decoded = decodeText(mapping, encoded)
