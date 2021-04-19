"""
easy dp solution, if take first one into consideration, ignore last, vice versa
time complexity: O(n)
space complexity: O(n)
possible improvement, use constant extra space
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        ret1 = [0, nums[0]]
        for i in nums[1: -1]:
            ret1.append(max(i + ret1[-2],ret1[-1]))

        r1 = max(ret1)
        ret2 = [0, nums[1]]
        for i in nums[2:]:
            ret2.append(max(i + ret2[-2], ret2[-1]))
        r2 = max(ret2)
        return max(r1, r2)