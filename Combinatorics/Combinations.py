'''
A combination is a selection of all or part of a set of objects,
without regard to the order in which objects are selected.
Each possible selection would be an example of a combination.

derivation:

n(P)r = permutation

n(P)r = c(r(P)r)

c = n(P)r / r(P)r

c = n!/(n-r)!r! = combination

c = (n r)'
'''

"""
Example: How many committies of 2 chemists and 1 physicist
can be formed from 4 chemists and 3 physicists?
"""
from Permutation import factorial_of


def combination(n, r):
    '''
    Combination is similar to permutaion with the multiplication of r!
    in the divisor.

    formula: n! / ((n-r)! * r!)
    '''
    return factorial_of(n)/((factorial_of(n - r))*(factorial_of(r)))


print('The answer is: {}'.format(combination(4, 2) * combination(3, 1)))
