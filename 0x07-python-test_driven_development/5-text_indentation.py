#!/usr/bin/python3
"""
a simple function to print a seprated text on one of these
chars (`?`,`:`,`.`)
"""


def least_index(res, start=0):
    """
    a simple function to get the 1st index of one (`?`,`.`,`:`)
    """
    try:
        dot = res.find('.', start)
        ques = res.find('?', start)
        colon = res.find(':', start)
    except IndexError:
        return None
    else:
        if dot < 0:
            return ques if ques < colon or colon == -1 else colon
        if ques < 0:
            return dot if dot < colon or colon == -1 else colon
        if colon < 0:
            return dot if dot < ques or ques == -1 else ques
        return dot if dot < ques and dot < colon \
            else ques if ques < dot and ques < colon else colon
    return -1


def text_indentation(text):
    """ the main function to seperate `text` base on
    (`:`,`?`,`.`)
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    start = 0
    while True:
        end = least_index(text, start)
        if end < 0:
            print(text[start:].strip(), end='')
            break
        sub = text[start:end + 1].strip()
        print(sub, '\n')
        start = end+1
