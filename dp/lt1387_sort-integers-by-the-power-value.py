"""
kind of simple dp solution, save every step and when input converge, just adjust the result

time complexity: O(m + n) + O(nlogn), for m is the largest path, n is the range, nlogn is for sorting
space complexity: O(m)

"""
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def even_power(x):
            return x//2
        def odd_power(x):
            return 3 * x + 1

        d = {1: 1, 2: 1}
        for i in range(lo, hi + 1):
            power_list = []
            power_list.append(i)
            while i != 1 and i not in d:
                if i % 2 == 0:
                    i = even_power(i)
                    power_list.append(i)
                else:
                    i = odd_power(i)
                    power_list.append(i)
            if i in d:
                for idx, t in enumerate(power_list[::-1]):
                    d[t] = d[i] + idx
            else:
                for idx, t in enumerate(power_list[::-1]):
                    d[t] = idx
        res = map(lambda x: (d[x], x), range(lo, hi + 1))
        return sorted(list(res))[k - 1][-1]