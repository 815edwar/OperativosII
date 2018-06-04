from threading import Semaphore

class CPU:
	
	def __init__(self, pk, quantum = 4):
		self.pk = pk
		self.quantum = quantum
		self.proccess = None
		self.pending_job = Semaphore(0)
		self.free = True


	def free(self):
		tmp = self.proccess
		self.proccess = None
		return tmp


	def rcv_proccess(self, proccess):
		self.proccess = proccess


	def run_proccess(self):
		self.proccess.min_t += 1


	def __repr__(self):
		cpu = "core: " + str(self.pk) + "\n"\
		 + "quantum: " + str(self.quantum) + "\n"\
		 + "proccess: " + str(self.proccess) + "\n" \
		 + 30 * "-" + "\n" 

		return cpu