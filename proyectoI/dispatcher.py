from threading import Thread

class Dispatcher(Thread):
    def __init__(self, cores, ready_tree, mutex_rb, num_rb):
        super(Dispatcher, self).__init__()
        self.cores = cores
        self.ready_tree = ready_tree
        self.mutex_rb = mutex_rb
        self.num_rb = num_rb
 
 
    def run(self):
        while True:
        	if (self.num_rb.acquire() and self.mutex_rb.acquire()):
        		process = self.ready_tree.minimum()
        		self.ready_tree.minimum(process)
        	self.mutex_rb.release()
            self.num_rb.release()