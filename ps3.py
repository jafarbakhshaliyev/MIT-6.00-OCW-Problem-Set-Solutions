# Problem Set 3
# Name: Jafar Bakhshaliyev

# Problem 1

from string import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


def countSubStringMatch(target, key):
    """
    This function takes a target and key strings and returns number of times key string appears in the target string
    by doing iteratively.
    :param target: str
    :param key: str
    :return: int
    """
    count = 0
    i = 0
    while i != len(target):
        index = target[i:].find(key)
        if index != -1:
            count += 1
        else:
            return count;
            break
        i += index + 1
    return count


def countSubStringMatchRecursive(target, key):
    """
    This function takes a target and key strings and returns number of times key string appears in the target string
    by doing recursively.
    :param target: str
    :param key: str
    :return: int
    """
    i = target.find(key)
    count = 0
    if i != -1:
        count = 1 + countSubStringMatchRecursive(target[(i + 1):], key)
    else:
        return count
    return count


pairs = [(target1, key10), (target1, key11), (target1, key12), (target1, key13), (target2, key10), (target2, key11),
         (target2, key12), (target2, key13)]

for target, key in pairs:
    print('Iterative result:', countSubStringMatch(target, key))
    print('Recursive result:', countSubStringMatchRecursive(target, key))


# Problem 2

def subStringMatchExact(target, key):
    """
    This function takes a target and key strings and returns a tuple for starting points (indexes) of matches of key
    to target.
    :param target: str
    :param key: str
    :return: tuple
    """
    match_points = ()
    i = 0
    while i != len(target):
        index = target.find(key, i)
        if index != -1:
            match_points += (index,)
        else:
            return match_points;
            break
        i = index + 1
    return match_points


for target, key in pairs:
    print('Match Points:', subStringMatchExact(target, key))


# Problem 3

def constrainedMatchPair(firstMatch, secondMatch, length):
    """
    This function takes match points for two different keys (as firstMatch and secondMatch) and
    length of the first key and returns a tuple of firstMatch points if it satisfies
    equation firstMatch + length + 1 = secondMatch.
    :param firstMatch: int
    :param secondMatch: int
    :param length: int
    :return: tuple
    """
    answer = ()
    for i in firstMatch:
        for j in secondMatch:
            if i + length + 1 == j:
                answer += (i,)
    return answer


def subStringMatchOneSub(key, target):
    """
    This function takes a key and target strings and returns a tuple for starting points (indexes) of matches of key
    to target with one substitution including perfect matches.
    :param key: str
    :param target: str
    :return: tuple
    """
    allAnswers = ()
    for miss in range(0, len(key)):
        key1 = key[:miss]
        key2 = key[miss + 1:]
        match1 = subStringMatchExact(target, key1)
        match2 = subStringMatchExact(target, key2)
        filtered = constrainedMatchPair(match1, match2, len(key1))
        allAnswers = allAnswers + filtered
    return allAnswers


# Problem 4

def subStringMatchExactlyOneSub(target, key):
    """
    This function takes a target and key strings and returns a tuple for starting points (indexes) of matches of key
    to target with one substitution excluding perfect matches.
    :param target: str
    :param key: str
    :return: tuple
    """
    all_answer = subStringMatchOneSub(key, target)
    perfect_matches = subStringMatchExact(target, key)
    result = ()
    for i in range(len(all_answer)):
        if all_answer[i] not in perfect_matches: result += (all_answer[i],)
    return result


for target, key in pairs:
    print('With Perfect Matches', subStringMatchOneSub(key, target))
    print('Without Perfect Matches', subStringMatchExactlyOneSub(target, key))
