import fileinput
from collections import deque

orbit_mapping = {}
for orbit in fileinput.input('./Day 6/Day-6-Input.txt'):
    a, b = orbit.replace('\n', '').split(')')
    orbit_mapping[b] = a

# Part 1
sum = 0
for orbit in orbit_mapping:
    current = orbit
    while current in orbit_mapping:
        current = orbit_mapping[current]
        sum += 1
print(f'Part 1: {sum}')

# Part 2
my_path = deque()
santa_path = deque()
current = orbit_mapping['YOU']
while current in orbit_mapping:
    current = orbit_mapping[current]
    my_path.appendleft(current)

current = orbit_mapping['SAN']
while current in orbit_mapping:
    current = orbit_mapping[current]
    santa_path.appendleft(current)

i = 0
while my_path[i] is santa_path[i]:
    i += 1

print(f'Part 2: {len(santa_path) + len(my_path) - (2 * i)}')