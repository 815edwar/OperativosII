from threading import Thread

class ProcessMounter(Thread):
    def __init__(self, ready_tree, new_processes):
        super(ProcessMounter, self).__init__()
        self.ready_tree = ready_tree
        self.new_procesesses = new_processes

    def run(self):
        pass
