from threading import Thread 
from process import *
from random import randint
import time

class ProcessGenerator(Thread):

	def __init__(self, queue, mutex_np, num_np, gen_interval, i_logic):
		super(ProcessGenerator, self).__init__()
		self.i_logic = i_logic

		self.queue = queue
		self.mutex_np = mutex_np
		self.num_np = num_np
		self.gen_interval = gen_interval


	def run(self):
		# for _ in range(16):
		while self.i_logic['loop']:
			process = Process(128)
			self.mutex_np.acquire()
			self.queue.enqueue(process)
			self.mutex_np.release()
			
			self.num_np.release()

			self.i_logic['screen'].acquire()
			self.i_logic['screen'].release()

			time.sleep(self.gen_interval * self.i_logic['speed'])