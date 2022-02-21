class Solution:
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    def convert(self, s, numRows):
        if (numRows == 1): return s
        
        cycle = 2 * numRows - 2
        retStr = ''

        for i in range(numRows):        
            for j in range(i, len(s), cycle):
                retStr += s[j]
                if (i != numRows-1 and i != 0 and j + cycle-2 * i < len(s)):
                    retStr += s[j+cycle-2*i]             
        
        return  retStr
    

    
def main():
    s1 = Solution()
    strr = s1.convert('PAYPALISHIRING' , 3)
    print(strr)
    

    return

if __name__ == '__main__': 
    main()