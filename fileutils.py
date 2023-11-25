CODES_SEPERATOR = "$$"


def readText(filepath, enc="utf-8"):
    return open(filepath, "r", encoding=enc).read()


def writeEncode(encoded, filepath):
    file = open(filepath, "ab")
    file.write(encoded)
    file.close()


def writeByteArray(byteData, filepath):
    with open(filepath, "ab") as file:
        for data in byteData:
            file.write(data)


def writeAsText(obj, filepath):
    with open(filepath, "w") as file:
        file.write(str(obj))
