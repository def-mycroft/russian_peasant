"""Simple implementation of Russian Peasant Multiplication

Russian Peasant Multiplication is a way to multiply two numbers.

https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication#Russian_peasant_multiplication

I first discovered Russian Peasant Multiplication in Combinatorics by Cameron.

https://www.amazon.com/Combinatorics-Techniques-Algorithms-Peter-Cameron/dp/0521457610

I wrote a function while working on proving Russian Peasant Multiplication.


"""
def peasant_v2(number_1, number_2):
    """The most concise implementation of RPM I've create so far"""
    column = [number_1]
    index = 2
    answer = 0

    while int(number_1 / index) != 1:
        column.append(int(number_1 / index))
        index *= 2

    for i in column:
        if i % 2 != 0:
            answer += number_2 * (2 ** column.index(i))

    return answer


def generate_columns(number_1, number_2):
    """Generates the two columns using an index"""
    left_side = [number_1]
    right_side = [number_2]
    remainder_bool = []
    index = 2 # Start the index at 2.
    stop_flag = False

    while not stop_flag:
        # Divide the first number by the index member and return floor.
        x = int(number_1 / index)

        left_side.append(int(x))

        # Append the second number times the index member.
        right_side.append((index * number_2))

        index *= 2

        # Stop when the left side reaches 1.
        if x <= 1:
            stop_flag = True

    for i in range(len(left_side)):
        if left_side[i] % 2 == 0:
            remainder_bool.append(0)
        else:
            remainder_bool.append(1)

    return left_side, right_side, remainder_bool



def peasant(number_1, number_2, verbose=False):
    """Removes values from the right side where the left is even"""
    left_side, right_side, remainder_bool = generate_columns(number_1, number_2)

    subtract_values = []

    for x in left_side:

        if x % 2 == 0:
            index = left_side.index(x)
            subtract_values.append(right_side[index])

    if not verbose:
        return sum(right_side) - sum(subtract_values)

    else:
        string = ''
        for i in remainder_bool:
            string = string + str(i)
        string = string[::-1]
        print('binary: %s decimal: %s' % (string, int(string, 2)))
        check = number_1 == int(string, 2)
        print('remainder bool == number_1: %s' % check)
        print(subtract_values)
        answer = sum(right_side) - sum(subtract_values) 
        #left_side, right_side, subtract_values
        print('answer: %s' % answer)
        print('columns:')
        for i in range(len(left_side)):
            print('%s    %s    %s' % (left_side[i], right_side[i], remainder_bool[i]))
