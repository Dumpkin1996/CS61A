"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.
"""

TEAM_NAME = 'ZTH&HYQ' 

GOAL_SCORE = 100

from dice import four_sided, six_sided, make_test_dice

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    num_rolled, sequence, result = 0, [], 0
    while num_rolled < num_rolls:
        x = dice()
        num_rolled += 1
        sequence += [x]
        result += x
    if 1 in sequence:
        return 1
    else:
        return result
    # END PROBLEM 1

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    a = opponent_score//10
    b = opponent_score-(10*a)
    return max(a,b)+1
    # END PROBLEM 2

def is_prime(x):
    """Check whether a number is a prime or not.
    >>> is_prime(6)
    False
    >>> is_prime(9)
    False
    >>> is_prime(7)
    True
    """
    if x == 1:
        return False
    else:
        i = 2
        while i < x:
            if x%i == 0:
                return False
            else:
                i += 1
        return True

def next_prime(x):
    """Return the next larger prime number of x.
    >>> next_prime(5)
    7
    >>> next_prime(11)
    13
    >>> next_prime(19)
    23
    """
    y = x+1
    while not is_prime(y):
        y += 1
    return y

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if num_rolls == 0:
        result = free_bacon(opponent_score)
    else:
        result = roll_dice(num_rolls, dice)
    if is_prime(result):
        result = next_prime(result)
    return result
    # END PROBLEM 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog Wild).
    """
    # BEGIN PROBLEM 3
    x = score + opponent_score
    if x%7 == 0:
        dice = four_sided
    else:
        dice = six_sided
    return dice
    # END PROBLEM 3

def max_dice(score, opponent_score):
    """Return the maximum number of dice the current player can roll. The
    current player can roll at most 10 dice unless the sum of SCORE and
    OPPONENT_SCORE ends in a 7, in which case the player can roll at most 1.
    """
    # BEGIN PROBLEM 3
    x = score + opponent_score
    y = x - 10*(x//10)
    if y == 7:
         max_dice = 1
    else:
        max_dice = 10
    return max_dice
    # END PROBLEM 3

def is_swap(score):
    """Returns whether the SCORE contains only one unique digit, such as 22.
    """
    # BEGIN PROBLEM 4
    a = score//100
    b = (score-100*a)//10
    c = score - 100*a - 10*b
    if a == 0:
        return b == 0 or b == c
    else:
        return a == b == c 
    # END PROBLEM 4

def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while max(score0, score1) < goal:
        if player == 0:
            dice_this_turn = select_dice (score0, score1)
            max_dice_this_turn = max_dice (score0, score1)
            num_rolls0 = min (strategy0 (score0, score1), max_dice_this_turn)
            socre_this_turn0 = take_turn (num_rolls0, score1, dice_this_turn)
            score0 += socre_this_turn0
            if is_swap(score0):
                score0, score1 = score1, score0
        elif player == 1:
            dice_this_turn = select_dice (score1, score0)
            max_dice_this_turn = max_dice (score1, score0)
            num_rolls1 = min (strategy1 (score1, score0), max_dice_this_turn)
            socre_this_turn1 = take_turn (num_rolls1, score0, dice_this_turn)
            score1 += socre_this_turn1
            if is_swap(score1):
               score0, score1 = score1, score0
        player = other(player)
    # END PROBLEM 5
    return score0, score1

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    @check_strategy
    def strategy(score, opponent_score):
        return n
    return strategy

def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid strategy
    output. All strategy outputs must be non-negative integers less than or
    equal to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls)'

def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the 
    strategy returns a valid input. Use `check_strategy_roll` to raise 
    an error with a helpful message if the strategy retuns an invalid 
    output.

    >>> always_roll_5 = always_roll(5)
    >>> always_roll_5 == check_strategy(always_roll_5)
    True
    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> fail_15_20 == check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (invalid number of rolls)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> fail_102_115 == check_strategy(fail_102_115)
    True
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    for score0 in range (0, goal):
        for score1 in range (0, goal):
            num_rolls_check = strategy (score0, score1)
            check_strategy_roll (score0, score1, num_rolls_check)
    # END PROBLEM 6
    return strategy

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7
    def gn(*args):
        i, sample_sum = 1, 0
        while i <= num_samples:
            i += 1
            sample_sum += fn(*args)
        return sample_sum/num_samples
    return gn
    # END PROBLEM 7

def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    max_ave, num_maximizing_ave = 0, 0
    for x in range (1,11):
        ave = make_averaged(roll_dice, num_samples)(x, dice)
        if ave > max_ave:
            max_ave = ave
            num_maximizing_ave = x
    return num_maximizing_ave
    # END PROBLEM 8

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

@check_strategy
def bacon_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    dice_this_turn = select_dice (score, opponent_score)
    free_bacon_expectation = take_turn (0, opponent_score, dice_this_turn)
    if free_bacon_expectation >= margin:
        return 0
    return num_rolls  # Replace this statement
    # END PROBLEM 9

@check_strategy
def swap_strategy(score, opponent_score, margin=5, num_rolls=6):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and doesn't trigger a
    swap. Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    dice_this_turn = select_dice (score, opponent_score)
    zero_result = take_turn (0, opponent_score, dice_this_turn)
    if is_swap(score + zero_result):
    	zero_result = opponent_score - (score + zero_result)
    	if zero_result > 0:
    		return 0
    elif zero_result >= margin:
        return 0
    return num_rolls  # Replace this statement
    # END PROBLEM 10

@check_strategy
def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 10
    dice_this_turn = select_dice (score, opponent_score)

    zero_result = take_turn (0, opponent_score, dice_this_turn)

    if dice_this_turn == four_sided:
    	return swap_strategy (score, opponent_score, 4, 4)

    else:
    	if score - opponent_score >= 8:
    		x = score + opponent_score + zero_result 
    		if x % 7 == 0 and x%10 == 7:
    			return 0
    		return swap_strategy (score, opponent_score, 6, 6)
    	elif score - opponent_score >= 0:
    		return swap_strategy (score, opponent_score, 7, 7) 
    	elif score - opponent_score <= -8:
    		return swap_strategy (score, opponent_score, 10, 9)
    	elif score - opponent_score < 0:
    		return swap_strategy (score, opponent_score, 9, 8)

    # END PROBLEM 10