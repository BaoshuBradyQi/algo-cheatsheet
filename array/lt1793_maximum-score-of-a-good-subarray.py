"""
two pointers to track left and right, move pointers based on corresponding value

time complexity: O(n)
space complexity: O(1)
"""
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = k
        j = k
        range_min = nums[k]

        ret = range_min
        while i >= 0 and j < len(nums):
            if i == 0 and j == len(nums) - 1:
                break
            if i == 0 and j < len(nums) - 1:
                j += 1
                range_min = min(range_min, nums[j])
                ret = max(ret, range_min * (j - i + 1))
            elif j == len(nums) - 1 and i > 0:
                i -= 1
                range_min = min(range_min, nums[i])
                ret = max(ret, range_min * (j - i + 1))
            elif nums[i - 1] < nums[j + 1]:
                j += 1
                range_min = min(range_min, nums[j])
                ret = max(ret, range_min * (j - i + 1))
            elif nums[i - 1] >= nums[j + 1] :
                i -= 1
                range_min = min(range_min, nums[i])
                ret = max(ret, range_min * (j - i + 1))
        return ret