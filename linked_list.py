from typing import Any


class Node:

    def __repr__(self) -> str:
        return f'{self.__dict__}'

    def new_node(self, item: str, value: int) -> Any:
        self.__dict__[item] = value

    def next_node(self, )


linked_list: Node = Node()

linked_list.new_node('A', 6)
linked_list.new_node('B', 3)
linked_list.new_node('C', 4)
linked_list.new_node('D', 2)
linked_list.new_node('E', 1)
print(linked_list)
