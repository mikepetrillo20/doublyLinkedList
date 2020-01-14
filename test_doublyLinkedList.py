import unittest
from doublyLinkedList import Node, DoublyLinkedList

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.test_list = DoublyLinkedList()
        self.one = Node(1)
        self.two = Node(2)
        self.three = Node(3)
        self.four = Node(4)
        self.five = Node(5)
        self.test_list.add(self.one)
        self.test_list.add(self.two)
        self.test_list.add(self.three)

    def test__len__(self):
        self.assertEqual(len(self.test_list), 3)
        self.assertNotEqual(len(self.test_list), 0)
        self.assertNotEqual(len(self.test_list), 10)
        self.assertNotEqual(len(self.test_list), 99)

        self.test_list.add(self.four)
        self.assertEqual(len(self.test_list), 4)

        self.test_list.remove(self.four)
        self.assertEqual(len(self.test_list), 3)
    
    def test__repr__(self):
        self.assertEqual(repr(self.test_list), "Contains: [1, 2, 3]")
        
        self.test_list.add(self.four)
        self.assertEqual(repr(self.test_list), "Contains: [1, 2, 3, 4]")

        self.test_list.remove(self.four)
        self.assertEqual(repr(self.test_list), "Contains: [1, 2, 3]")

    def test_add(self):
        self.assertEqual(len(self.test_list), 3)
        self.test_list.add(self.four)
        self.assertEqual(len(self.test_list), 4)
        self.test_list.add(self.five)
        self.assertEqual(len(self.test_list), 5)
        self.test_list.remove(self.five)
        self.assertEqual(len(self.test_list), 4)
        self.test_list.remove(self.four)
        self.assertEqual(len(self.test_list), 3)
    
    def test_peek(self):
        self.assertEqual((self.test_list.head.value, self.test_list.tail.value), self.test_list.peek())
        self.test_list.remove(self.one)                 
        self.assertEqual((self.test_list.head.value, self.test_list.tail.value), self.test_list.peek())
        self.test_list.remove(self.three)                 
        self.assertEqual((self.test_list.head.value, self.test_list.tail.value), self.test_list.peek())
        self.test_list.add(self.one)
        self.assertEqual((self.test_list.head.value, self.test_list.tail.value), self.test_list.peek())
        self.test_list.add(self.three)
        self.assertEqual((self.test_list.head.value, self.test_list.tail.value), self.test_list.peek())

    def test_remove(self):
        self.test_list.remove(self.one)
        self.assertEqual(len(self.test_list), 2)
        self.test_list.remove(self.two)
        self.assertEqual(len(self.test_list), 1)
        self.test_list.remove(self.three)
        self.assertEqual(len(self.test_list), 0)
        self.test_list.add(self.one)
        self.test_list.add(self.two)
        self.test_list.add(self.three)



    def test_addBefore(self):
        pass

    def test_addAfter(self):
        pass

    def test_containsNodeWithValue(self):
        self.assertTrue(self.test_list.containsNodeWithValue(1))
        self.assertTrue(self.test_list.containsNodeWithValue(2))
        self.assertTrue(self.test_list.containsNodeWithValue(3))
        self.assertFalse(self.test_list.containsNodeWithValue(99))
        self.assertFalse(self.test_list.containsNodeWithValue(-99))
        self.assertFalse(self.test_list.containsNodeWithValue(0))
    
    def test_removeNodeWithValue(self):
        pass
        

if __name__ == "__main__":
    unittest.main()