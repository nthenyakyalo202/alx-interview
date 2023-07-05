#!/usr/bin/python3

""" n number of boxes
   each box is numbered sequentially from 0 to n - 1 and
   each box may contain keys to the other boxes."""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened """
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
