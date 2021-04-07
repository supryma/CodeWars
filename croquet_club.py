"""The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
   They would like your help with an application form that
   will tell prospective members which category they will be placed.

   To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
   In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap."""


def open_or_senior(data):
    a = []
    for el1 in data:
        if (el1[0] >= 55) and (el1[1] > 7):
            a.append('Senior')
        else:
            a.append('Open')
    return a
