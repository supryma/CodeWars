"""Count the number of divisors of a positive integer n."""


def divisors(n):
    answer = 1
    for el in range(1, n):
        if n == 0:
            return 0
            break
        if n % el == 0:
            answer += 1
    return answer
