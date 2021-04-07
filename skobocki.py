"""Write a function that takes a string of parentheses,
   and determines if the order of the parentheses is valid.

   The function should return true if the string is valid,
   and false if it's invalid."""


def valid_parentheses(string):
    i = 0
    for el in string:
        if i == 0 and el == ')':
            return False
        elif el == '(':
            i += 1
        elif el == ')' and i != 0:
            i -= 1
    if i == 0:
        return True
    else:
        return False
