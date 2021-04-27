"""
using semaphore to control the other thread and using lock to control the counts
"""
from threading import Semaphore, Lock

class H2O:
    def __init__(self):
        self.oxy_sema = Semaphore(1)
        self.hydro_sema = Semaphore(0)
        self.h_count = 0
        self.count_lock = Lock()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        self.hydro_sema.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        with self.count_lock:
            self.h_count += 1
            if self.h_count == 2:
                self.h_count =0
                self.oxy_sema.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        self.oxy_sema.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.hydro_sema.release()
        self.hydro_sema.release()
