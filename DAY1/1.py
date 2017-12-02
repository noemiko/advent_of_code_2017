"""
Find the sum of all digits that match the next digit in the list.
The list is circular, so the digit after the last digit is the first digit in the list.
"""

def sum_digits_where_next_digit_is_the_same(path):
    try:
        with open(path, 'r') as file:
            digits = file.read()
            numbers_to_summary = []
            before_digit = None
            for digit in digits:
                digit = int(digit)
                if before_digit == digit:
                    numbers_to_summary.append(before_digit)
                before_digit = digit
            if digits[0] == digits[-1]:
                numbers_to_summary.append(int(digits[-1]))
    except EOFError as err:
        exit(err)
    return sum(numbers_to_summary)


if __name__ == "__main__":
    print(sum_digits_where_next_digit_is_the_same('./input1.txt'))