"""
maintain a 'waitlist' for char that should be k distance apart
using heap to track put the most desired char first

time complexity: O(nlogn) for maintaining the heap
space complexity: O(n)

possible improvement: check if there's a valid return first
"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:

        from collections import Counter
        import heapq
        from queue import Queue as q

        t = list(map(lambda x: (- x[1], x[0]), Counter(s).items()))
        heapq.heapify(t)
        waitqueue = q()
        waited_c = 0

        for i in range(0, k - 1):
            waitqueue.put("")
        ret_str = ''

        while t or waited_c:

            if t:
                c = heapq.heappop(t)
                ret_str += c[1]

                if c[0] != -1:
                    new_c = (c[0] + 1, c[1])
                    waitqueue.put(new_c)
                    waited_c += 1
                else:
                    waitqueue.put("")

            else:
                return ""
                waitqueue.put("")

            waitc = waitqueue.get()

            if waitc != "":
                waited_c -= 1
                heapq.heappush(t, waitc)

        return ret_str