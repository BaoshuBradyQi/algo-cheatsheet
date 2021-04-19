"""
easy dp solution, keep tracking the two smallest number of last round
time complexity: O(nk)
space complexity: O(k)

possible improvement: directly tracking the two smallest num instead of maintaining a list

"""

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])
        if k == 1:
            return costs[0][0]
        ret = [0] * k
        for c in costs:

            f_min = (ret[0], 0)
            s_min = (ret[1], 1)
            if f_min > s_min:
                f_min, s_min = s_min, f_min
            for idx in range(2, len(ret)):
                if ret[idx] <= f_min[0]:
                    f_min, s_min = (ret[idx], idx), f_min
                elif ret[idx] > f_min[0] and ret[idx] < s_min[0]:
                    s_min = (ret[idx], idx)
            new_ret = []
            for idx, color in enumerate(c):
                if idx == f_min[1]:
                    new_ret.append(color + s_min[0])
                else:
                    new_ret.append(color + f_min[0])
            ret = new_ret
        return min(ret)
