# -*- coding: utf-8 -*-

class Menu:

	def __init__(self):
		self.loop = True

	def print_menu(self):
		print(30 * "-" , "MENU" , 30 * "-")
		print("1. Generar un proceso")
		print("2. Ver procesos esperando para pasar al árbol de listos")
		print("3. Imprimir árbol de listos [Proximamente]")
		print("4. Ver procesadores [Proximamente]")
		print("5. Salir")
		print(67 * "-")


	def loop_menu(self):
		while self.loop:
			self.print_menu()
			choice = raw_input("Escoja una opción [1-5]")

			if choice=="1":	 
				print("Generar un proceso")
			elif choice=="2":
				print("Procesos esperando para pasar al árbol")
			elif choice=="3":
				print("[Proximamente]")
			elif choice=="4":
				print("[Proximamente]")
			elif choice=="5":
				print("Adios")
				self.loop=False
			else:
				print("Introduzca una opción válida.")


menu = Menu()
menu.loop_menu()