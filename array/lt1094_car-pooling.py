"""
sort with two keys
time complexity: O(nlogn)
space complexity: O(n)
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        load = list()
        for i in trips:
            load.append((i[1], i[0]))
            load.append((i[2], - i[0]))
        load.sort(key= lambda x: (x[0], x[1]))
        cap = 0
        for l in load:
            cap += l[1]
            if cap > capacity:
                return False
        return True