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