class Solution:
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    def reverse(self, x):
        xStr= str(x)

        if (x < 0): 
            y = int('-' + xStr[1: len(xStr)][::-1])
            return 0 if (y <= -2147483647) else y
        else: return 0 if (int(xStr[::-1]) >= 2147483647) else int(xStr[::-1])
    

    
def main():
    s1 = Solution()
    strr = s1.reverse(-21483647)
    print(strr)

    #print(pow(2,31) -1)
    

    return

if __name__ == '__main__': 
    main()