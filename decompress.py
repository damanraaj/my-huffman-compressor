from fileutils import CODES_SEPERATOR


def getCodeTrie(codes: str):
    mapping = {}
    v = False
    curr = mapping
    for c in codes:
        if v:
            curr["V"] = c
            v = False
            curr = mapping
        elif c.isdigit():
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        elif c == ":":
            v = True
    return mapping


def readEncodedFile(path):
    with open(path, "r") as file:
        content = file.read()
        codes, encodedBytes = content.split(CODES_SEPERATOR, 1)
        encoded = map(lambda n: bin(n)[2:], map(ord, encodedBytes))
        return codes, encoded


def decompress(path):
    codes, encoded = readEncodedFile(path)
    mapping = getCodeTrie(codes)
