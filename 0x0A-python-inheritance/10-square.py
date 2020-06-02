#!/usr/bin/python3
"""
Module - Square
"""


class Square(__import__('9-rectangle').Rectangle):
    """ description of a square """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
