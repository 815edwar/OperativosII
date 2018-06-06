from threading import Semaphore
import pygame, sys
from pygame.locals import *

class CPU:
	
	def __init__(self, pk, quantum = 8):
		self.pk = pk
		self.quantum = quantum
		self.process = None
		self.pending_job = Semaphore(0)
		self.free = True
		self.posx = 100
		self.posy = 400


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

	def draw(self,window,font,px_offset):
		worker1 = pygame.image.load("images/worker1.png")
		worker2 = pygame.image.load("images/worker2.png")
		worker3 = pygame.image.load("images/worker3.png")
		tmp = pygame.draw.rect(window, (154, 180, 200), (self.posx + px_offset, self.posy,100,120))
		cpu_name = window.blit(font.render('cpu' + str(self.pk), True, (255,0,0)), tmp.topleft)
		px = tmp.centerx - 5
		py = tmp.centery - 10


		try:
			if self.process.pid % 2 == 0:
				window.blit(worker3,[px-50,py+80])
			else:
				window.blit(worker2,[px-50,py+80])
			pid = "p" + str(self.process.pid)
		except:
			window.blit(worker1,[px-50,py+80])
			pid = "vacio"
		process = window.blit(font.render(pid, True, (255,0,0)), (px, py))
	