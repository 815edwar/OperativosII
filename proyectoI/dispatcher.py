from threading import Thread

class Dispatcher(Thread):
    def __init__(self, cores, ready_tree):
        super(Dispatcher, self).__init__()
        self.cores = cores
        self.ready_tree = ready_tree
 
 
    def run(self):
        pass