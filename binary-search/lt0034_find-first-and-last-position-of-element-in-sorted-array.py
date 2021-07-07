"""
it's a good example to differentiate bisect_left/bisect_right

Time complexity: O(logn)
Space complexity: O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bi_right(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left
        def bi_left(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right ) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        l_idx = bi_left(nums, target)
        r_idx = bi_right(nums, target)
        if l_idx == r_idx:
            return [-1, -1]
        return [l_idx, r_idx - 1]
