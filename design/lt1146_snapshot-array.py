"""
general thoughts:
maintain a snap id,
maintain a history dictionary, for each element
maintain an "object store"

for set
if there's no snap shot after last update, directly update the element
if there's snapshot, add a new one
time complexity: O(n)



for get
use binary search to get the closest snapshot
if there's no element ever, return 0
time complexity: O(logn)

overall space complexity: O(#saved instances)
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snapshot_dict = dict()
        self.history = defaultdict(lambda: [])

    def set(self, index: int, val: int) -> None:

        last_snapshot = -1 if not self.history[index] else self.history[index][-1]

        if self.snap_id > last_snapshot:

            self.history[index].append(self.snap_id )

            self.snapshot_dict[(index, self.snap_id)] = val

        else:
            self.snapshot_dict[(index, last_snapshot)] = val


    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:

        if not self.history[index]:
            return 0

        last = bisect_left(self.history[index], snap_id)

        if last < len(self.history[index]) and self.history[index][last] == snap_id:
            return self.snapshot_dict[(index, snap_id)]

        elif snap_id > self.history[index][-1]:
            return self.snapshot_dict[(index, self.history[index][-1])]

        elif snap_id < self.history[index][0]:
            return 0

        else:
            return self.snapshot_dict[(index, self.history[index][last -1])]
