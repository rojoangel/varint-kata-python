import unittest

from varint import *

class VarintTest(unittest.TestCase):

	def test_convertToBinaryRepr_128(self):
		self.assertEqual("00000010000000", convertToBinaryRepr(128))

	def test_convertToBinaryRepr_129(self):
		self.assertEqual("00000010000001", convertToBinaryRepr(129))

	def test_swapTheTwoPartsOfTheRepr_128(self):
		self.assertEqual("00000000000001", swapTheTwoPartsOfTheRepr("00000010000000"))

	def test_swapTheTwoPartsOfTheRepr_129(self):
		self.assertEqual("00000010000001", swapTheTwoPartsOfTheRepr("00000010000001"))

	def test_addMostSignificantBit_128(self):
		self.assertEqual("1000000000000001", addMostSignificantBit("00000000000001"))

	def test_addMostSignificantBit_129(self):
		self.assertEqual("1000000100000001", addMostSignificantBit("00000010000001"))

if __name__ == '__main__':
	unittest.main(verbosity=2)
	print(testResult)