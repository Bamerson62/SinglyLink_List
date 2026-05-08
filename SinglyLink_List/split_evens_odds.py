from singly_linked_list import SinglyLinkedList, Node

class SplitEvensOdds(SinglyLinkedList):

    def split_evens_odds(self):
        evens = SinglyLinkedList()
        odds = SinglyLinkedList()

        current = self._SinglyLinkedList__head
        self._SinglyLinkedList__head = None
        self._SinglyLinkedList__tail = None
        self._SinglyLinkedList__count = 0

        ev_head = ev_tail = None
        od_head = od_tail = None

        while current:
            nxt = current.next
            current.next = None

            if current.data % 2 == 0:
                if ev_head is None:
                    ev_head = ev_tail = current
                else:
                    ev_tail.next = current
                    ev_tail = current
            else:
                if od_head is None:
                    od_head = od_tail = current
                else:
                    od_tail.next = current
                    od_tail = current

            current = nxt

        evens._SinglyLinkedList__head = ev_head
        evens._SinglyLinkedList__tail = ev_tail
        evens._SinglyLinkedList__count = self._count_nodes(ev_head)

        odds._SinglyLinkedList__head = od_head
        odds._SinglyLinkedList__tail = od_tail
        odds._SinglyLinkedList__count = self._count_nodes(od_head)

        return evens, odds

    def _count_nodes(self, node):
        c = 0
        while node:
            c += 1
            node = node.next
        return c
