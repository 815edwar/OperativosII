from threading import Thread
from process import *
import time
import os

class CommandLine(Thread):
	def __init__(self, proc_gen, ready_tree, cores, mutex_np, num_np, i_logic):
		super(CommandLine, self).__init__()

		self.i_logic = i_logic
		self.proc_gen = proc_gen
		self.ready_tree = ready_tree
		self.cores = cores
		self.mutex_np = mutex_np
		self.num_np = num_np

	def run(self):
		while self.i_logic['loop']:
			self.print_menu()
			choice = input("Escoja una opción [1-5]: ")

			if choice == "1":	 
				timeslice = int(input("Indica el tiempo de ejecucion que requiere el proceso: "))

				process = Process(timeslice)
				self.mutex_np.acquire()
				self.proc_gen.enqueue(process)
				self.mutex_np.release()
				
				self.num_np.release()

				print("¡Se ha generado el proceso exitosamente!")
				input("Presiona enter para continuar")

			elif choice == "2":
				print("Procesos esperando para pasar al árbol: ")
				print(self.proc_gen)
				input("Presiona enter para continuar")
			elif choice == "3":
				print("Árbol de listos: ")
				print(self.ready_tree)
				input("Presiona enter para continuar")
			elif choice == "4":
				print("Procesadores: ")
				for c in self.cores:
					print(c)

				input("Presiona enter para continuar")
			elif choice == "5":
				print("Adios")
				self.i_logic['loop'] = False
				print("i_logic")
			else:
				print("Introduzca una opción válida.")

	def print_menu(self):
		os.system('clear')
		print(30 * "-" + " MENU " + 30 * "-")
		print("1. Generar un proceso")
		print("2. Ver procesos esperando para pasar al árbol de listos")
		print("3. Imprimir árbol de listos")
		print("4. Ver procesadores")
		print("5. Salir")
		print(66 * "-")
