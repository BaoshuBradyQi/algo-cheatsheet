"""
minimal window problem, generally speaking, the solution to this kind of problems has two rounds
first is to get a valid window from top to bottom, second is to improve it from bottom to up

Time complexity: for worst case could be O(m * n), m, n is len(s1), len(s2)
Space complexity: O(m)
"""
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        p1, p2 = 0, 0
        ret = s1
        valid = False
        def to_improve(idx):
            pr = -1
            while pr >= -len(s2):
                if s1[idx] == s2[pr]:
                    pr -= 1
                idx -= 1
            return idx + 1


        while p1 < len(s1):
            if s1[p1] == s2[p2]:
                p2 += 1
            p1 += 1
            if p2 == len(s2):
                # to improve
                valid = True
                new_p1 = to_improve(p1 - 1)
                if p1 - new_p1 < len(ret):
                    ret = s1[new_p1: p1]
                p1 = new_p1 + 1
                p2 = 0
        return ret if valid else ''
