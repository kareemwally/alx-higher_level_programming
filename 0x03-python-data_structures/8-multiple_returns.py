#!/usr/bin/python3
def multiple_returns(sentence):
    two = sentence[0] if len(sentence) >= 0 else None
    one = len(sentence)
    return(one, two)
