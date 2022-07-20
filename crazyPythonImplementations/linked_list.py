from platform import node


class Node(object):
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    def __repr__(self) -> str:
        return self.data


class LinkedList(object):
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next_node = Node(data=elem)
                node = node.next_node

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next_node
        nodes.append("None")
        # return " -> ".join(nodes)
        return nodes

    def print_list(self) -> None:
        if self.head == None:
            print("Linkedlist is Empty!")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data, end=" -> ")
                curr = curr.next_node

    # Getting the size of LinkedList
    def get_length(self) -> int:
        size = 0
        curr = self.head
        while curr != None:
            size += 1
            curr = curr.next_node
        return size

    # inserting at the begining
    def insert_at_start(self, data) -> None:
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        return

    # inserting at the end of the list
    def insert_at_end(self, data) -> None:
        new_node = Node(data)
        if self.head == None:
            new_node = self.head
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        return

    # inserting at the index
    def insert_at_position(self, data) -> None:
        new_node = Node(data)
        if self.head == None:
            new_node = self.head
        else:
            curr = self.head
            while True:
                pass


llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

# print(help(llist))
