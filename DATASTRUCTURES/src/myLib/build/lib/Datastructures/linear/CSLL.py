#from SLL import *
from build.lib.Datastructures.linear.SLL import SLL

class CSLL(SLL):

    def __init__(self, node=None):
        super().__init__(node)
        if node is not None:
            node.next = node
            self.tail = node

    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size_list += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
        self.size_list += 1

    def DeleteHead(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size_list -= 1

    def DeleteTail(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            curr.next = self.head
            self.tail = curr
        self.size_list -= 1

    def Clear(self):
        self.head = None
        self.tail = None
        self.size_list = 0

    def UpdateTail(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current.next is not self.head and current.next is not None:
                current = current.next
            self.tail = current


    def Print(self):
        if self.head is None:
            return "Empty list"
        else:
            result = ""
            print("Size of list: ", self.size_list)
            current = self.head
            while current.next != self.head:
                result += str(current.value) + " -> "
                current = current.next
            result += str(current.value)
            return result
