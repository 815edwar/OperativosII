#!/usr/bin/env python
#
# Descripcion: Clase Nodo, Lista y ListaIterator que implementan el
#     	       TAD lista de forma enlazada
#
# Autor: Federico Flaviani
# 

# Descripcion: Clase que implementa el nodo de una lista
#   Atributos: data: almacena el contenido del nodo
#              next: referencia al proximo nodo

class ListNode:
  def __init__(self,data, link = None):
    self.data = data
    self.next = link

# Descripcion: Clase que implementa una lista enlazada
#   Atributos: _head: atributo privado que referencia al primer elemento de la lista
#              _size: atributo privado entero que indica la longitud de la lista

class LinkedList:
  def __init__(self):
    self._head = None
    self._size = 0

# Descripcion: Metodo que devuelve la longitud de la lista
#     Retorna: valor entero que indica la longitud de la lista

  def __len__(self):
    return self._size

# Descripcion: Metodo que verifica si el elemento target se encuentra
#              en algun nodo de la lista
#   Atributos: target: elemento a ser buscado en la lista
#     Retorna: valor booleano que indica si el elemento esta o no en la lista

  def __contains__(self, target):
    curNode = self._head
    while curNode is not None and curNode.data != target:
      curNode = curNode.next
    return curNode is not None

# Descripcion: Metodo que agrega un nuevo elemeto item dentro de la lista
#              Se crea un nuevo nodo que contiene al elemeto item y se
#              enlaza en la lista
#   Atributos: item: elemento a ser agregado a la lista

  def add(self, item):
    newNode = ListNode(item)
    newNode.next = self._head
    self._head = newNode
    self._size += 1

# Descripcion: Metodo que elimina el elemento item y su respectivo
#              nodo de la lista
#   Atributos: item: elemento a ser eliminado de la lista
#     Retorna: Si el elemento item se encuentra dentro de la lista 
#              se devuelve item

  def remove(self,item):
    predNode = None
    curNode = self._head
    while curNode is not None and curNode.data != item :
      predNode = curNode
      curNode = curNode.next

    assert curNode is not None, "El elemento tiene que estar en la lista para poder eliminarlo."

    self._size -= 1
    if curNode is self._head:
       self._head = curNode.next
    else:
       predNode.next = curNode.next
    return curNode.data

# Descripcion: Metodo que devuelve un iterador de la lista
#     Retorna: iterador de la lista

  def __iter__(self):
    return ListIterator(self._head)

# Descripcion: Clase que implementa un iterador de lista
#   Atributos: _curNode: atributo privado que hace referencia al
#              nodo "actual" en el que se encuentra el iterador

class ListIterator:
  def __init__(self,listHead):
    self._curNode = listHead

# Descripcion: Metodo que devuelve un iterador de la lista
#     Retorna: iterador de lista

  def __iter__(self):
    return self

# Descripcion: Metodo que devuelve el elemento del proximo nodo 
#              en el que se encuentra el iterador y actualiza el
#              nodo "actual" a su sucesor
#     Retorna: Si el nodo "actual" no es nulo devuelve el elemento 
#              del proximo nodo del iterador, sino se lanza una 
#              excepcion de tipo StopIteration

  def next(self):
    if self._curNode is None:
      raise StopIteration
    else :
      item = self._curNode.data
      self._curNode = self._curNode.next
      return item
