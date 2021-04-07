"""Move the first letter of each word to the end of it,
   then add "ay" to the end of the word.
   Leave punctuation marks untouched."""


def pig_it(text):
    a = text.split()
    c = ''
    for i in range(len(a)):
        if a[i].isalpha():
            b = a[i][1:] + a[i][0] + 'ay'
            c += b
            if i != len(a)-1:
                c += " "
        else:
            c += a[i]
    return c
