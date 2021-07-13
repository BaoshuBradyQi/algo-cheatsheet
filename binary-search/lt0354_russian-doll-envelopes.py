"""
longest increasing subsequence question, append the valid nums and replace existing nums with potential candidates

Time complexity: O(nlogn) for sorting, O(n log ret) for updating the subsequences
Space complexity: O(ret)
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key= lambda x: (x[0], - x[1]))

        doll = list()
        for _, l in envelopes:
            if not doll or doll[-1] < l:
                doll.append(l)
            else:
                left, right = 0, len(doll)
                while left < right:
                    mid = (left + right) // 2
                    if doll[mid] < l:
                        left = mid + 1
                    else:
                        right = mid
                doll[left] = l
        return len(doll)


