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
            
    # easily view list for testing purposes    
    def viewList(self):
        node = self.head 
        
        while node != None:
            print(node.value)
            node = node.next
    
    def peek(self):
        print(f"Head: {self.head.value}\nTail: {self.tail.value}")
        
    def remove(self, node):
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
    
    def switch(self, nodeOne, nodeTwo):
        # save nodeTwo next and prev
        tempNext = nodeTwo.next
        tempPrev = nodeTwo.prev

        # change nodeTwos prev and next node to point to nodeOne
        nodeTwo.prev.next = nodeOne
        nodeTwo.next.prev = nodeOne

        # move nodeTwo to nodeOne
        nodeTwo.next = nodeOne.next
        nodeTwo.prev = nodeOne.prev

        # change nodeOne's prev and next nodes to point to nodeTwo
        nodeOne.prev.next = nodeTwo
        nodeOne.next.prev = nodeTwo

        # move nodeOne to nodeTwos old location
        nodeOne.next = tempNext
        nodeOne.prev = tempPrev



    
    def containsNodeWithValue(self, value):
        pass
    
    def removeNodeWithValue(self, value):
        pass

