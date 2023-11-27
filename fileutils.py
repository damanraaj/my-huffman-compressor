CODES_SEPERATOR = "$$\n"


def readText(filepath, enc="utf-8"):
    return open(filepath, "r", encoding=enc).read()


def writeByteArray(byteData, filepath):
    with open(filepath, "ab") as file:
        file.write(byteData)


def writeAsText(obj, filepath):
    with open(filepath, "wb") as file:
        file.write(str(obj).encode())
