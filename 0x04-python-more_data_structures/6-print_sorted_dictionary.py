#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorte = list(a_dictionary)
    for i in sorte:
        print("{}: {}".format(i, a_dictionary[i]))
