
# Node class to be used by multiple data structures
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Doubly Linked List class that will be used in future projects
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        length = 0
        node = self.head

        while node != None:
            length += 1
            node = node.next
            
        return length

    def __repr__(self):
        print_list = []
        node = self.head 
        
        while node != None:
            print_list.append(node.value)
            node = node.next

        return f"Contains: {print_list}"

    # adds node to end of linked list
    def add(self, node):
        # checks to see if any nodes exist yet
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None
        else:
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
               
    def viewList(self):
        node = self.head 
        
        while node != None:
            print(node.value)
            node = node.next

    def peek(self):
        return (self.head.value, self.tail.value)
        
    def remove(self, node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            node.next.prev = None
        elif node == self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:  
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = None
        node.prev = None
    
    def addBefore(self, node, nodeToAdd):
        nodeToAdd.next = node
        nodeToAdd.prev = node.prev
        
        if node == self.head:
            self.head = nodeToAdd
            node.prev = nodeToAdd
        else:
            node.prev.next = nodeToAdd
            node.prev = nodeToAdd
            
    def addAfter(self, node, nodeToAdd):
        nodeToAdd.next = node.next
        nodeToAdd.prev = node

        if node == self.tail:
            self.tail = nodeToAdd
            node.next = nodeToAdd
        else:
            node.next.prev = nodeToAdd
            node.next = nodeToAdd
    
    def containsNodeWithValue(self, value):
        node = self.head

        while node != None and node.value != value:
            node = node.next
        return node != None
    
    def removeNodeWithValue(self, value):
        node = self.head

        while node != None and node.value != value:
            node = node.next
        if node == None:
            return
        else:
            self.remove(node)

