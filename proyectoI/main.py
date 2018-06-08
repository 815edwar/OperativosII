#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Descripcion: Implementacion de hilo que se encarga iniciar el simulador de despachador de
# procesos de linux
#
# Autores: Domingo Arteaga y Edwar Yepez
#
import os, time, pygame, sys
from cpu import CPU
from queue import Queue
from processGenerator import *
from processMounter import *
from dispatcher import *
from cpuWorker import *
from commandLine import *
from threading import Semaphore
from tree import *
from pygame.locals import *
from getopt import getopt, GetoptError

class Main:

	def __init__(self, cpu_slices = 8, cores_qty = 4, gen_interval = 2, speed = 1):
		self.SPEED = speed
		self.screen = Semaphore()
		self.iteration = 0
		self.loop = True
		
		self.i_logic = {
			'speed' : speed,
			'loop' : self.loop,
			'screen' : self.screen
		}

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
		pg = ProcessGenerator(self.new_processes, self.mutex_np, self.num_np, self.gen_interval, self.i_logic)
		pg.start()
		pm = ProcessMounter(self.ready_tree, self.mutex_rb, self.num_rb, self.new_processes, self.mutex_np, self.num_np, self.i_logic)
		pm.start()
		d = Dispatcher(self.cores, self.ready_tree, self.mutex_rb, self.num_rb, self.free_cpus, self.i_logic)
		d.start()
		workers = []
		for c in self.cores:
			tmp = CPUWorker(c, self.ready_tree, self.mutex_rb, self.num_rb, self.free_cpus, self.i_logic)
			workers.append(tmp)
			tmp.start()

		cl = CommandLine(self.new_processes, self.ready_tree, self.cores, self.mutex_np, self.num_np, self.i_logic)
		cl.start()

		while self.i_logic['loop']:
			self.draw()
			time.sleep(1)
			self.iteration += 1

		sys.exit(2)


	def draw(self):
		pygame.init()
		window = pygame.display.set_mode((1080,720))
		background_image = pygame.image.load("images/background2.jpg")
		background_color = (255,255,255,)
		window.blit(background_image,[0,0])
		font = pygame.font.SysFont('Arial', 15)
		pygame.display.set_caption("CFS")

		self.new_processes.draw(window, font)
		self.ready_tree.draw(window, font)
		
		px = 0
		i = 0
		for c in self.cores:
			c.draw(window,font,px)
			px += 110       
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()


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
			if a == "rapida":
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