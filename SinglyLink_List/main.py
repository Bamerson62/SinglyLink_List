from singly_linked_list import SinglyLinkedList


def test_list(build_method):
    lst = SinglyLinkedList()
    build_method(lst, [10, 20, 30, 40, 50])
    lst.display()

    print("Delete the first node:", end=" ")
    lst.remove(10)
    lst.display()

    print("Delete the last node:", end=" ")
    lst.remove(50)
    lst.display()

    print("Delete the interior node:", end=" ")
    lst.remove(30)
    lst.display()

def main():
    print("---- Build a forward list ----")
    test_list(lambda l, data: l.build_forward_list(data))

    print("---- Build a backward list ----")
    test_list(lambda l, data: l.build_backward_list(data))

    print("---- Non-recursive reverse print test----")
    lst = SinglyLinkedList()
    lst.build_forward_list([10, 20, 30, 40, 50])
    print("Insertion order:", end=" ")
    lst.display()
    print("Reverse order (recursive):", end=" ")
    lst.display_reverse()
    print("Reverse order (non-recursive):", end=" ")
    lst.display_reverse_nr()

    print("---- Remove all test ----")
    lst = SinglyLinkedList()
    lst.build_forward_list([1, 2, 4, 6, 1, 3, 6])
    lst.display()
    print("Removing 1 and all duplicates:", end=" ")
    lst.remove_all(1)
    lst.display()
    print("Removing 6 and all duplicates:", end=" ")
    lst.remove_all(6)
    lst.display()

if __name__ == "__main__":
    main()

