from typing import List
class Node:
    def __init__(self, data)-> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=str(nodes.pop(0)))
            self.head = node
            for el in nodes:
                node.next_node = Node(data=el)
                node = node.next_node

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next_node
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self)-> None:
        node = self.head
        while node is not None:
            yield node
            node = node.next_node
    
    # def normal_travel(self)->None:
    
    def reverse_travel(self, head=None)-> None:
        if head is None or head.next_node is None:
            return head
        rest = self.reverse_travel(head.next_node)

        head.next_node.next_node = head
        head.next_node = None

        return rest





l = LinkedList(['a', 'b', 'c'])
print(l)
print('reversing')
print(l.reverse_travel())
# l = 
# print(l)

