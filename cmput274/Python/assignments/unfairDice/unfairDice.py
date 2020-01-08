# ---------------------------------------------------
#    Name: Darius Fang
#    ID: 1570975
#    CMPUT 274, Fall  2019
#
#    Weekly Assignment 2: Unfair Dice
#    Citation: docs.python.random module libraries
# ---------------------------------------------------
import random


def biased_rolls(prob_list, s, n):
    """ Simulate n rolls of a biased m-sided die and return
    a list containing the results.

    Arguments:
        prob_list: a list of the probabilities of rolling the
                   number on each side of the m-sided die. The list
                   will always have the length m (m >= 2), where m is
                   the number of sides numbered 1 to m. Therefore,
                   for example, the probability stored at index 0 in
                   the list is the probability of rolling a 1 on
                   the m-sided die.
        s: the seed to use when initializing the PRNG
        n: the number of rolls to return

    Return:
        rolls: a list (of length n) containing each of the n rolls of the
               biased die, in the order they were generated.
    """
    rolls = []
    random.seed(s)

    for roll in range(n):
        num = random.random()
        compare = 0
        i = 0

        while compare < num:
            compare = compare + prob_list[i]
            i += 1

        rolls.append(i)

    return rolls


def draw_histogram(m, rolls, width):
    """ Draws a frequency histogram of the rolls of an m-sided die
    mapped to a fixed width.

    Arguments:
        m (int): the number of sides on the die
        rolls (list): the list of rolls generated by the biased die
        width (int): the fixed width of the histogram, in characters
                     (this is the length of the longest bar in the
                     histogram, to maximize space in the chart)

    Returns:
        None (but prints the histogram to standard output)
    """
    sideval = {}
    for i in range(m):
        sideval[i + 1] = rolls.count(i+1)

    maxVal = max(sideval.values())
    for n in range(m):
        line = str(n+1) + ":"
        length = round(sideval[n + 1]*width/maxVal)

        for l in range(width):
            if length <= l:
                line = line + "."

            else:
                line = line + "*"

        print(line)


if __name__ == "__main__":
    rolls = biased_rolls([1/4, 1/6, 1/12, 1/12, 1/4, 1/6], 42, 200)
    print(rolls)
    draw_histogram(6, rolls, 10)