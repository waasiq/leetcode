class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i in range(len(nums)):
            number = nums[i]
            diff = target - number

            if (diff in map.keys()):
                return [map.get(diff), i]

            map[number] = i
            
        return []
           
def main():
    s = Solution()
    num = [2,7,11,15]
    print(s.twoSum(num,9))

if __name__ == '__main__':
    main()