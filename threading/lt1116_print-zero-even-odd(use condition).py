"""
condition is to check block a thread until it satisfies certain requirement
in this case we have to block odd and even until zero goes
and block zero after each iteration until one of odd or even goes
"""
from threading import Condition
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cv = Condition()
        self.current = 0
        self.pos = 0

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cv:
            while self.current < self.n:
                printNumber(0)
                self.current += 1
                if self.current % 2:
                    self.pos = 1
                else:
                    self.pos = 2
                self.cv.notify(2)
                self.cv.wait_for(lambda: self.pos == 0)


    def even(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cv:
            for i in range(0, self.n // 2):
                self.cv.wait_for(lambda: self.pos == 2)
                self.pos = 0
                printNumber(self.current)
                self.cv.notify(2)



    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cv:
            for i in range(0, self.n - self.n // 2):
                self.cv.wait_for(lambda: self.pos == 1)
                self.pos = 0
                printNumber(self.current)
                self.cv.notify(2)
