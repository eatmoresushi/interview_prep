#!/usr/bin/env python3

"""
First, a given key can appear in a dictionary only once. Duplicate keys are not allowed. A dictionary maps each key to a corresponding value, so it doesn’t make sense to map a particular key more than once. If you specify a key a second time during the initial creation of a dictionary, then the second occurrence will override the first.

Second, a dictionary key must be of a type that is immutable. For example, you can use an integer, float, string, or Boolean as a dictionary key. However, neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable. Values, on the other hand, can be any type and can be used more than once.
"""

LINKEDLIST_LENGTH = 10


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"key: {self.key}, value: {self.value}"


class mLinkedlist:
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append([node.key, node.value])
            node = node.next
        nodes.append(None)
        return " -> ".join([":".join(pair) for pair in nodes if pair])


def hash_and_map(key):
    # 	Return the hash value of the object (if it has one). Hash values are integers.
    return hash(key) % LINKEDLIST_LENGTH


class mHashtable:
    def __init__(self):
        self.array_llist = [None] * LINKEDLIST_LENGTH

    def add(self, node):
        index = hash_and_map(node.key)
        if not self.array_llist[index]:
            self.array_llist[index] = mLinkedlist(node)
        else:
            current_head = self.array_llist[index].head
            while current_head.next:
                current_head = current_head.next
            current_head.next = node

    def retrieve(self, key):
        index = hash_and_map(key)
        if self.array_llist[index]:
            current_head = self.array_llist[index].head
            while current_head.key != key and current_head.next:
                current_head = current_head.next
            return current_head.value
        return "Key not found"


def main():
    first_node = Node("key1", "value1")
    second_node = Node("key2", "value2")
    third_node = Node("key3", "value3")
    m_hashtable = mHashtable()
    m_hashtable.add(first_node)
    m_hashtable.add(second_node)
    m_hashtable.add(third_node)
    print(m_hashtable.retrieve("key3"))


if __name__ == "__main__":
    main()
