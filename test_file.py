from doublyLinkedListPractice import Node, DoublyLinkedList


# instance of DoublyLinkedList
test_list = DoublyLinkedList()

# # initially added
two = Node(2)
test_list.add(two)
four = Node(4)
test_list.add(four)
six = Node(6)
test_list.add(six)

# # added after
one = Node(1)
three = Node(3)
five = Node(5)
seven = Node(7)

# # testing output before any changes
print("\nView Current List")
test_list.viewList()
print("\nPeek Head and Tail")
test_list.peek()
# print("\nView addBefore Results")
test_list.addBefore(two, one)
test_list.addAfter(two, three)
test_list.addAfter(four, five)
test_list.addAfter(six, seven)
# test_list.viewList()
# test_list.peek()

# # testing output after any changes
print("\nView Current List")
test_list.viewList()
print("\nPeek Head and Tail")
test_list.peek()