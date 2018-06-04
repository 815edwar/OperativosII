from threading import Thread 
from process import *
from random import randint
import time

class ProcessGenerator(Thread):

	def __init__(self, queue, mutex_np, num_np, clock, generate, can_run):
		super(ProcessGenerator, self).__init__()
		self.queue = queue
		self.mutex_np = mutex_np
		self.num_np = num_np
		self.clock = clock
		self.generate = generate
		self.can_run = can_run


	def run(self):
		while True:
			self.can_run['generator'].acquire()
			if ( self.generate.acquire() ):
				print("Running generator...")
				process = Process(randint(10,120))
				# print("Proceso creado.")
				if (self.mutex_np.acquire()):
					self.queue.enqueue(process)
					# print("Proceso encolado.")
				self.mutex_np.release()
				self.num_np.release()

				self.clock.release()
				print("Ending generator...")
		