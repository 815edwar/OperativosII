from threading import Thread

class CPUWorker(Thread):
    def __init__(self, cpu, ready_tree, mutex_rb, num_rb, clock, can_run):
        super(CPUWorker, self).__init__()
        self.cpu = cpu
        self.ready_tree = ready_tree
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb
        self.remaining_time = cpu.quantum
        self.clock = clock
        self.can_run = can_run


    def run(self):
        while True:
            if self.cpu.free:
                self.cpu.pending_job.acquire()

            self.cpu.run_proccess()

            if not self.cpu.proccess.done():
                self.mutex_rb.acquire()
                self.ready_tree.add( self.cpu.proccess )
                self.mutex_rb.release()
                
                self.num_rb.release()

            self.cpu.free = True