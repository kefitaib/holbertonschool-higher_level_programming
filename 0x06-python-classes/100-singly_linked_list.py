#!/usr/bin/python3
"""singly linked list """


class Node:
    """ class Node that defines a node of a singly linked list """
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gat a sqaure"""
        return self.__data

    @data.setter
    def data(self, value):
        """set a data for the a node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")

        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = value

        elif type(value) is not Node:
            raise TypeError("next_node must be a Node object")

        else:
            self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        self.__head = Node()

    def sorted_insert(self, value):
        new = Node(value)
        tmp = self.__head
        if not tmp:
            self.__head = new

        else:
            while tmp:
                if tmp.data >= value:
                    break
                prev = tmp
                tmp = tmp.next_node

            if self.__head == tmp:
                new.next_node = self.__head
                self.__head = new

            elif not tmp:
                prev.next_node = new

            else:
                prev.next_node = new
                new.next_node = tmp

    def __str__(self):
        tmp = self.__head
        s = ""

        while tmp:
            s += str(tmp.data)
            if tmp.next_node:
                s += "\n"
            tmp = tmp.next_node

        return s
