"""The smallest number should come first,
   and the largest number should come second."""


def min_max(lst):
    a = []
    lst.sort()
    a.append(lst[0])
    a.append(lst[-1])
    return a
