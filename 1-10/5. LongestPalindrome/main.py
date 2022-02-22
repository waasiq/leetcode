from xml.dom.minidom import Element

class Solution:
    """
      :type s: str
      :rtype: str
    """
    def expandFromMiddle(self, s, left, right):
        if (left > right or s is None): return 0

        while (left >= 0 and right < len(s) and s[left] == s[right]):
            right += 1
            left -= 1        
        return (right - left - 1)
    

    def longestPalindrome(self, s):    
        if (s == '' or len(s) < 1): return ""
        
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandFromMiddle(s,i,i)
            len2 = self.expandFromMiddle(s, i, i+1)
            length = max(len1, len2)

            if (length > end - start):
                start = i - (length-1) //2
                end = i + length//2
        
        return s[start:end + 1]
        

def main():
    s1 = Solution()
    strr = s1.longestPalindrome('racecar')
    print('Output: ' + strr)

    return

if __name__ == '__main__': 
    main()