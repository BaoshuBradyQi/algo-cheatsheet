"""
simply sort the meetings by starting and end time, then push to a heap
popout the already-end meetings when pushing to it
the maximum heap size would be the maximum rooms needed

Time complexity: O(nlogn), for sorting and the worst popout case
Space complexity: O(n)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        meetings = list()
        ret = 0
        intervals.sort(key= lambda x: (x[0], x[1]))
        for start, end in intervals:
            while meetings and meetings[0][0] <= start:
                heappop(meetings)
            heappush(meetings, (end, start))
            ret = max(ret, len(meetings))
        return ret
