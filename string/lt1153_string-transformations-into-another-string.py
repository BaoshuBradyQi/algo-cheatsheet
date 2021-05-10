"""
for str1, if the end-point(last transfer target) is different, then def a False
if str1 == str2, def True
if str2 has all 26 chars, which means there's no tmp solution for str1, def a False
otherwise True

time compplexity: O(n), loop through all chars
space complexity: O(1), a dictionary for 26 chars
"""
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        d = dict()
        if not str1:
            return False
        if str1 == str2:
            return True
        for idx in range(0, len(str1)):
            if str1[idx] not in d:
                d[str1[idx]] = str2[idx]
            else:
                if d[str1[idx]] != str2[idx]:
                    return False
        return len(set(d.values())) < 26