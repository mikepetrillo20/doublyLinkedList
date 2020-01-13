class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
     
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
        print(f"Head: {self.head.value}\nTail: {self.tail.value}")
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

