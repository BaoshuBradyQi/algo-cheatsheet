"""
greediness, assign whenever available

time complexity: O(m * n)
space complexity: O(1), no extras
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        ret = [ [0 for c in colSum] for r in rowSum]
        for r_idx in range(0, len(ret)):
            for c_idx in range(0, len(ret[r_idx])):
                r_remain = rowSum[r_idx]

                c_remain = colSum[c_idx]
                assign = min(r_remain, c_remain)
                ret[r_idx][c_idx] = assign
                rowSum[r_idx] -= assign
                colSum[c_idx] -= assign

        return ret
