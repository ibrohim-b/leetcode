class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import numpy as np
        import math
        def sub_lists(l):
            lists = [[]]
            for i in range(len(l) + 1):
                for j in range(i):
                    lists.append(l[j: i])
            return lists
        sub = sub_lists(nums)
        subc = sub.copy()
        sub = [x for x in subc if len(x) <= 2]
        sub.pop(0)
        print(sub)
        gcds = 0
        for i in sub:
            arr = np.array(i)
            result = np.gcd.reduce(arr)
            #print(i)
            if result == k:
                gcds += 1
                elif len(i) == 1 and i[0] == k:
                gcds += 1
            #print(gcds)
        return gcds



nums = [9,3,1,2,6,3]
k = 3
print(Solution().subarrayGCD(nums,k))