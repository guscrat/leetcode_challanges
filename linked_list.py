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
        self.next = None
        self.ll_list = deque()

    def __repr__(self) -> str:
        # return {print(i) for i in self.__dict__["ll_list"]}
        return f'{self.__dict__["ll_list"]}'

    def next(self):
        return f'{self.next}'

    def insertAtEnd(self, data):
        self.ll_list.append(data)
        self.next = None

    def insertAtBegin(self, data):
        try:
            self.next = self.ll_list[0]
        except IndexError:
            self.next = None

        self.ll_list.appendleft(data)

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)

        if index > len(self.ll_list):
            return 'Index out of range'

        self.ll_list[index] = data

        try:
            self.next = self.ll_list[index + 1]
        except IndexError:
            self.next = None


ll_test: LinkedList = LinkedList()

ll_test.insertAtBegin('A')
ll_test.insertAtBegin('B')
ll_test.insertAtEnd('E')
ll_test.insertAtEnd('F')
ll_test.insertAtIndex('W', 3)

print(ll_test)
print(ll_test.next)
