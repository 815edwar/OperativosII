class Process():

	def __init__(self, pid, required_t, min_t):
		self.pid = pid
		self.required_t = required_t
		self.min_t = min_t

	def done(self):
		return self.required_t == self.min_t
	