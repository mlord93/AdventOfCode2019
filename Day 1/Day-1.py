import fileinput
import math

def get_fuel_from_mass(mass):
    return math.floor(mass / 3) - 2

# Part 1
sum = 0
for module_mass in fileinput.input('./Day 1/Day-1-Input.txt'):
    sum += get_fuel_from_mass(int(module_mass))
print(f'Part 1 sum: {sum}')

# Part 2
sum = 0
for module_mass in fileinput.input('./Day 1/Day-1-Input.txt'):
    additional_fuel = get_fuel_from_mass(int(module_mass))
    while additional_fuel > 0:
        sum += additional_fuel
        additional_fuel = get_fuel_from_mass(additional_fuel)
print(f'Part 2 sum: {sum}')
