class Process():

	pid_counter = 0

	def __init__(self, required_t, min_t=0):
		self.pid = self.pid_counter
		self.required_t = required_t
		self.min_t = min_t
		Process.pid_counter += 1

	def done(self):
		return self.required_t == self.min_t
	