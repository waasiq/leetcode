class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()

        size = len(nums3)
        
        if (size % 2 == 0): return ((nums3[size// 2] + nums3[size//2 - 1])/2)
        else: return (nums3[size// 2])


def main():
    nums1 = [1,2]
    nums2 = [3,4]
    s1 = Solution()
    print(s1.findMedianSortedArrays(nums1, nums2))
    
    return

if __name__ == '__main__': 
    main()

