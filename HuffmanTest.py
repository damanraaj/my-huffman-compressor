import unittest

from compress import compressFile
from decompress import decompress


class HuffmanTest(unittest.TestCase):
    def test_helloWorld(self):
        compressFile("tests\\hello", "tests\\hello.out")
        decompress("tests\\hello.out")
        with open("tests\\hello") as f:
            with open("tests\\hello.out" + "extracted") as e:
                self.assertEqual(f.read(), e.read())

    def test_lorem_ipsum(self):
        compressFile("tests\\Lorem ipsum.txt", "tests\\Lorem ipsum.out")
        decompress("tests\\Lorem ipsum.out")
        with open("tests\\Lorem ipsum.txt") as f:
            with open("tests\\Lorem ipsum.out" + "extracted") as e:
                self.assertEqual(f.read(), e.read())

    def test_les_miserables(self):
        compressFile("tests\\Les Miserables.txt", "tests\\Les Miserables.out")
        decompress("tests\\Les Miserables.out")
        with open("tests\\Les Miserables.txt", encoding="utf-8") as f:
            with open("tests\\Les Miserables.out" + "extracted", encoding="utf-8") as e:
                self.assertEqual(f.read(), e.read())


if __name__ == "__main__":
    unittest.main()
