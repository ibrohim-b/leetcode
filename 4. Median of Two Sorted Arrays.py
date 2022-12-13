class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        if len(nums1) % 2 == 0:
            num1 = nums1[len(nums1) // 2 - 1]
            num2 = nums1[len(nums1) // 2]
            print(num1, num2)
            res = float(num1 + num2)
            return res / 2
        elif len(nums1) % 2 != 0:
            return nums1[len(nums1) // 2]
        else:
            return 0
nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1,nums2))
