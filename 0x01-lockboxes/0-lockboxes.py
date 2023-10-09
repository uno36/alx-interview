#!/usr/bin/python3
'''task's 0 Module
'''


def canUnlockAll(boxes):
    key = [0]
    for k in key:
        for i in boxes[k]:
            if i not in key and i < len(boxes):
                key.append(i)
    if len(key) == len(boxes):
        return True
    else:
        return False
