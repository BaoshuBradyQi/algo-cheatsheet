"""
using semaphore
using printnum as controller center, if condition satisfied, give access to other thread

"""
from threading import Semaphore
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.fizz_sema = Semaphore(0)
        self.buzz_sema = Semaphore(0)
        self.fizzbuzz_sema = Semaphore(0)
        self.num_sema = Semaphore(1)

        # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fizz_sema.acquire()

            if self.current > self.n:
                self.num_sema.release()
                break
            printFizz()
            self.current += 1
            self.num_sema.release()


    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.buzz_sema.acquire()

            if self.current > self.n:
                self.num_sema.release()
                break
            printBuzz()
            self.current += 1
            self.num_sema.release()


    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fizzbuzz_sema.acquire()

            if self.current > self.n:
                self.num_sema.release()
                break
            printFizzBuzz()
            self.current += 1
            self.num_sema.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.num_sema.acquire()

            if self.current > self.n:
                break
            if self.current % 5 ==0 and self.current % 3 == 0:
                self.fizzbuzz_sema.release()
            elif self.current % 5 == 0:
                self.buzz_sema.release()
            elif self.current % 3 == 0:
                self.fizz_sema.release()
            else:
                printNumber(self.current)
                self.current += 1
                self.num_sema.release()

        self.buzz_sema.release()
        self.fizz_sema.release()
        self.num_sema.release()
        self.fizzbuzz_sema.release()
