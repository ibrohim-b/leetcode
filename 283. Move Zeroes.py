class Solution(object):
    def moveZeroes(self, nums):
        """first_len = len(nums)
        while 0 in nums:
            nums.remove(0)
        for _ in range(first_len - len(nums)):
            nums.append(0)
        return nums"""
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums
nums = [0,0,1]
print(Solution().moveZeroes(nums))