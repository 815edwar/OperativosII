from threading import Thread
from random import randint
import time

class Dispatcher(Thread):
    def __init__(self, val):
        super(Dispatcher, self).__init__()
        self.val = val
 
 
    def run(self):
        for i in range(1, self.val):
            print('Value %d in thread %s' % (i, self.getName()))
            
            # Sleep for random time between 1 ~ 3 second
            secondsToSleep = randint(1, 5)
            print('%s sleeping fo %d seconds...' % (self.getName(), secondsToSleep))
            time.sleep(secondsToSleep)

     
if __name__ == '__main__':
   # Declare objects of MyThread class
   DispatcherOb1 = Dispatcher(4)
   DispatcherOb1.setName('Thread 1')
 
   DispatcherOb2 = Dispatcher(4)
   DispatcherOb2.setName('Thread 2')
 
   # Start running the threads!
   DispatcherOb1.start()
   DispatcherOb2.start()
 
   # Wait for the threads to finish...
   DispatcherOb1.join()
   DispatcherOb2.join()
 
   print('Main Terminating...') 