import random

def generate_random_numbers_file(filepath, size):
    with open(filepath, 'w') as f:
        for _ in range(size):
            f.write(f"{random.randint(0, 1000000)}\n")

def read_numbers_from_file(filepath):
    with open(filepath, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]

def write_numbers_to_file(filepath, numbers):
    with open(filepath, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")
