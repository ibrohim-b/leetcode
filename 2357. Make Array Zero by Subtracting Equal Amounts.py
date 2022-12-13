class Solution:
    def minimumOperations(self, nums):
        op = 0
        while nums != []:
            while 0 in nums:
                nums.remove(0)
            small = sorted(nums)[0]
            for i in range(len(nums)):
                nums[i] -= small
                op += 1
                print(nums,"||", small,"||",op)
print(Solution().minimumOperations([1,3,0,3,3]))