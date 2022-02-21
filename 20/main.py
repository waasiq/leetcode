brackets = { '}' : '{', ']': '[', ')' : '('}

class Solution():
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        s = list(s)

        for bracket in s:
            if (bracket in brackets.values()):
                stack.append(bracket)
            else:
                if (len(stack) <= 0): return False
                top = stack.pop()
                if (brackets[bracket] != top): return False
        
        if (len(stack) != 0): return False 
        return True
        

def main():
    sol  = Solution()
    data = "("
    
    print(sol.isValid(data))    

if __name__ == '__main__':
    main()