from threading import Thread

class CPUWorker(Thread):
    def __init__(self, cpu, ready_tree):
        super(CPUWorker, self).__init__()
        self.cpu = cpu
        self.ready_tree = ready_tree

    def run(self):
        pass