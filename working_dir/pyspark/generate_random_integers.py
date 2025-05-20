import random

# Path to the output file
output_file = "datasets/LargeInteger-mapreduce.txt"

# Generate 100,000 random integers and write them to the file
with open(output_file, "w") as file:
    for _ in range(100000):  # Generate 100,000 integers
        random_integer = random.randint(1, 1000000)  # Generate a random integer between 1 and 1,000,000
        file.write(f"{random_integer}\n")

print(f"100,000 random integers saved to {output_file}")