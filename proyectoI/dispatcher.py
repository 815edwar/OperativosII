from threading import Thread
import time

class Dispatcher(Thread):
    def __init__(self, cores, ready_tree, mutex_rb, num_rb, free_cpus, i_logic):
        super(Dispatcher, self).__init__()
        self.i_logic = i_logic

        self.cores = cores
        self.ready_tree = ready_tree
        self.free_cpus = free_cpus
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb

 
    def run(self):
        while self.i_logic['loop']:
            self.num_rb.acquire()

            self.mutex_rb.acquire()
            node = self.ready_tree.minimum()
            self.ready_tree.delete(node)
            self.mutex_rb.release()

            self.i_logic['screen'].acquire()
            self.i_logic['screen'].release()
            

            cpu_id = self.dispatch(node.key)
            
            self.i_logic['screen'].acquire()
            self.i_logic['screen'].release()

            time.sleep(1 * self.i_logic['speed'])
            time.sleep(1 * self.i_logic['speed'])


    def dispatch(self, process):
        assigned = False
        
        if process.last_core:
            cpu_id = process.last_core
        else:
            cpu_id = 0

        self.free_cpus.acquire()
        
        while not assigned:
            if self.cores[cpu_id].free:
                self.cores[cpu_id].rcv_process(process)
                self.cores[cpu_id].pending_job.release()
                assigned, self.cores[cpu_id].free = True, False
            else:
                cpu_id = (cpu_id + 1) % len(self.cores)

        return cpu_id