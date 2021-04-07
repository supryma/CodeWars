"""Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
   Square all numbers k (0 <= k <= n) between 0 and n.
   Count the numbers of digits d used in the writing of all the k**2.
   Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count."""


def nb_dig(n, d):
    b = []
    for el in range(n):
        a = el**2
        a = str(a)
        b.append(a)
        b.append(str(n**2))
    k = 0
    for el1 in b:
        for el2 in el1:
            if str(d) == el2:
                k += 1
    return k
