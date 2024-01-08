"""
Function if of same class
"""


def is_kind_of_class(obj, a_class):
    """
    return wheaher obj is in aninstance of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
