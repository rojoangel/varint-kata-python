def convertToBinaryRepr(inputInt):
	output = ""
	for exponent in [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
		currentPowerOf2 = 2**exponent
		currentBit = (int) (inputInt/currentPowerOf2)
		output += str(currentBit)
		inputInt = inputInt%currentPowerOf2
	return output

def swapTheTwoPartsOfTheRepr(inputStringBitRepr):
	part1 = inputStringBitRepr[0:7]
	part2 = inputStringBitRepr[7:14]
	return part2 + part1

#if __name__ == '__main__':
#	swapTheTwoPartsOfTheRepr("s0000m0x00000e")
