from collections import Counter
from heapq import heappop, heappush
from typing import Iterable

CODES_SEPERATOR = "$$\n"


def buildTree(text: str):
    freq = sorted(Counter(text).items(), key=lambda pair: pair[1])
    heap = [[v, k, None, None] for k, v in freq]
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        heappush(heap, [left[0] + right[0], left[1] + right[1], left, right])
    return heappop(heap)


def buildCodes(tree, codes=None, pre="") -> dict[str, str]:
    if codes is None:
        codes = {}
    if not tree[2] and not tree[3]:
        tree.append(pre)
        codes[tree[1]] = pre
    if tree[2]:
        buildCodes(tree[2], codes, pre + "0")
    if tree[3]:
        buildCodes(tree[3], codes, pre + "1")
    return codes


def encodeText(text, codes) -> Iterable[bytes]:
    enc = "".join(map(codes.get, text))
    splitencoded = []
    for i in range(0, len(enc), 8):
        splitencoded.append(enc[i : i + 8])
    output = map(lambda n: int(n, 2).to_bytes(length=1, byteorder="big"), splitencoded)
    return output


def invertCodes(codes) -> str:
    return ",".join(f"{v}:{k}" for k, v in codes.items())


def compressText(data):
    codeTree = buildTree(data)
    codes = buildCodes(codeTree)
    encoded = encodeText(data, codes)
    return codes, encoded


def compressFile(path, output):
    with open(path, "r", encoding="utf-8") as file:
        fileContent = file.read()
        codes, encoded = compressText(fileContent)
        with open(output, "wb") as file:
            file.write(invertCodes(codes).encode())
            file.write(CODES_SEPERATOR.encode())
            for b in encoded:
                file.write(b)
        return codes, encoded
