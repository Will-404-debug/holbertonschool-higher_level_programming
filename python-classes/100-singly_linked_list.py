#!/usr/bin/python3


"""Module for defining a singly linked list.

This module defines the Node class
which represents a node in the singly linked list.
It also defines the SinglyLinkedList class 
which provides methods to manage a singly
linked list including sorted insertion and string representation.
"""


class Node:
    """Represents a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node, must be an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node reference."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node reference, must be a Node object or None."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list.

    Attributes:
        head (Node): The head node of the list.
    """
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the list."""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The data value of the new node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
