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

	def __init__(self, cores_qty = 4, gen_interval = 2, speed = 1):
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
			self.cores.append(CPU(i))


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


Main = Main()
Main.run()