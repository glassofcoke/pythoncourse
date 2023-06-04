
#define the basic element that forms the list
class Node:
    #constructor
    def __init__(self, data = None, next_node= None):
        self.__data = data
        self.__next_node = next_node

    #Get data
    def get_data(self):
        return self.__data
    #Get next node
    def get_next(self):
        return self.__next_node
    #Set next node
    def set_next(self, new_next):
        self.__next_node = new_next


class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.__head = Node('__Head__')

    #Get the first node that contains the specified data
    def get_node(self, data):
        current = self.__head

    #Go through the list until it finds a match, or reach the end of the list
        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
        return None

    #Delete the first node that contains the specified data
    def delete(self, data):
        current = self.__head
        previous = None
    #Go through the list until it finds a match, or reach the end of the list
        while current:
            if current.get_data() == data:
                previous.set_next(current.get_next())
                break
            else:
                previous = current
                current = current.get_next()

    #Append new node to the end of the list
    def append(self, data):
        current = self.__head
    #Go to the last node in the list
        while current.get_next():
              current = current.get_next()

        #Append at the end of the list
        current.set_next(Node(data)) #shouldn't be set_next instead of data?!

    def size(self):
        current = self.__head
        count = 0
        while current:
            count+=1
            current = current.get_next()
        return count-1

    def print_list(self):
        current = self.__head.get_next()
        while current:
            print(current.get_data())
            current = current.get_next()

#Create list
list = SinglyLinkedList()
list.append('cat')
list.print_list()

#append
list.append('dog')
list.append('fish')
list.append('bird')
list.print_list()

#get_node
node = list.get_node('fish')
print(node.get_data())

#Delete
list.delete('fish')
list.print_list()

#Size of the list
a = list.size()
print(a)

