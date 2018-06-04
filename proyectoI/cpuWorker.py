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
            self.can_run['cores'][self.cpu.pk].acquire()
            if (self.cpu.free):
                self.cpu.pending_job.acquire()
                # print("Running worker " + str(self.cpu.pk))

            self.cpu.run_proccess()
            self.remaining_time -= 1

            if (not self.cpu.proccess.done()):
                print("Running worker " + str(self.cpu.pk))
                if (self.remaining_time == 0):
                    if (self.mutex_rb.acquire()):
                        self.ready_tree.add( self.cpu.proccess )
                    self.mutex_rb.release()
                    self.num_rb.release()
                    self.cpu.free = True
            else:
                print("Running worker " + str(self.cpu.pk))
                self.cpu.free = True

            self.clock.release()
            print("Ending worker " + str(self.cpu.pk))