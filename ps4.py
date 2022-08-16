# Problem Set 4
# Name: Jafar Bakhshaliyev

# Problem 1

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    F = [salary * save * 0.01]
    for i in range(1, years):
        F.append(F[i - 1] * (1 + 0.01 * growthRate) + F[0])
    return F


def testNestEggFixed():
    salary = 10000
    save = 10
    growthRate = 15
    years = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)

    print(savingsRecord)


testNestEggFixed()


# Problem 2

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    F = [salary * save * 0.01]
    for i in range(1, len(growthRates)):
        F.append(F[i - 1] * (1 + 0.01 * growthRates[i]) + F[0])
    return F


def testNestEggVariable():
    salary = 10000
    save = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)


testNestEggVariable()


# Problem 3

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    F = [(savings * (1 + growthRates[0] * 0.01) - expenses)]
    for i in range(1, len(growthRates)):
        F.append(F[i - 1] * (1 + 0.01 * growthRates[i]) - expenses)
    return F


def testPostRetirement():
    savings = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)


testPostRetirement()


# Problem 4


def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    F_pre = nestEggVariable(salary, save, preRetireGrowthRates)
    low, high = 0, F_pre[-1]
    F = postRetirement(F_pre[-1], postRetireGrowthRates, low)
    i = 0
    while abs(F[-1]) > epsilon and i <= 100:
        mid = (high + low) / 2
        expenses = mid
        print('Iteration', expenses)
        F = postRetirement(F_pre[-1], postRetireGrowthRates, expenses)
        if F[-1] > epsilon:
            low = mid
        else:
            high = mid
        F = postRetirement(F_pre[-1], postRetireGrowthRates, expenses)
        i += 1
    assert i <= 100, 'Iteration exceeded the limit'
    return expenses


def testFindMaxExpenses():
    salary = 10000
    save = 10
    preRetireGrowthRates = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)


testFindMaxExpenses()
