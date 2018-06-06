from threading import Thread 
from process import *
from random import randint
import time

class ProcessGenerator(Thread):

	def __init__(self, queue, mutex_np, num_np, gen_interval):
		super(ProcessGenerator, self).__init__()
		self.queue = queue
		self.mutex_np = mutex_np
		self.num_np = num_np
		self.gen_interval = gen_interval


	def run(self):
		while True:
			print("Running generator...")
			process = Process(randint(10,120))
			
			self.mutex_np.acquire()
			self.queue.enqueue(process)
			self.mutex_np.release()
			
			self.num_np.release()

			time.sleep(self.gen_interval)