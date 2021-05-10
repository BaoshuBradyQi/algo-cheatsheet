"""
use intervals as key, returns will be the values of that dictionary

time complexity: O(n), n is total length of strings
space complexity: O(n)
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def char_to_idx(char):
            return ord(char) - 97

        def convert_to_interval(string):
            ret = []
            if len(string) == 1:
                return tuple()
            last = char_to_idx(string[0])
            for i in range(1, len(string)):
                inter = char_to_idx(string[i]) - last
                if inter < 0:
                    inter += 26
                last = char_to_idx(string[i])
                ret.append(inter)
            return tuple(ret)

        d = dict()
        for s in strings:
            k = convert_to_interval(s)
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
        return d.values()