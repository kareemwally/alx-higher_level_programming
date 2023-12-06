#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorte = list(a_dictionary)
    sorte.sort()
    for i in sorte:
        print("{:s}: {}".format(i, a_dictionary[i]))
