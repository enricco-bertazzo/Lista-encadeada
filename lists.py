class Node:# criaçao de nós
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self): # criacao da lista encadeada
        self._head = None
        self._size = 0

    def __str__(self):
        lists = ''
        for i in range(self._size):
            lists += str(self.__getitem__(i))
            lists += ', '
        return lists[:-2]

    def __len__(self): # mostra o numero de elementos na lista
        return self._size
    
    def __getitem__(self, index): # retorna o item na posiçao index desejada
        pointer = self._head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Index maior que o tamanho da lista")
        if pointer:
            return pointer.data
        raise IndexError("Index maior que o tamanho da lista")

    def __setitem__(self, index, element): # colocar um elemento em uma determinada posição
        pointer = self._head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Index maior que o tamanho da lista")
        if pointer:
            pointer.data = element
        else:
            raise IndexError("Index maior que o tamanho da lista")

    def append(self, element): # adiciona elementos na lista encadeada
        if self._head:
            pointer = self._head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self._head = Node(element)
        self._size += 1
    
    def remove(self, index):
        pointer = self._head
        if(pointer and index == -1):
            self._head = pointer.next
            self._size -= 1
            return
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Index maior que o tamanho da lista")
        if pointer:
            if(index != self._size):
                pointer.next = (pointer.next).next
            else:
                pointer.next = None
            self._size -= 1
        else:
            raise IndexError("Index maior que o tamanho da lista")

    def index(self, element): # apresenta o index do elemento desejado
        pointer = self._head
        i = 0
        while (pointer):
            if pointer.data == element:
                return i + 1
            pointer = pointer.next
            i += 1
        raise ValueError('{} is not in list'.format(element))

    def reverse(self): # inversão de toda a lista
        lista = ''
        for i in range(self._size -1, -1, -1):
            lista += str(self.__getitem__(i))
            lista += ', '
        return lista

    def destruct(self): # zerar a lista
        pointer = self._head
        self._head = None
        for i in range(self._size):
            if pointer:
                self.data = None
                pointer = pointer.next
                self.next = None
            else:
                raise IndexError("Index maior que o tamanho da lista")
        self._size = 0
    
    def equals(self, second_list):
        pointer = self._head
        if(self._size == len(second_list)):
            for i in range(self._size):
                if not(pointer.data == second_list[i]):
                    return False
                pointer = pointer.next
            return True
        else:
            return False