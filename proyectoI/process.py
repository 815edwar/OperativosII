#!/usr/bin/env python3
#
# Descripcion: Representa una abstraccion de lo que es un proceso de linux
#
# Autores: Domingo Arteaga y Edwar Yepez
#

class Process():

	pid_counter = 2048

	def __init__(self, required_t, min_t=0):
		self.pid = self.pid_counter
		self.required_t = required_t
		self.min_t = min_t
		self.last_core = None
		Process.pid_counter += 1

	def done(self):
		return self.required_t <= self.min_t


	def __eq__(self, other):
		return self.min_t == other.min_t

	def __lt__(self, other):
		return self.min_t < other.min_t

	def __gt__(self, other):
		return self.min_t > other.min_t

	def __repr__(self):
		return "Process: " + str(self.pid) + " min_t: " + str(self.min_t) + " required_t: " + str(self.required_t)
	
