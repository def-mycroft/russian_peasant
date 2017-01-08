"""Simple implementation of Russian Peasant Multiplication

Russian Peasant Multiplication is a way to multiply two numbers.

https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication#Russian_peasant_multiplication

I first discovered Russian Peasant Multiplication in Combinatorics by Cameron.

https://www.amazon.com/Combinatorics-Techniques-Algorithms-Peter-Cameron/dp/0521457610

I wrote a function while working on proving Russian Peasant Multiplication.


"""
def generate_columns(number_1, number_2, length=500):
    """Generates the two columns using an index"""
    index = [2]
    left_side = [number_1]
    right_side = [number_2]

    # The index is a list of integers with each member being twice the 
    # previous member.
    for i in range(1,length):
        # This index would need to be larger for operations involving
        # larger numbers.
        n = index[i-1] * 2
        index.append(n)

    for i in range(len(index)):
        # Divide the first number by the index member and return floor.
        x = int(number_1 / index[i])
        left_side.append(int(x))
        # Append the second number times the index member.
        right_side.append((index[i] * number_2))

        # Stop when the left side reaches 1.
        if x <= 1:
            break

    return left_side, right_side


def peasant(number_1, number_2, length=500, verbose=False):
    """Removes values from the right side where the left is even"""
    left_side, right_side = generate_columns(number_1, number_2)

    subtract_values = []

    for x in left_side:

        if x % 2 == 0:
            index = left_side.index(x)
            subtract_values.append(right_side[index])

    if not verbose:
        return sum(right_side) - sum(subtract_values)

    else:
        return sum(right_side) - sum(subtract_values), left_side, right_side, subtract_values
