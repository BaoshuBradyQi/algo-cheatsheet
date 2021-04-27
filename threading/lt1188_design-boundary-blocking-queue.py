"""
using one semaphore to control the length of queue
using another th control the access of the queue
"""
from collections import deque
from threading import Semaphore

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.store = deque()
        self.cap = Semaphore(capacity)
        self.block = Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.cap.acquire()
        self.store.append(element)
        self.block.release()

    def dequeue(self) -> int:
        self.block.acquire()
        t = self.store.popleft()
        self.cap.release()
        return t

    def size(self) -> int:
        return len(self.store)