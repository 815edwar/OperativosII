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

class Main:

	def __init__(self, cores_qty = 4, gen_interval = 2):
		self.loop = True
		self.cores = []
		self.new_processes = Queue()
		self.mutex_np = Semaphore()
		self.num_np = Semaphore(0)
		self.ready_tree = RedBlackTree()
		self.mutex_rb = Semaphore()
		self.num_rb = Semaphore(0)
		self.clock = Semaphore(0)
		self.generate = Semaphore(0)
		self.free_cpus = Semaphore(cores_qty)
		self.gen_interval = gen_interval
		self.secs_to_gen = 0
		self.iteration = 0
		self.can_run = {
			'generator' : Semaphore(1),
			'mounter' : Semaphore(1),
			'dispatcher' : Semaphore(1),
			'cores' : []
		}

		for i in range(cores_qty):
			self.cores.append(CPU(i))
			self.can_run['cores'].append( Semaphore(1) )


	def print_menu(self):
		os.system('clear')
		print(30 * "-" + " MENU " + 30 * "-")
		print("1. Generar un proceso")
		print("2. Ver procesos esperando para pasar al árbol de listos")
		print("3. Imprimir árbol de listos [Proximamente]")
		print("4. Ver procesadores [Proximamente]")
		print("5. Salir")
		print(66 * "-")


	def run_terminal(self):
		while self.loop:
			self.print_menu()
			choice = raw_input("Escoja una opción [1-5]: ")

			if choice == "1":	 
				print("Generar un proceso")
			elif choice == "2":
				print("Procesos esperando para pasar al árbol")
			elif choice == "3":
				print("[Proximamente]")
			elif choice == "4":
				print("[Proximamente]")
			elif choice == "5":
				print("Adios")
				self.loop=False
			else:
				print("Introduzca una opción válida.")

	def run(self):
		pg = ProcessGenerator(self.new_processes, self.mutex_np, self.num_np, self.clock, self.generate, self.can_run)
		pg.start()
		pm = ProcessMounter(self.ready_tree, self.mutex_rb, self.num_rb, self.new_processes , self.mutex_np, self.num_np, self.clock, self.can_run)
		pm.start()
		d = Dispatcher(self.cores, self.ready_tree, self.mutex_rb, self.num_rb, self.free_cpus, self.clock, self.can_run)
		d.start()
		workers = []
		for c in self.cores:
			tmp = CPUWorker(c, self.ready_tree, self.mutex_rb, self.num_rb, self.clock, self.can_run)
			tmp.start()
			workers.append(tmp)

		while True:
			self.render()
						
			for c in self.cores:
				if (not c.free):
					self.clock.acquire()
					

			if ( self.ready_tree.size > 0 ):
				self.clock.acquire()

			if ( self.new_processes._count > 0 ):
				self.clock.acquire()

			if (self.secs_to_gen == 0):
				self.secs_to_gen = self.gen_interval
				self.generate.release()
				self.clock.acquire()
			self.secs_to_gen -= 1

			time.sleep(10)
			
			for c in self.cores:
				self.can_run['cores'][c.pk].release()

			self.can_run['dispatcher'].release()

			self.can_run['mounter'].release()

			self.can_run['generator'].release()

			self.iteration += 1

	def render(self):

		print(30 * "-" + "ITERATION " + str(self.iteration) + 30 * "-")
		print(self.new_processes, self.new_processes._count)
		print(30 * "-" + "ARBOL" + 30 * "-")
		print(self.ready_tree)
		print()
		print(30 * "-" + "CPU'S" + 30 * "-")
		for c in self.cores:
			print(c)


Main = Main()
Main.run()