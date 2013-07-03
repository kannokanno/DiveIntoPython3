#!/usr/bin/python

def false_only(xs):
    """ Select only false elements

    Arguments:
        xs - List

    Returns: List
    """
    # 内包表記を使えばもっと簡単だけどchap2では出てこないので使わない
    false_elements = []
    for x in xs:
        if not xs:
            false_elements.append(x)
    return false_elements
