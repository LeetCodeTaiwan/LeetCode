class Solution(object):

    def __init__(self):
        self.table = [1]

    # def countDigitOneSlow(self, n):
    # 	counter = 0
    # 	for i in range(1, n+1):
    # 		numArray = str(i)
    # 		for j in range(len(numArray)):
    # 			if numArray[j] is '1':
    # 				counter += 1
    # 	return counter

    def createTable(self, n):
        for i in range(1, n + 1):
            self.table.append(10 * self.table[i - 1] + 10**i)

    def countDigitOne(self, n):
        if n < 0:
            return 0

        digitOfNumber = len(str(n))
        self.createTable(digitOfNumber - 2)

        return self.recursiveCountDigitOne(n, digitOfNumber)

    def recursiveCountDigitOne(self, n, digitOfNumber):
        firstDigit = int(str(n)[0]) if str(n) != '' else 0

        if digitOfNumber is 1:
            if n is 0:
                return 0
            else:
                return 1

        restDigit = int(str(n)[1:]) if str(n)[1:] != '' else 0

        digitOfRestDigit = len(str(restDigit))

        if firstDigit is 0:
            return self.recursiveCountDigitOne(restDigit, digitOfRestDigit)
        if firstDigit is 1:
            return self.table[digitOfNumber - 2] + 1 + restDigit + self.recursiveCountDigitOne(restDigit, digitOfRestDigit)

        return firstDigit * self.table[digitOfNumber - 2] + 10 ** (digitOfNumber - 1) + self.recursiveCountDigitOne(restDigit, digitOfRestDigit)
