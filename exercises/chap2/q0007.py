#!/usr/bin/python

def wordcount(xs):
    """ Count each word count

    Arguments:
        xs - List

    Returns: Dict
        key   - word
        value - count
    """
    counts = {}
    for x in xs:
        count = counts[x] if x in counts else 0
        counts[x] = count + 1
    return counts
