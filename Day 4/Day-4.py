from pathlib import Path
import itertools
import re

# TODO: clean up with regexes 

[min_range, max_range] = map(int, Path('./Day 4/Day-4-Input.txt').read_text().split('-'))


# Part 1
valid_numbers = []
for i in range(min_range, max_range):
    digit_list = [int(d) for d in str(i)]
    current_digit = digit_list[0]
    sorted = True
    has_double_digit = False
    for digit in digit_list[1:]:
        if digit < current_digit:
            sorted = False
            break
        elif digit == current_digit:
            has_double_digit = True
        else:
            current_digit = digit
    if sorted is True and has_double_digit is True:
        valid_numbers.append(i)

#print(f'Part 1: {len(valid_numbers)}')

# Part 2
valid_double_numbers = []
for i in valid_numbers:
    digit_list = [int(d) for d in str(i)]
    current_digit = digit_list[0]
    duplicate_counter = 1
    has_double_digit = False
    for digit in digit_list[1:]:
        if digit == current_digit:
            duplicate_counter += 1
        elif duplicate_counter == 2:
            current_digit = digit
            has_double_digit = True
        else:
            current_digit = digit
            duplicate_counter = 1
    if has_double_digit is True or duplicate_counter == 2:
        valid_double_numbers.append(i)

print(len(valid_double_numbers))

#(^|(?<!\1))(\d)\1{1}((?!\1)|$)
