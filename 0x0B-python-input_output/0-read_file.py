#!/usr/bin/python3
"""
Module for read_file, function that reads
a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    read_file: read a file using
    with statement
    """


with open("my_file_0.txt", mode='r', encoding="utf-8") as f:
    read_data = f.read()
print("{:s}".format(read_data), end="")
f.closed