class linked_list:
    def __init__(self, head = None):
        self.head = head #inintializing the first node with only the head
    

        def append(self, new_node): # adding a new node at the end of the existing node
            current = self.head # make the head the current node 

            if current: 
                while current.next: # if there is a next node, then make the next node the current, having iterated the list
                    current = current.next
                current.next = new_node # if there isnt, then make the next a new node

            else:
                self.head = new_node # if non head, then maje the head a new node.and

        def delete():
            
