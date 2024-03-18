class linked_list:
    def __init__(self, head = None):
        self.head = head
        

        def append(self, new_node):
            current = self.head

            if current:
                while current.next:
                    current = current.next
                curent.next = new_node

            else:
                self.head = new_node
