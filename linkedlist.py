#!/usr/bin/env python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class mLinkedlist:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        # the last node links to "None"
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def append(self, node):
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def delete(self, value):
        if not self.head:
            raise Exception("List is empty")
        if self.head.data == value:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == value:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % value)


def main():
    first_node = Node("value1")
    second_node = Node("value2")
    llist = mLinkedlist()
    llist.append(first_node)
    llist.append(second_node)
    llist.delete("value3")
    print(llist)


if __name__ == "__main__":
    main()
