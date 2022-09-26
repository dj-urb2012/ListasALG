class Node:
    #Crea un nodo, sus atributos son
    #data = Dato a almacenar en el nodo
    #next = Accede al elemento siguiente
    #prev = Accede al elemento anterior
    def __init__(self, data = None, next = None, prev = None):
        self.next = next
        self.data = data
        self.prev = prev

#Tiene como atributos la cabeza y la cola de la lista
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Retorna el tamaño de la lista
    def get_size(self):
        #Se crea una variable contador
        count = 0
        #Se inicializa una variable que contenga la cabeza
        current_node = self.head
        #Si el elemento no es nulo, aumenta el contador por 1
        while current_node:
            count += 1
            #Se le asigna el valor de next, permitiendo iterar por la lista hasta llegar
            #al ultimo elemento
            current_node = current_node.next
        return count
    #Permite añadir un nodo al final lista
    def append_node(self, data):
        #Se crea un nodo con los datos deseados
        new_node = Node(data)
        #Verificamos si la cabeza esta vacia, en ese caso la lista esta vacia
        if self.head is None:
            #El primer nodo sera cabeza y cola al mismo tiempo
            self.head = new_node
            self.tail = new_node
        else:
            #Caso contrario, añadimos un nuevo nodo al final
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    #Permite añadir un nodo al inicio lista
    def prepend_node(self, data):
        #Se crea un nodo con los datos deseados
        new_node = Node(data)
        #Verificamos si la cabeza esta vacia, en ese caso la lista esta vacia
        if self.get_size() == 0:
            #El primer nodo sera cabeza y cola al mismo tiempo
            self.head = new_node
            self.tail = new_node
        else:
            #Caso contrario, añadimos un nuevo nodo al inicio
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def remove_first(self):
        head = self.head
        if self.get_size() == 0:
            return
        elif self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = head.next
            self.head.prev = None
            head.next = None

    def remove_last(self):
        tail = self.tail
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = tail.prev
            self.tail.next = None
            tail = None

    def iterate_from_beg(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def iterate_from_end(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev

doubly = DoublyLinkedList()