from threading import Thread

class Dispatcher(Thread):
    def __init__(self, cores, ready_tree, mutex_rb, num_rb, free_cpus, clock, can_run):
        super(Dispatcher, self).__init__()
        self.cores = cores
        self.ready_tree = ready_tree
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb
        self.free_cpus = free_cpus
        self.clock = clock
        self.can_run = can_run
 
 
    def run(self):
        while True:
            self.can_run['dispatcher'].acquire()
            if (self.num_rb.acquire() and self.mutex_rb.acquire()):
                self.can_run['dispatcher'].acquire()
                print("Running dispatcher")
                process = self.ready_tree.minimum()
                self.ready_tree.delete(process)
            self.mutex_rb.release()
            self.dispatch(process.key)
            self.clock.release()
            print("Ending dispatcher")


    def dispatch(self, process):
        if process.last_core:
            cpu_id = process.last_core
        else:
            cpu_id = 0
        assigned = False

        if (self.free_cpus.acquire()):
            print("Despachando")
            while not assigned:
                print("Trato de asginar")
                if self.cores[cpu_id].free:
                    self.cores[cpu_id].rcv_proccess(process)
                    self.cores[cpu_id].pending_job.release()
                    assigned, self.cores[cpu_id].free = True, False
                else:
                    cpu_id = (cpu_id + 1) % len(self.cores)