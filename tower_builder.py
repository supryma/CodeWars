"""Build Tower by the following given argument:
   number of floors (integer and always greater than 0).

   Tower block is represented as *"""


def tower_builder(n_floors):
    a = []
    c = '*'
    j = 1
    i = 0
    while i != n_floors:
        b = ((n_floors - j) * ' ') + c + ((n_floors - j) * ' ')
        a.append(b)
        c += '**'
        j += 1
        i += 1
    return a
