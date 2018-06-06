from threading import Thread
import time

class CommandLine(Thread):
    def __init__(self, proc_gen, ready_tree, cores, mutex_np, num_np, screen):
        super(CPUWorker, self).__init__()

        self.loop = True
        self.proc_gen = proc_gen
        self.ready_tree = ready_tree
        self.cores = cores

    def run(self):
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

    def print_menu(self):
    	os.system('clear')
    	print(30 * "-" + " MENU " + 30 * "-")
    	print("1. Generar un proceso")
    	print("2. Ver procesos esperando para pasar al árbol de listos")
    	print("3. Imprimir árbol de listos")
    	print("4. Ver procesadores")
    	print("5. Salir")
    	print(66 * "-")
