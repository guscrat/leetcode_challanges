from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'{self.data}'


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.ll_list = deque()

    def __repr__(self) -> str:
        return f'{self.__dict__["ll_list"]}'

    def next(self):
        return f'{self.next}'

    def insertAtEnd(self, data):
        self.ll_list.append(Node(data))

    def insertAtBegin(self, data):
        self.next = self.ll_list[0]
        self.ll_list.appendleft(data)


ll_test: LinkedList = LinkedList()

ll_test.insertAtEnd(1)
ll_test.insertAtEnd(2)
ll_test.insertAtBegin(2)
ll_test.insertAtEnd(1)
ll_test.insertAtEnd(2)
ll_test.insertAtBegin(2)


print(ll_test)
print(ll_test.next)
