class SLL:
    size_list = 0

    def __init__(self, head=None):
        self.head = head
        if head is not None:
            self.size_list += 1
        self.UpdateTail()

    def InsertHead(self, node):
        node.next = self.head
        self.head = node
        self.size_list += 1
        self.UpdateTail()

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        self.size_list += 1
        self.UpdateTail()

    def Insert(self, node, position):
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            i = 1
            while curr.next is not None:
                if i != (position - 1):
                    curr = curr.next
                elif i == (position - 1):
                    node.next = curr.next
                    curr.next = node
                    break
                i += 1
            if position == 1:
                self.InsertHead(node)
                return
            elif position <= 0 or position > self.size_list:
                print("Invalid Position")
                return
        self.size_list += 1
        self.UpdateTail()

    def SortedInsert(self, node):
        if self.head is None:
            self.head = node
        else:
            is_sorted = True
            curr = self.head
            while curr.next is not None:
                if curr.next.value < node.value:
                    curr = curr.next
                else:
                    is_sorted = False
                    break
            if is_sorted:
                curr.next = node
            else:
                self.Sort()
                present = None
                curr = self.head
                while curr is not None and curr.value < node.value:
                    present = curr
                    curr = curr.next
                node.next = curr
                if present is not None:
                    present.next = node
                else:
                    self.head = node
        self.size_list += 1
        self.UpdateTail()

    def Search(self, node):  # Return weird characters
        curr = self.head
        while curr is not None:
            if curr.value == node.value:
                return curr
            curr = curr.next
        return None

    def DeleteHead(self):
        if self.head is None:
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size_list -= 1
            self.UpdateTail()

    def DeleteTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
        self.size_list -= 1
        self.UpdateTail()

    def Delete(self, node):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        if node is None:
            return
        if self.head.next.value == node.value:
            self.head.next = self.head.next.next
            self.size_list -= 1
            self.UpdateTail()
            return
        else:
            curr = self.head
            while curr.next is not None:
                if curr.next.value == node.value:
                    curr.next = curr.next.next
                    self.size_list -= 1
                    self.UpdateTail()
                    return
                curr = curr.next
        self.size_list -=1

    def Sort(self):
        if self.head is None or self.head.next is None:
            return

        first_check = self.head
        second_check = self.head.next
        first_check.next = None

        while second_check is not None:
            curr = second_check
            second_check = second_check.next
            if curr.value <= first_check.value:
                curr.next = first_check
                first_check = curr
            else:
                moving_curr = first_check
                while (
                    moving_curr.next is not None and moving_curr.next.value < curr.value
                ):
                    moving_curr = moving_curr.next
                curr.next = moving_curr.next
                moving_curr.next = curr
        self.head = first_check
        self.UpdateTail()

    def Clear(self):
        self.head = None
        self.size_list = 0
        self.UpdateTail()

    def Print(self):
        single_linked_list = []
        is_sorted = True
        curr = self.head
        moving_curr = self.head
        while curr is not None:
            single_linked_list.append(curr.value)
            curr = curr.next
        while moving_curr is not None and moving_curr.next is not None:
            if moving_curr.value > moving_curr.next.value:
                is_sorted = False
            moving_curr = moving_curr.next

        var_sort = ""
        if is_sorted is True:
            var_sort += "sorted"
        else:
            var_sort += "not sorted"
        print(
            "The lenght of the list: ",
            self.size_list,
            "\nThe list is",
            var_sort,
            "\nThe content in the list are: ",
            single_linked_list,
        )
        
        return
    
    def UpdateTail(self):
        curr = self.head
        while curr.next is not None and curr.next != self.head:
            curr = curr.next
        self.tail = curr
