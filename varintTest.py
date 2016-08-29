import unittest

from varint import *

class VarintTest(unittest.TestCase):

    def test_convertToBinaryRepr_128(self):
        self.assertEqual("00000010000000", convertToBinaryRepr(128))

    def test_convertToBinaryRepr_129(self):
        self.assertEqual("00000010000001", convertToBinaryRepr(129))

    def test_swapTheTwoPartsOfTheRepr_128(self):
		self.assertEqual("00000000000001", swapTheTwoPartsOfTheRepr("00000010000000"))

if __name__ == '__main__':
	unittest.main(verbosity=2)
	print(testResult)