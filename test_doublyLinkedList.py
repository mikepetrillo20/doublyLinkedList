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