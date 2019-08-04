import math


'''
    If E(sub 1) is an experiment with n(sub 1) outcomes
    and E(sub 2) is an experiment with n(sub 2) outcomes,
    then the experiment which consists of performing E(sub 1) first
    and then E(sub 2) consists of n(sub 1) * n(sub 2) possible outcomes.
'''


def toss_coin_outcome(numberOfCoins=1):
    '''
    Example of finding all possible outcomes of a
    coin * numberOfCoin.

    CONSTANT: number of possible outcomes of 1 coin == 2
    '''
    answer = POSSIBLE_OUTCOME = 2  # Head and Tail
    while numberOfCoins > 1:
        numberOfCoins -= 1
        answer *= (POSSIBLE_OUTCOME)
    return answer


print('The answer is: {}'.format(toss_coin_outcome(3)))


def toss_coin_and_die_outcome(numberOfCoin=1, numberOfDice=1):
    '''
    Finding the number of possible outcomes of the rolling of a die
    and then tossing a coin.

    CONSTANTS: E(sub 1) == coin == 2 POSSIBLE OUTCOMES
               E(sub 2) == die  == 6 POSSIBLE OUTCOMES
    '''
    # shortcut for while loop is using the power function of math class
    return math.pow(2, numberOfCoin) * math.pow(6, numberOfDice)


print('The answer is: {}'.format(toss_coin_and_die_outcome(1, 2)))
