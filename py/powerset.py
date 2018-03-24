# CS350 Spring 2018 Seth Lewis

"""
    Since elements of Python sets must be immutable,
    a Python set cannot contain Python sets.
    For example, a power set cannot be represented using Python sets.

    So we will simulate a set using lists.
    For example, [[1,2], [1,3]] represents the set {{1,2}, {1,3}}.
    This works, since lists do not have the immutability constraint.
"""

import random


def randomSet(n, up):
    """Build a random 'set' of integers.

    Be sure to guarantee the key property of a set: no duplicates.

    >>> randomSet(4, 10)
    [5, 3, 2, 8]

    Params: 
        n (int): # of integers in the set
        up (int): upperbound 
    Returns: (list) random 'set' of n integers between 0 and up, inclusive
    """

    # A = random.sample(range(up), n)
    L = []
    end_list = 0
    while end_list < n:  # repeats do not create shorter sets
        number = random.randint(0, up)
        if number not in L:  # equivalent to "if x != number for all x in L then true"
            end_list += 1
            L.append(number)

    '''
    for x in range(n):  # repeats will lead to shorter sets
        number = random.randint(0, up)
        if number not in L:
            L.append(number)
    '''

    return L


def powerSet(A):
    """Build the power set of A.

    >>> powerSet ([1,2])
    [[], [1], [2], [1,2]]
    
    Params: A (list): set of integers, represented internally as a list
    Returns: (list) powerset of A, represented internally as a list
    """

    if len(A) == 0:  # base case returns power set of empty set could also use A == [] for conditional
        return [[]]
    else:
        partial = powerSet(A[1:])  # recursive call new list A[1] to len(A) eventually reach list with single element
        # print(partial)  # print for trace
        L = []  # initialize empty list to contain part of power set of A
        for x in partial:
            # print(A[0])  # print for trace: can see exponential growth of calls here
            L.append([A[0]] + x)  # union {A[0]} and subset of partial: new set includes subsets containing A[0]
            # print(L)  # print for trace
            # print(L + partial)  # print for trace
    return L + partial  # union combines all subsets into power set current A until is full power set of A in final call


def printSet(L):
    """Print a 'set', using standard set notation.
    To restore the correct interpretation, this function prints the 'set'
    in true set notation.
    Hint: you can print without adding a newline (see print documentation)

    >>> printSet ([[1,2], [1,3]])
    {{1,2}, {1,3}}
    
    Params: A (list): set of integers
    """

    L.sort()  # added for fun and for clarity
    string = str(L)  # replace is for strings = "aha! moment"

    def replaceCharacter(s):  # could not figure out how to work on lists then discovered python has inner function
        if len(s) == 0:
            return ''
        if s[0] == '[':
            return '{' + replaceCharacter(s[1:])
        if s[0] == ']':
            return '}' + replaceCharacter(s[1:])
        return s[0] + replaceCharacter(s[1:])

    print(replaceCharacter(string))

    '''
    L.sort()  # added for fun and clarity
    print(str(L).replace("[", "{").replace("]", "}"))
    '''

    return


# an example of a test call
A = randomSet(5, 100)
# print (A)
print("The power set of ")
printSet(A)
print("is")
B = powerSet(A)
printSet(B)
print("of size " + str(len(B)))  # sanity check: should be 2^5 = 32
