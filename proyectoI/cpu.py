from process import *


class CPU:
	
	def __init__(self, pk, quantum = 4):
		self.pk = pk
		self.quantum = quantum
		self.process = None

	def clock(self):
		tmp = self.process.min_t + self.quantum
		if self.process.required_t < tmp:
			self.process.min_t = self.process.required_t
		else:
			self.process.min_t = tmp


	def free(self)	:
		tmp = self.process
		self.process = None
		return tmp