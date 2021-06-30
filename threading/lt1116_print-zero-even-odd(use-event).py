"""
event is to give the permission to some threads
in this case zero gives signal to either odd or even and odd/even gives signal back to zero after each iteration
"""
from threading import Event
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.e0 = Event()
        self.e1 = Event()
        self.e2 = Event()
        self.current = 0
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(0, self.n):

            printNumber(0)
            self.current += 1
            if self.current % 2:
                self.e1.set()
            else:
                self.e2.set()
            self.e0.clear()
            self.e0.wait()


    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n //2):
            self.e2.wait()
            printNumber(self.current)
            self.e2.clear()
            self.e0.set()


    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(0, self.n - self.n//2):
            self.e1.wait()
            printNumber(self.current)
            self.e1.clear()
            self.e0.set()
