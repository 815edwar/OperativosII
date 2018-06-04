#!/usr/bin/env python
#
# Descripcion: Implementacion del TAD Pila usando
#     	       listas enlazadas
#
# Autores: Domingo Arteaga y Edwar Yepez
# 

from linkedList import ListNode, ListIterator

# Descripcion: Clase que implementa una pila usando listas enlazadas
#   Atributos: _top: atributo privado que referencia al tope de la pila
#              _size: atributo privado entero que indica la longitud de la pila

class Stack:

  def __init__(self):
    self._top = None
    self._size = 0

# Descripcion: Metodo que indica si la pila es vacia o no
#     Retorna: booleano que indica si la pila es vacia

  def isEmpty(self):
    return self._top is None

# Descripcion: Metodo que devuelve la longitud de la pila
#     Retorna: entero que indica la longitud de la pila

  def __len__(self):
      return self._size

  def peek(self):
      return self._top


# Descripcion: Metodo que desempila el tope de la pila
#     Retorna: Si la pila no es vacia se devuelve el elemento
#              desempilado

  def pop(self):
      curnode = self._top
      self._size -= 1
      return curnode.data


# Descripcion: Metodo que empila un nuevo elemeto item dentro de la pila
#   Atributos: item: elemento a ser empilado en la pila

  def push(self,item):
      newNode = ListNode(item)
      newNode.next = self._top
      self._top = newNode
      self._size += 1
          

# Descripcion: Metodo que verifica si el elemento target se encuentra
#              en algun nodo de la lista
#   Atributos: target: elemento a ser buscado en la lista
#     Retorna: valor booleano que indica si el elemento esta o no en la lista

  def __contains__(self, target):
    curNode = self._top
    while curNode is not None and curNode.data != target:
      curNode = curNode.next
    return curNode is not None


# Descripcion: Metodo que devuelve un iterador de la pila
#     Retorna: iterador de la pila

  def __iter__(self):
    return ListIterator(self._top)