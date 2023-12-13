import unittest

from compress import compressFile
from decompress import decompress


class HuffmanTest(unittest.TestCase):
    def isSameContent(self, filename):
        compressed = filename + ".out"
        extracted = filename + "-extracted.out"
        compressFile(filename, compressed)
        decompress(compressed, extracted)
        with open(filename, encoding="utf-8") as f:
            with open(extracted, encoding="utf-8") as e:
                self.assertEqual(f.read(), e.read())

    def test_helloWorld(self):
        filename = "tests/hello"
        self.isSameContent(filename)

    def test_lorem_ipsum(self):
        self.isSameContent("tests/Lorem Ipsum.txt")

    def test_les_miserables(self):
        self.isSameContent("tests/Les Miserables.txt")


if __name__ == "__main__":
    unittest.main()
