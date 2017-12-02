"""
Find the sum of all digits that match the next digit in the list.
The list is circular, so the digit after the last digit is the first digit in the list.
"""


def sum_digits_where_next_digit_is_the_same(path):
    try:
        with open(path, 'r') as file:
            digits = list(map(int, file.read()))
            digits_to_summary = []
            digits_len = len(digits)
            for index, digit in enumerate(digits):
                index_to_compare = (index+1) % digits_len
                if digit == digits[index_to_compare]:
                    digits_to_summary.append(digit)
    except EOFError as err:
        exit(err)
    return sum(digits_to_summary)

if __name__ == "__main__":
    print(sum_digits_where_next_digit_is_the_same('./input1.txt'))