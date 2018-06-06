from threading import Thread
import time

class ProcessMounter(Thread):
    def __init__(self, ready_tree, mutex_rb, num_rb, new_processes, mutex_np, num_np, speed, screen):
        super(ProcessMounter, self).__init__()
        self.SPEED = speed
        self.screen = screen

        self.ready_tree = ready_tree
        self.new_processes = new_processes
        self.mutex_np = mutex_np
        self.num_np = num_np
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb


    def run(self):
        while True:
            self.num_np.acquire()

            self.mutex_np.acquire()
            process = self.new_processes.dequeue()
            self.mutex_np.release()
            
            self.screen.acquire()
            print("Proceso " + str(process.pid) + " desencolado")
            self.screen.release()
            time.sleep(1 * self.SPEED)

            self.mutex_rb.acquire()
            self.ready_tree.add(process)
            self.mutex_rb.release()
            
            self.num_rb.release()
            
            self.screen.acquire()
            print("Proceso " + str(process.pid) + " agregado al arbol")
            self.screen.release()
            time.sleep(1 * self.SPEED)