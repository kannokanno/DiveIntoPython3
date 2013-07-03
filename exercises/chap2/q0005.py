# -*- coding: utf-8 -*-
#!/usr/bin/python

def numbering(xs):
    """ Convert xs to [(index, element), ...]

    Arguments:
        xs - List

    Returns: List of tuple
        (index, element)
        index   - index of element
        element - original element
    """
    # 手続き的。素直
    number_pairs = []
    for i in range(len(xs)):
        number_pairs.append((i, xs[i]))
    return number_pairs

# 別解。ただこれだと練習にならないかもしれない。
def _numbering(xs):
    return list(enumerate(xs))
