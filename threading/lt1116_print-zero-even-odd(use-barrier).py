"""
barrier is to control the number of threads that waits together at some point
in this case, zero/odd and zero/even bind together, however, zero always has to go first
thus a lock is needed to control the accessibility
"""
from threading import Barrier, Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.b1 = Barrier(2)
        self.b2 = Barrier(2)
        self.current = 0
        self.lock = Lock()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.current < self.n:
            self.lock.acquire()
            printNumber(0)

            self.current += 1

            if self.current % 2:
                self.b1.wait()

            else:
                self.b2.wait()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(0, self.n // 2):
            self.b2.wait()
            printNumber(self.current)
            self.lock.release()



    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(0, self.n - self.n // 2):
            self.b1.wait()
            printNumber(self.current)
            self.lock.release()