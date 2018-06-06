from threading import Thread
import time

class Dispatcher(Thread):
    def __init__(self, cores, ready_tree, mutex_rb, num_rb, free_cpus, speed, screen):
        super(Dispatcher, self).__init__()
        self.SPEED = speed
        self.screen = screen

        self.cores = cores
        self.ready_tree = ready_tree
        self.free_cpus = free_cpus
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb

 
    def run(self):
        while True:
            self.num_rb.acquire()
            print("DISPATCHER DESPERTO")
            
            self.mutex_rb.acquire()
            node = self.ready_tree.minimum()
            self.ready_tree.delete(node)
            self.mutex_rb.release()

            self.screen.acquire()
            print("Proceso " + str(node.key.pid) + " sacado del arbol")
            self.screen.release()
            time.sleep(1 * self.SPEED)

            cpu_id = self.dispatch(node.key)
            
            self.screen.acquire()
            print("Proceso " + str(node.key.pid) + " insertado en cpu " + str(cpu_id))
            self.screen.release()
            time.sleep(1 * self.SPEED)


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