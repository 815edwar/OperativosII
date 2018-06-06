from threading import Thread
import time

class ProcessMounter(Thread):
    def __init__(self, ready_tree, mutex_rb, num_rb, new_processes, mutex_np, num_np, i_logic):
        super(ProcessMounter, self).__init__()
        self.i_logic = i_logic

        self.ready_tree = ready_tree
        self.new_processes = new_processes
        self.mutex_np = mutex_np
        self.num_np = num_np
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb


    def run(self):
        while self.i_logic['loop']:
            self.num_np.acquire()

            self.mutex_np.acquire()
            process = self.new_processes.dequeue()
            self.mutex_np.release()
            
            self.i_logic['screen'].acquire()
            self.i_logic['screen'].release()


            self.mutex_rb.acquire()
            self.ready_tree.add(process)
            self.mutex_rb.release()
            
            self.num_rb.release()
            
            self.i_logic['screen'].acquire()
            self.i_logic['screen'].release()

            time.sleep(1 * self.i_logic['speed'])
            time.sleep(1 * self.i_logic['speed'])