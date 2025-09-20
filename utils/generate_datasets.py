import os
import random

def generate_dataset(size, output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"sample_{size}.txt")
    with open(filepath, "w") as f:
        for _ in range(size):
            f.write(f"{random.randint(0, 1000000)}\n")
    print(f"Dataset generated: {filepath}")

if __name__ == "__main__":
    sizes = [10000, 25000, 50000, 75000, 100000]
    for size in sizes:
        generate_dataset(size)
