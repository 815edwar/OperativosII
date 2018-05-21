# -*- coding: utf-8 -*-
import os
from cpu import CPU
from queue import Queue

class Main:

	def __init__(self, cores_qty = 4):
		self.loop = True
		self.cores = []
		self.new_processes = Queue()

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


Main = Main()
Main.run_terminal()