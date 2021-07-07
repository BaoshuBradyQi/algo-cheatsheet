"""
classic binary search problem, looks tricky in the beginning but it follows the binary search pattern
given a boundary (left and right) and some criteria, probably there's binary search solution

Time complexity: O(log n) n is the range of boundary
Space complexity: O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eating_time(nums):
            ret = 0
            for p in piles:
                ret += p // nums
                if p % nums:
                    ret += 1
            return ret

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if eating_time(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left
