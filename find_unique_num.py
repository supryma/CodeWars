"""There is an array with some numbers.
   All numbers are equal except for one.
   Try to find it!"""


def find_unique(arr):

    for i in range(len(arr)):
        if i == 0:
            if len(arr) > 2:
                if (arr[i+1] != arr[i]) and arr[i+2] != arr[i]:
                    return arr[i]

        if i == len(arr)-1:
            if (arr[i-1] != arr[i]) and (arr[i-2] != arr[i]):
                return arr[i]

        if i < len(arr):
            if (arr[i] != arr[i-1]) and (arr[i] != arr[i+1]):
                return arr[i]
