"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        # Get the previous node before insertion. This will become the "prev" for the inserted node
        current_prev = self.prev

        # assign the previous for our node to a new node. (prev pointer now points to new node)
        # new node is created with the prev pointer going to the old prev node (current prev) and
        # with the next pointer going to self.
        # We assign 3 out of the 4 pointers in this one line of code
        self.prev = ListNode(value = value, prev = current_prev, next = self)

        # The last pointer we need to address is the one that points from the old prev node to self
        # Need to modify it so instead of pointing to self, it will point to 
        # This pointer only exists if the previous node was NOT None!
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    # Head pointer in this case probably refers to self.head and not the 
    # next and prev pointers between nodes
    def add_to_head(self, value):
        
        # regardless of empty or non-empty list, adding to head will increase length
        self.length += 1

        # case of empty linked list
        if self.head == None:
            self.head = ListNode(value = value, prev = None, next = None)
            self.tail = self.head

        # case of non-empty linked list
        else:
            # get the old head node
            old = self.head

            # Create new node that will become the head
            # Note that the insert_before method will handle all of the pointers for us.
            # We just need to make sure that the self.head and self.length attributes are also updated
            old.insert_before(value)
            
            self.head = old.prev


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):

        # save the current head node because we need to return its value at the end
        removed_node = self.head

        # if empty list, just return None
        if self.head == None:
            return None
        
        # if linked list only contains 1 value
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_node.value

        else:
            # save the node after the head node so that we can assign it as the new head
            new_head = self.head.next

            # delete the head
            self.head.delete

            # assign the new head
            self.head = new_head

            self.length -= 1
            return removed_node.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        
        # regardless of empty or non-empty list, adding to head will increase length
        self.length += 1

        # case of empty linked list, head = tail.
        # So we can re-use the code from add_to_head()
        if self.head == None:
            self.head = ListNode(value = value, prev = None, next = None)
            self.tail = self.head

        # case of non-empty linked list
        else:
            # get the old tail node
            old = self.tail

            # Create new node that will become the tail
            # Note that the insert_before method will handle all of the pointers for us.
            # We just need to make sure that the self.tail and self.length attributes are also updated
            old.insert_after(value)
            
            # assign the tail to the node we just added
            self.tail = old.next
  

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # save the current tail node because we need to return its value at the end
        removed_node = self.tail

        # if empty list, just return None
        if self.head == None:
            return None
        
        # if linked list only contains 1 value
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_node.value

        else:
            # save the node after the tail node so that we can assign it as the new tail
            new_tail = self.head.next

            # delete the tail
            self.tail.delete

            # assign the new tail
            self.tail = new_tail

            self.length -= 1
            return removed_node.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):

        # start from the first node and loop through the linked list until current = node
        current = self.head
        while current != node:
            current = current.next
        
        # save the value of the desired node and delete the node
        new_head_value = current.value
        current.delete
        # Remember that add_to_head adds +1 to length. So we need to -1 here.
        self.length -= 1

        # add a new node to head using the saved value
        self.add_to_head(new_head_value)

        # If there are only 2 nodes, then moving the head to the tail means we must
        # assign the old tail to be the new head
        if self.length == 2:
            self.tail = self.head.next
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):

        # start from the first node and loop through the linked list until current = node
        current = self.head
        while current != node:
            current = current.next

        # save the value of the desired node and delete the node
        new_tail_value = current.value
        current.delete
        # Remember that add_to_head adds +1 to length. So we need to -1 here.
        self.length -= 1

        # add a new node to head using the saved value
        self.add_to_tail(new_tail_value)

        # If there are only 2 nodes, then moving the head to the tail means we must
        # assign the old tail to be the new head
        if self.length == 2:
            self.head = self.tail.prev

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # start from the first node and loop through the linked list until current = node
        current = self.head
        while current != node:
            current = current.next

        # case where list has only 1 element
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # case where we delete the head
        elif current == self.head:
            self.head = current.next
        
        # case where we delete the tail
        elif current == self.tail:
            self.tail == current.prev

        # regardless of the case, we delete the node and shorten the list by one
        current.delete
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        
        # Start at the head and iterate through each list element
        # If an element is larger than the current max value, update max
        current = self.head
        max = current.value

        while current.value != self.tail.value:
            current = current.next
            if current.value > max:
                max = current.value
        
        return max

        
