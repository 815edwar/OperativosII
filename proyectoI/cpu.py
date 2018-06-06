from threading import Semaphore

class CPU:
	
	def __init__(self, pk, quantum = 8):
		self.pk = pk
		self.quantum = quantum
		self.process = None
		self.pending_job = Semaphore(0)
		self.free = True


	def free(self):
		tmp = self.process
		self.process = None
		return tmp


	def rcv_process(self, process):
		self.process = process


	def run_process(self):
		self.process.min_t += self.quantum


	def __repr__(self):
		cpu = "core: " + str(self.pk) + "\n"\
		 + "quantum: " + str(self.quantum) + "\n"\
		 + "process: " + str(self.process) + "\n" \
		 + 30 * "-" + "\n" 

		return cpu