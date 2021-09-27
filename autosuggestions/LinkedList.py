class ListNode:
    def __init__(self, val=None, next=None):
        if val is None:
            val = 0

        self.val = val
        self.next = next

    def reverse(self):
        if self.next is None:
            return self

        first = self
        prev = None
        while first is not None:
            _next = first.next
            first.next = prev
            prev = first
            first = _next

        return prev

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, *values):
        self.head = None
        self.tail = None

        if len(values) > 0:
            self.head = ListNode(values[0])
            self.tail = self.head

            if len(values) > 1:
                node = self.head
                for i in range(1, len(values)):
                    node.next = ListNode(values[i])
                    node = node.next
                    self.tail = node

    def __len__(self):
        length = 1
        node = self
        while True:
            if node.next is None:
                break
            else:
                length += 1
                node = node.next
        return length

    def __reversed__(self):
        if self.head:
            self.head.reverse()

    def __iter__(self):
        node = self.head

        while True:
            if node is None:
                break
            yield node.val
            node = node.next

    def printAll(self):
        x = str(self.head.val)

        if self.head.next is None:
            print(x)
            return x
        else:
            head = self.head.next

        while head:
            x = x + " -> " + str(head.val)
            head = head.next

        # print(x)
        return x

    def prepend(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            temp = self.head
            self.head = ListNode(val=val, next=temp)

    def append(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

    def insert(self, index, val):
        if index == 0:
            self.prepend(val)
            return

        node = ListNode(val)
        prev = self.head

        for i in range(index - 1):
            prev = prev.next

        _next = prev.next
        prev.next = node
        node.next = _next

    def add_by_popularity(self, string, called_times):
        node = self.head

        index = 0
        while True:

            if node is None:
                self.append((string,called_times))
                break

            if node.val[1] <= called_times:
                self.insert(index,(string,called_times))
                break

            node = node.next
            index += 1


    def sort_by_popularity(self, node_index: int, called_times: int):
        if node_index == 0:  # if node already at the beginning
            return

        node = self.head
        index = 0
        selected_node = None
        selected_index = None

        while True:
            if index == node_index - 1:
                selected_node = node.next  # save selected_node

            if node.val.called_times <= called_times and selected_index is None:
                selected_index = index

            node = node.next
            index += 1
            if node is None:
                break
        if selected_node and selected_index is not None:
            self.insert(selected_index, selected_node.val)
            self.remove(node_index+1)

    def remove(self, index: int):
        if index == 0:  # if head
            head = self.head
            self.head = self.head.next
            del head
            return

        i = 0
        node = self.head
        while True:
            if i == index - 1:
                node.next = node.next.next  # remove selected_node from position

            if node.next is None:
                self.tail = node

            node = node.next
            i += 1
            if node is None:
                break

    # def replace(self, node1: ListNode = None, node2: ListNode = None, prev1: ListNode = None, prev2: ListNode = None):
    #     prev2.next = node1
    #
    #     if prev1 is not None:
    #         prev1.next = node2
    #     else: # node1 is head
    #         self.head = node2
    #
    #     node1.next, node2.next = node2.next, node1.next

    # tail is not finished
