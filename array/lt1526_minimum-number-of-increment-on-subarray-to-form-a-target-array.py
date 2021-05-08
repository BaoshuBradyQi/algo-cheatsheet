"""
record previous ones, if current is larger than previous, meaning subarray after this point have to increase separately
if smaller, meaning the end of certain subarray

time complexity: O(n)
space complexity: O(1)
"""
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        last = 0
        ret = 0
        for i in target:
            if i > last:
                ret += i - last
            last = i
        return ret