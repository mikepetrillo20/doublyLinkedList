<<<<<<< HEAD
import unittest
from doublyLinkedList import Node, DoublyLinkedList

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        test_list = DoublyLinkedList()
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        test_list.add(one)
        test_list.add(two)
        test_list.add(three)

    def tearDown(self):
        pass

    def test_add(self):
        pass

    def test_viewList(self):
        pass
    
    def test_peek(self):
        pass

    def test_remove(self):
        pass

    def test_addBefore(self):
        pass

    def test_addAfter(self):
        pass

    def test_containsNodeWithValue(self):
        self.assertTrue(test_list.containsNodeWithValue(1), True)
    
    def test_removeNodeWithValue(self):
        pass
        
      
        

    


    





if __name__ == "__main__":
    unittest.main()

=======
from doublyLinkedListPractice import Node, DoublyLinkedList


# instance of DoublyLinkedList
test_list = DoublyLinkedList()

# # initially added
one = Node(1)
test_list.add(one)
two = Node(2)
test_list.add(two)
three = Node(3)
test_list.add(three)
four = Node(4)
test_list.add(four)
five = Node(5)
test_list.add(five)
six = Node(6)
test_list.add(six)
seven = Node(7)
test_list.add(seven)

# # testing output before any changes
print("\nView Current List")
test_list.viewList()
print("\nPeek Head and Tail")
test_list.peek()

# current tests
# test_list.removeNodeWithValue(5)
# test_list.removeNodeWithValue(1)
# test_list.removeNodeWithValue(7)
# test_list.removeNodeWithValue(3)

# testing output after any changes
print("\nView Current List")
test_list.viewList()
print("\nPeek Head and Tail")
test_list.peek()

# # old tests
# print("\nView addBefore Results")
# test_list.addBefore(two, one)
# test_list.addAfter(two, three)
# test_list.addAfter(four, five)
# test_list.addAfter(six, seven)
# test_list.viewList()
# test_list.peek()
>>>>>>> aa76ea2685c9d42bf4cffaf37a7047b13458348e
