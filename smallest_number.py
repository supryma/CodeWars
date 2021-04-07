"""Given a list of digits,
   return the smallest number that could be formed from these digits,
   using the digits only once (ignore duplicates)."""


def min_value(digits):
    digits.sort()
    i = ''
    for el in digits:
        if str(el) in i:
            continue
        else:
            i += str(el)
    return int(i)
