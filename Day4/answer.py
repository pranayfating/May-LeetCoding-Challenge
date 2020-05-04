class Solution:
    def findComplement(self, num: int) -> int:
        bin = "{0:b}".format(num)
        bin2 = ''
        for i in range(len(bin)):
            bin2 += str(1-int(bin[i]))
    
        return int(bin2, 2)
