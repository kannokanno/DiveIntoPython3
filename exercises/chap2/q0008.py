#!/usr/bin/python

def flatten(xs):
    """ Flatten of list

    Arguments:
        xs - List

    Returns: List
    """
    return _flatten(xs, [])

def _flatten(xs, result):
    for x in xs:
        if isinstance(x, list):
            _flatten(x, result)
        else:
            result.append(x)
    return result
