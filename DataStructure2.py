#Define the basic element that forms the list
class Node:
    #Constructor
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.__data = data
        self.__next_node = next_node
        self.__prev_node = prev_node

    #Get data
    def get_data(self):
        return self.__data

    #Get next node
    def get_next(self):
        return self.__next_node

    #Set next node
    def set_next(self, new_next):
        self.__next_node = new_next

    #Get prev node
    def get_prev(self):
        return self.__prev_node

    #Set prev node
    def set_prev(self, new_prev):
        self.__prev_node = new_prev



class DoublyLinkedList:
    def __init__(self):
        head = Node('__head__')
        self.__head = head
        self.__tail = head

#Get the first node that contains that specified data
    def get_node(self, data):
        current = self.__head

#Go through the list until it fings a match or Reaches the end of it
        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
        return None

#Append new  node to the end of te list
    def append(self,data):
        new_tail =Node(data)
        self.__tail.set_next(new_tail)
        new_tail.set_prev(self.__tail)
        self.__tail = new_tail

#Delete the first node that contains the specified data
    def delete(self, data):
        del_node = self.get_node(data)
        if del_node:
            prev_node = del_node.get_prev()
            next_node = del_node.get_next()
            prev_node.set_next(next_node)
            if next_node:
                next_node.set_prev(prev_node)
            else:
                self.__tail = prev_node

#Get the number of nodes in the list
    def size(self):
        current = self.__head
        count = 0

        while current:
            count += 1
            current = current.get_next()
        return count - 1

    def print_list(self):
        current = self.__head.get_next()
        while current:
            print(current.get_data())
            current = current.get_next()

    def print_backwards(self):
        current = self.__tail
        while current.get_prev():
            print(current.get_data())
            current = current.get_prev()

#Testing Out the list

#Create a list
list = DoublyLinkedList()

list.append('cat')
list.append('dog')
list.append('snake')
list.append('bird')
list.print_list()
list.print_backwards()
list.delete('cat')
list.print_list()
a = list.size()
print(a)






