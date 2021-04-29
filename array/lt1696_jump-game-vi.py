"""
maintain a monotonous decreasing queue
for certain index, maximum value would be itself + the maximum value of the index of the head of queue
condition for popleft is the index out of k boundary,
condition for pop right is the new maximum value larger than the last one in queue

time complexity: O(n), since loop through the given list and all element is pushed/poped once
space complexity: O(n), for maintaining dp list
"""
from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        ret = [0] * len(nums)
        ret[0] = nums[0]
        q = deque()
        q.append(0)
        for idx, n in enumerate(nums[1:]):

            if q and q[0] < idx - k + 1:
                q.popleft()
            ret[idx + 1] = ret[q[0]] + n

            while q and ret[q[-1]] <= ret[idx + 1]:
                q.pop()
            q.append(idx + 1)
        return ret[-1]