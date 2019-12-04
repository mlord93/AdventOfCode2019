import fileinput
import itertools
import math

unchanged_input = list(map(int, fileinput.input('./Day-2-Input.txt')[0].split(',')))

def get_program_output(noun, verb):
    program_array = unchanged_input.copy()
    program_array[1] = noun
    program_array[2] = verb
    i = 0
    while i < len(program_array) + 3 and program_array[i] is not 99:
        a, b, c = program_array[i + 1 : i + 4]
        if program_array[i] is 1:
            program_array[c] = program_array[a] + program_array[b]
        elif program_array[i] is 2:
            program_array[c] = program_array[a] * program_array[b]
        else:
            print(f'Error: Opcode {program_array[i]} does not exist')
        i += 4
    return program_array[0]

# Part 1
print(f'Part 1: {get_program_output(12, 2)}')

# Part 2
for (i, j) in itertools.product(range(100), repeat=2):
    if get_program_output(i, j) == 19690720:
        print(f'Part 2: {100 * i + j}')
        break
