"""
Consider the digit halfway around the circular list.
That is, if your list contains 10 items,
only include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
Fortunately, your list has an even number of elements.
"""

def sum_expected_digits(path):
    try:
        with open(path, 'r') as file:
            digits = list(file.read())
            digits = list(map(int, digits))
            digits_to_summary = []
            digits_len = len(digits)
            steps_forward_to_compare = (digits_len//2)
            for index, digit in enumerate(digits):
                index_to_compare = (index+steps_forward_to_compare)%digits_len
                if digit == digits[index_to_compare]:
                    digits_to_summary.append(digit)
    except EOFError as err:
        exit(err)
    return sum(digits_to_summary)


if __name__ == "__main__":
    print(sum_expected_digits('./input2.txt'))