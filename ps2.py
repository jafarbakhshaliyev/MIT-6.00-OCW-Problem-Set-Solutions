# Problem Set 1
# Name: Jafar Bakhshaliyev

# Problem 1

def nugget(n):
    """
    This function takes a number n and returns a tuple as (a,b,c) which n satisfies the equation 6*a + 9*b + 20*c =
    n, otherwise it returns a tuple as (None,None,None)
    :param n: int
    :return: tuple
    """
    for c in range(0, (n // 20 + 1)):
        for b in range(0, (n // 9 + 1)):
            for a in range(0, (n // 6 + 1)):
                total = 6 * a + 9 * b + 20 * c
                if total == n: return (a, b, c)
    return (None, None, None)


trials = [50, 51, 52, 53, 54, 55]
for t in trials:
    print(nugget(t))


# It is observable to see that we can buy 56-65 combination of McNuggets (for ex: just add 6 to all numbers you have
# done starting from 50.

# Problem 2

# Theorem: If it is possible to buy x, x+1,…, x+5 sets of McNuggets, for some x, then it is
# possible to buy any number of McNuggets >= x, given that McNuggets come in 6, 9 and 20 packs.

# You can find the numbers which is greater and equal by x with just adding the smallest integer 6, and it is
# observable that it goes to from x+6....x+10 (also x+10...x+15), so it repeats after that.

# Problem 3

def largest_nugget(n):
    """
    This function takes a number n and prints the largest number (less than n) which does not satisfy equation
    6*a + 9*b + 20*c =  n.
    :param n: int
    :return: None
    """
    possibles = [1, 2, 3, 4, 5]
    count = 0
    for p in range(6, n):
        if nugget(p) != (None, None, None): count += 1
        if count == 6: print(
            f"Largest number of McNuggets that cannot be bought in exact quantity: {possibles[-1]}"); break
        if nugget(p) == (None, None, None): count = 0; possibles.append(p)
    return None


largest_nugget(100)


# Problem 4


def all_nugget(a1, b1, c1, n):
    """
    This function takes a size of packages as a1, b1, c1 and a number n, and it returns True which n satisfies
    the equation a1*a + b1*b + c1*c = n, otherwise it returns False.
    :param a1: int
    :param b1: int
    :param c1: int
    :param n: int
    :return: boolean
    """
    for c in range(0, (n // c1 + 1)):
        for b in range(0, (n // b1 + 1)):
            for a in range(0, (n // a1 + 1)):
                total = a1 * a + b1 * b + c1 * c
                if total == n: return True
    return False


def all_largest_nugget(packages):
    """
    This function takes a tuple of size of packages and prints the largest number of McNugget that does not satisfy
    equation a1*a + b1*b + c1*c = n.
    :param packages: tuple
    :return: None
    """
    bestSoFar = 0
    count = 0
    for n in range(6, 150):
        if all_nugget(packages[0], packages[1], packages[2], n): count += 1
        if count == 6: print(
            f"Given package sized {packages[0]}, {packages[1]}, {packages[2]}, the largest number of McNugget that "
            f"cannot "
            f"be bought in exact quantity is: {bestSoFar}"); break
        if not all_nugget(packages[0], packages[1], packages[2], n): count = 0; bestSoFar = n
    return None


trials = [(6, 9, 20), (5, 5, 3), (7, 8, 6)]
for package in trials:
    all_largest_nugget(package)
