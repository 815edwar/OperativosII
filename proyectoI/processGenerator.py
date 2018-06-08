#!/usr/bin/env python3
#
# Descripcion: Implementacion de hilo que se encarga de generar procesos cada cierto intervalo de tiempo
# que depende de las unidades de tiempo establecidas como intervalo y la transformacion que esta utilizando
# el simulador en el momento
#
# Autores: Domingo Arteaga y Edwar Yepez
#

from threading import Thread 
from process import *
from random import randint
import time

class ProcessGenerator(Thread):

	def __init__(self, queue, mutex_np, num_np, gen_interval, i_logic):
		super(ProcessGenerator, self).__init__()
		self.i_logic = i_logic

		self.queue = queue
		self.mutex_np = mutex_np
		self.num_np = num_np
		self.gen_interval = gen_interval


	def run(self):
		# for _ in range(16):
		while self.i_logic['loop']:
			process = Process(randint(12, 32))
			self.mutex_np.acquire()
			self.queue.enqueue(process)
			self.mutex_np.release()
			
			self.num_np.release()

			self.i_logic['screen'].acquire()
			self.i_logic['screen'].release()

			time.sleep(self.gen_interval * self.i_logic['speed'])