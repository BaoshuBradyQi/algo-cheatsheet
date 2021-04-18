from collections import Counter
import heapq
from queue import Queue as q

def leastInterval(tasks, n: int) -> int:

    t = list(map(lambda x: (- x[1], x[0]), Counter(tasks).items()))
    heapq.heapify(t)

    waitlist = q()
    waited_task = 0
    for i in range(0, n):
        waitlist.put("")
    ret = 0
    ret_str = ''
    while t or  waited_task:
        ret += 1
        if t:
            task = heapq.heappop(t)
            ret_str += task[1]

            if task[0] != -1:
                new_task = (task[0] + 1, task[1])
                waitlist.put(new_task)
                waited_task += 1
            else:
                waitlist.put("")
        else:
            ret_str += '?'
            waitlist.put("")

        waittask = waitlist.get()
        if waittask != "":
            waited_task -= 1
            heapq.heappush(t, waittask)
    print(ret_str)
    return ret
print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))