"""
using binary index tree, which is represented by a list
length of list should be O(n), or precisely n + 1 distinct number

Time complexity of update, O(log n)
Time complexity of counting, O(log n)

So the entire solution takes 2 steps:
first to sort the distinct number array and create a number-index mapping
then using a for loop starting from the end to do counting and updating

*** compare to segment tree, binary index tree only takes half space,
but with several restrictions as well
"""
class Solution(object):
    def countSmaller(self, nums: List[int]) -> List[int]:
        distinct_set = set(nums)
        distinct_list = sorted(list(distinct_set))
        idx_mapping = dict({n: idx for idx, n in enumerate(distinct_list)})
        bit = [0] * (len(distinct_list) + 1)

        def update(idx,  val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & -idx

        def count(left, right):
            l, r = 0, 0
            while left > 0:
                l += bit[left]
                left -= left & -left
            while right > 0:
                r += bit[right]
                right -= right &-right
            return r - l

        ret = list()
        for n in nums[:: -1]:
            ret.append(count(0, idx_mapping[n]))
            update(idx_mapping[n] + 1, 1)
        return ret[::-1]
