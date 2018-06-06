from threading import Thread 
from process import *
from random import randint
import time

class ProcessGenerator(Thread):

	def __init__(self, queue, mutex_np, num_np, gen_interval, speed, screen):
		super(ProcessGenerator, self).__init__()
		self.SPEED = speed
		self.screen = screen

		self.queue = queue
		self.mutex_np = mutex_np
		self.num_np = num_np
		self.gen_interval = gen_interval


	def run(self):
		# while True:
		for _ in range(16):
			process = Process(128)
			self.mutex_np.acquire()
			self.queue.enqueue(process)
			self.mutex_np.release()
			
			self.num_np.release()

			self.screen.acquire()
			self.screen.release()

			time.sleep(self.gen_interval * self.SPEED)