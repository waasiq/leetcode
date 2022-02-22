class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend == 0 or divisor == 0): return 0
        if (dividend == -2147483648 and divisor== -1): return 2147483647
        ans, sign = 0, 1

        if (dividend < 0): dividend, sign = -dividend, -sign
        if (divisor < 0): divisor, sign = -divisor, -sign
        if (dividend == divisor): return sign
        
        while dividend >= divisor:
            step = 0
            while divisor << step <= dividend: step += 1
            dividend -= divisor << step - 1
            ans += 1 << step - 1

        return -ans if sign < 0 else ans

def main():
    s = Solution()
    print(s.divide(10,3))

if __name__ == '__main__':
    main()