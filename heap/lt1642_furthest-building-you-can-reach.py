"""
for small height difference, we use bricks, while use ladder for large gaps

in this case, we treats all gaps as large ones at first, using ladder regardlessly
at some point, if we're running out of ladders, we'll replaces small gaps with bricks
this step is controlled by min-heap

Time complexity: O(nlogn)
Space complexity: O(n)

"""

import * from heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff = list()
        for idx in range(1, len(heights)):
            diff.append(heights[idx] - heights[idx - 1])
        if not diff:
            return 0
        l_remains = ladders
        b_remains = bricks
        ret = 0
        climb = list()	# the height that one climbs with ladder
        for d in diff:
            if d <= 0:
                ret += 1
                continue
            l_remains -= 1
            heappush(climb, d)
            if climb[0] > b_remains and l_remains < 0:
                return ret
            elif l_remains < 0:
                b_remains -= heappop(climb)
                l_remains += 1
            ret += 1
        return ret
