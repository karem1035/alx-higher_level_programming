#!/usr/bin/python3
""" A class that taks a list and sort it """


class MyList(list):

    """the init method"""

    def __init__(self):
        super().__init__()

    """ sort the self list and print it """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
