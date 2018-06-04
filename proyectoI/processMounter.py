from threading import Thread

class ProcessMounter(Thread):
    def __init__(self, ready_tree, mutex_rb, num_rb, new_processes, mutex_np, num_np, clock, can_run):
        super(ProcessMounter, self).__init__()
        self.ready_tree = ready_tree
        self.new_processes = new_processes
        self.mutex_np = mutex_np
        self.num_np = num_np
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb
        self.clock = clock
        self.can_run = can_run

    def run(self):
        while True:
            self.can_run['mounter'].acquire()
            if (self.num_np.acquire() and self.mutex_np.acquire()):
                self.can_run['mounter'].acquire()
                print("Running mounter")
                process = self.new_processes.dequeue()
                # print("Proceso desecolado por Mounter")
            self.mutex_np.release()

            if(self.mutex_rb.acquire()):
                self.ready_tree.add(process)
                # print("Proceso insertado en arbol por Mounter")
            self.mutex_rb.release()
            self.num_rb.release()

            self.clock.release()
            print("Ending mounter")
    