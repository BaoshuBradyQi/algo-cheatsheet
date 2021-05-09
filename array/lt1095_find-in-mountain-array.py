"""
find the peak in the array, then do binary search to each section
left-hand side is increasing array, right-hand side is decreasing

time complexity: O(logn)
space complexity: O(1)

"""
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length() - 1
        left, right = 0, length

        while left < right:
            idx = (left + right ) // 2
            if mountain_arr.get(idx) < mountain_arr.get(idx + 1):
                left = idx + 1
            else:
                right = idx
        peak = left


        l, p = 0, peak
        while l < p:
            if mountain_arr.get(p) == target:
                return p
            idx = (l + p) // 2
            mid = mountain_arr.get(idx)
            if mid == target:
                return idx
            elif mid < target:
                l = idx + 1
            else:
                p = idx

        l, p  = peak, length
        while l < p:
            if mountain_arr.get(p) == target:
                return p
            idx = (l + p) // 2
            mid = mountain_arr.get(idx)
            if mid == target:
                return idx

            elif mid > target:
                l = idx + 1
            else:
                p = idx
        return -1