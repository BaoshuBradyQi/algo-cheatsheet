"""
use semaphore to signal the other thread
"""
from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sema = Semaphore(1)
        self.bar_sema = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.foo_sema.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_sema.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.bar_sema.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_sema.release()