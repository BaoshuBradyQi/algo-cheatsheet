"""
maintain a heap for largest expectations if add one extra student, everytime satisfy that expectation

time complexity: O(nlogn + slogn), for n is number of classes and s is number of students
space complexity: O(n), for maintaining heap
"""
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq
        ratio = list()
        for g in classes:
            heapq.heappush(ratio, (-(( 1 + g[0])/(g[1] + 1) - g[0]/g[1]), g[0], g[1]))

        for s in range(extraStudents):
            c = heapq.heappop(ratio)
            heapq.heappush(ratio, (-((c[1] + 2 )/ (c[2] + 2) - (c[1] + 1)/(c[2] + 1)), c[1] + 1, c[2] + 1))

        ret = sum([x[1]/x[2] for x in ratio])/len(classes)
        return ret