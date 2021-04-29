"""
maintaining a monotonous decreasing queue,
element in the of the index of queue head would be the maximum value of that window

space complexity: O(k), the length of queue
time complexity: O(n)
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ret = []
        for idx, n in enumerate(nums):
            if q and idx - q[0] >= k:
                q.popleft()

            while q and nums[q[-1]] < n:
                q.pop()
            q.append(idx)
            if idx + 1 >= k:
                ret.append(nums[q[0]])
        return ret