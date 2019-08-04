'''
A PERMUTATION is an arrangement of all or part of a set of objects,
with regard to the order of the arrangement.

factorial formula: n(n-1)(n-2)...(n-r+1)
permutation formula: n!/(n - r)!
'''


def factorial_of(n):
    '''
    multiplies a number by every number below it.

    CONSTANT: if n == 0, this function returns 1 by definition
    '''
    answer = n
    counter = 1
    if n == 0:
        return 1  # 0! is equal to 1 by definition
    while n > 1:
        if (n-counter) == 1:
            break
        answer *= (n - counter)
        counter += 1
    return answer


def permutation(n, r):
    '''
    n is the number of objects
    r is the number of positions

    FORMULA: n!/(n-r)!
    '''
    return factorial_of(n)/factorial_of(n-r)


print('The answer is: {}'.format(factorial_of(4)))
print('The answer is: {}'.format(permutation(24, 4)))
