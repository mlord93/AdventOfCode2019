import fileinput
import math

instructions = list(map(int, fileinput.input(
    './Day 5/Day-5-Input.txt')[0].split(',')))


def get_program_output(program_input, program_array):
    i = 0
    output = 0
    while i < len(program_array) and program_array[i] is not 99:
        if output != 0:
            return f'ERROR: UNEXPECTED OUTPUT {output}'
        op_code = program_array[i] % 100

        if op_code == 1:
            parameters, parameter_modes = get_parameters(program_array, i, 3)
            program_array[parameters[2]] = (parameters[0] if parameter_modes[0] == 1 else program_array[parameters[0]]) + (
                parameters[1] if parameter_modes[1] == 1 else program_array[parameters[1]])
            i += 4
        elif op_code == 2:
            parameters, parameter_modes = get_parameters(program_array, i, 3)
            program_array[parameters[2]] = (parameters[0] if parameter_modes[0] == 1 else program_array[parameters[0]]) * (
                parameters[1] if parameter_modes[1] == 1 else program_array[parameters[1]])
            i += 4
        elif op_code == 3:
            parameters, parameter_modes = get_parameters(program_array, i, 2)
            program_array[parameters[0]] = program_input
            i += 2
        elif op_code == 4:
            parameters, parameter_modes = get_parameters(program_array, i, 2)
            output = (parameters[0] if parameter_modes[0] == 1 else program_array[parameters[0]])
            i += 2
        elif op_code == 5:
            # Jump if true
            parameters, parameter_modes = get_parameters(program_array, i, 2)
            if ((parameters[0] if parameter_modes[0] == 1 else program_array[parameters[0]])) != 0:
                i = (parameters[1] if parameter_modes[1] ==
                     1 else program_array[parameters[1]])
            else:
                i += 3
        elif op_code == 6:
            # Jump if false
            parameters, parameter_modes = get_parameters(program_array, i, 2)
            if ((parameters[0] if parameter_modes[0] == 1 else program_array[parameters[0]])) == 0:
                i = (parameters[1] if parameter_modes[1] ==
                     1 else program_array[parameters[1]])
            else:
                i += 3
        elif op_code == 7:
            # Less than
            parameters, parameter_modes = get_parameters(program_array, i, 3)
            if ((parameters[0] if parameter_modes[0] == 1 else program_array[parameters[0]])) < ((parameters[1] if parameter_modes[1] == 1 else program_array[parameters[1]])):
                program_array[parameters[2]] = 1
            else:
                program_array[parameters[2]] = 0
            i += 4
        elif op_code == 8:
            # Equal to 
            parameters, parameter_modes = get_parameters(program_array, i, 3)
            if ((parameters[0] if parameter_modes[0] == 1 else program_array[parameters[0]])) == ((parameters[1] if parameter_modes[1] == 1 else program_array[parameters[1]])):
                program_array[parameters[2]] = 1
            else:
                program_array[parameters[2]] = 0
            i += 4
        else:
            return f'Error: Opcode {program_array[i]} does not exist'

    return f'OUTPUT: {output}'

def get_parameters(program_array, start, num_parameters):
    parameter_modes = []
    parameters = program_array[start + 1: start + num_parameters + 1]
    for idx in range(num_parameters):
        parameter_modes.append(math.floor(
            program_array[start] / math.pow(10, idx + 2)) % 10)
    return (parameters, parameter_modes)

def extract_param():
    print('TODO: create function to get a single param given its mode')


print(f'Part 1: {get_program_output(1, instructions.copy())}')
print(f'Part 2: {get_program_output(5, instructions.copy())}')


