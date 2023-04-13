#from DLL import *
from build.lib.Datastructures.linear import DLL


class CDLL(DLL):
    def __init__(self, node=None):
        super().__init__(node)

        if node is not None:
            node.next = node
            node.prev = node

    def InsertHead(self, node):
        super().InsertHead(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def InsertTail(self, node):
        super().InsertTail(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def Insert(self, node, position):
        super().Insert(node, position)
        self.head.prev = self.tail
        self.tail.next = self.head

    def SortedInsert(self, node):
        super().SortedInsert(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def DeleteHead(self):
        super().DeleteHead()
        self.head.prev = self.tail
        self.tail.next = self.head

    def DeleteTail(self):
        super().DeleteTail()
        self.head.prev = self.tail
        self.tail.next = self.head

    def Delete(self, node):
        super().Delete(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def Clear(self):
        super().Clear()
        self.head = None
        self.tail = None

    def Print(self):
        double_linked_list = []
        is_sorted = True
        curr = self.head
        while curr is not None:
            double_linked_list.append(curr.value)
            curr = curr.next
            if curr == self.head:
                break
        moving_curr = self.head
        while moving_curr is not None and moving_curr.next is not None:
            if moving_curr.value > moving_curr.next.value:
                is_sorted = False
            moving_curr = moving_curr.next
            if moving_curr == self.head:
                break
        var_sort = ""
        if is_sorted is True:
            var_sort = "sorted"
        else:
            var_sort = "not sorted"
        result =(
            "The lenght of the list: ",
            self.size_list,
            "\nThe list is",
            var_sort,
            "\nThe content in the list are: ",
            double_linked_list,
        )
        return result
