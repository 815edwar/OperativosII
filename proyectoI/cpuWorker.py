from threading import Thread
import time

class CPUWorker(Thread):
    def __init__(self, cpu, ready_tree, mutex_rb, num_rb, free_cpus, i_logic):
        super(CPUWorker, self).__init__()
        self.i_logic = i_logic

        self.cpu = cpu
        self.ready_tree = ready_tree
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb
        self.free_cpus = free_cpus


    def run(self):
        while self.i_logic['loop']:
            self.cpu.pending_job.acquire()

            self.run_process()

            if not self.cpu.process.done():
                self.cpu.process.last_core = self.cpu.pk
                self.mutex_rb.acquire()
                self.ready_tree.add( self.cpu.process, time.time() )
                self.mutex_rb.release()
                
                self.num_rb.release()

            self.cpu.process = None
            self.cpu.free = True
            self.free_cpus.release()


    def run_process(self):
        for i in range(self.cpu.quantum):
            self.cpu.process.min_t += 1
            
            self.i_logic['screen'].acquire()
            self.i_logic['screen'].release()
            
            time.sleep(1 * self.i_logic['speed'])

            if self.cpu.process.done():
                return