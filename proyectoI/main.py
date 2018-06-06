# -*- coding: utf-8 -*-
import os, time
from cpu import CPU
from queue import Queue
from processGenerator import *
from processMounter import *
from dispatcher import *
from cpuWorker import *
from threading import Semaphore
from tree import *
from getopt import getopt, GetoptError
import sys

class Main:

	def __init__(self, cpu_slices = 8, cores_qty = 4, gen_interval = 2, speed = 1):
		self.SPEED = speed
		self.screen = Semaphore()
		self.iteration = 0

		self.loop = True
		self.cores = []
		self.free_cpus = Semaphore(cores_qty)
		
		self.new_processes = Queue()
		self.mutex_np = Semaphore()
		self.num_np = Semaphore(0)
		
		self.ready_tree = RedBlackTree()
		self.mutex_rb = Semaphore()
		self.num_rb = Semaphore(0)
		
		self.gen_interval = gen_interval

		for i in range(cores_qty):
			self.cores.append(CPU(i, cpu_slices))


	def run(self):
		pg = ProcessGenerator(self.new_processes, self.mutex_np, self.num_np, self.gen_interval, self.SPEED, self.screen)
		pg.start()
		pm = ProcessMounter(self.ready_tree, self.mutex_rb, self.num_rb, self.new_processes, self.mutex_np, self.num_np, self.SPEED, self.screen)
		pm.start()
		d = Dispatcher(self.cores, self.ready_tree, self.mutex_rb, self.num_rb, self.free_cpus, self.SPEED, self.screen)
		d.start()
		workers = []
		for c in self.cores:
			tmp = CPUWorker(c, self.ready_tree, self.mutex_rb, self.num_rb, self.free_cpus, self.SPEED, self.screen)
			workers.append(tmp)
			tmp.start()

		while True:
			self.render()
			time.sleep(1)
			self.iteration += 1

	def render(self):
		self.screen.acquire()
		print(30 * "-" + "IMPRESION" + str(self.iteration) + 30 * "-")
		print(self.new_processes)
		print(30 * "-" + "ARBOL" + 30 * "-")
		print(self.ready_tree)
		print()
		print(30 * "-" + "CPU'S" + 30 * "-")
		for c in self.cores:
			print(c)
		self.screen.release()


if __name__ == "__main__":
	try:
		opts, args = getopt(sys.argv[1:], "", ['cpu-slices=', 'cores-quantity=', 'proc-gen-interval=', 'speed='])
	except GetoptError as err:
		print(err) # will print something like "option -a not recognized"
		sys.exit(2)

	quantum = 8
	cores_qty = 4
	gen_interval = 4
	speed = 1
	for o, a in opts:
		if o == "--cpu-slices":
			quantum = int(a)
		elif o == "--cores-quantity":
			cores_qty = int(a)
		elif o == "--proc-gen-interval":
			gen_interval = int(a)
		elif o == "--speed":
			if a == "ultra_rapida":
				a = 0
				speed = a
			elif a == "rapida":
				a = 1
				speed = a
			elif a == "normal":
				a = 3
				speed = a
			elif a == "lenta":
				a = 5
				speed = a
		else:
			assert False, "unhandled option"
	Main = Main(quantum, cores_qty, gen_interval, speed)
	Main.run()