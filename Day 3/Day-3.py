import fileinput

def build_wire_path(instructions):
    instruction_list = instructions.split(',')
    wire_path = dict()
    current_point = (0, 0)
    step_count_from_origin = 0
    for instruction in instruction_list:
        direction = instruction[0]
        for i in range(int(instruction[1:])):
            step_count_from_origin += 1
            if direction is 'R':
                current_point = (current_point[0] + 1, current_point[1])
            if direction is 'L':
                current_point = (current_point[0] - 1, current_point[1])
            if direction is 'U':
                current_point = (current_point[0], current_point[1] + 1)
            if direction is 'D':
                current_point = (current_point[0], current_point[1] - 1)
            if current_point not in wire_path:
                wire_path[current_point] = step_count_from_origin
    return wire_path

[wire_1, wire_2] = fileinput.input('./Day-3-Input.txt')
wire_1_path = build_wire_path(wire_1)
wire_2_path = build_wire_path(wire_2)
intersection_set = set(wire_1_path.keys()) & set(wire_2_path.keys())

# Part 1
intersection_distances = []
for coordinate in intersection_set:
    intersection_distances.append(abs(coordinate[0]) + abs(coordinate[1]))
print(f'Part 1: {min(intersection_distances)}')

# Part 2
intersection_step_distances = []
for coordinate in intersection_set:
    intersection_step_distances.append(wire_1_path[coordinate] + wire_2_path[coordinate])
print(f'Part 2: {min(intersection_step_distances)}')