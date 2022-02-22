class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 1): return 1

        subStr = ''
        maxSize = 0
        currSize = 0
        for i in range(len(s)):
            if ((s[i]  in subStr) == False):
                subStr += s[i]
                currSize = len(subStr)
                if (currSize > maxSize):
                    maxSize = currSize
            else:
                currSize = len(subStr)
                if (currSize > maxSize):
                    maxSize = currSize
                subStr = subStr[subStr.find(s[i])+1 : len(subStr)]
                subStr += s[i]
            
        return maxSize

def main():
    s1 = Solution()

    '''
    abcabcbb
    bbbbb
    pwwkew
    CODINGISAWESOME = NGISAWE
    always be coding
    '''
    
    val = s1.lengthOfLongestSubstring('CODINGISAWESOME')
    print('Val is: ' + str(val))
    return

if __name__ == '__main__': 
    main()

