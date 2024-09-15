#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the
set. The player that cannot make a move loses the game. They play
x rounds of the game, where n may be different for each round. Assuming
Maria always goes first and both players play optimally, determine who
the winner of each game is.
"""


def isWinner(x, nums):
    """Return: name of the player that won the most rounds"""
    wins_maria = 0
    for round in range(x):
        n = nums[round]
        if n == 1:
            # maria automatically loses
            # print(f"n: {n} maria loses")
            continue
        prime = [True for _ in range(n + 1)]
        p = 2
        while (p * p <= n):
            # print(f"p: {p}, prime: {prime}")
            if prime[p] is True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        # get rid of 0 and 1, not a prime
        prime = prime[2:]
        # print(prime)

        if len([is_prime is True for is_prime in prime]) % 2 != 0:
            wins_maria += 1
            # print(f"n: {n} maria wins\n")
        # else:
        #     print(f"n: {n} maria loses\n")
    # print("wins_maria: ", wins_maria)
    if wins_maria > (x / 2):
        return "Maria"
    else:
        return "Ben"


if __name__ == '__main__':
    isWinner(1, [3])
