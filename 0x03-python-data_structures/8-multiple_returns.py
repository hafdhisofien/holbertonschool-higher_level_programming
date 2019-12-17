#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = []
    tuple.append(len(sentence))
    if len(sentence) == 0:
        tuple.append(None)
    else:
        tuple.append(sentence[0])
    return (tuple)
