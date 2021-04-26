"""
simply sort the array
time complexity: O(nlogn)
space complexity: O(n)
"""
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)
        ret = 0
        for idx, c in enumerate(sorted_costs):
            if coins < ret + c:
                return idx
            ret += c
        return len(costs)