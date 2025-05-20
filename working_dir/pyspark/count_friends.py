from collections import defaultdict
import time

# Path to the input file
input_file = "datasets/undirected_graph.txt"

# Start the timer for wall time
start_time = time.time()

# Dictionary to store the number of friends for each node
friend_counts = defaultdict(int)

# Measure time for reading the file
read_start_time = time.time()
with open(input_file, "r") as file:
    edges = file.readlines()
read_end_time = time.time()

# Measure time for processing edges
process_start_time = time.time()
for line in edges:
    # Parse the edge (a, b)
    a, b = map(int, line.strip().split(","))
    # Increment the friend count for both nodes
    friend_counts[a] += 1
    friend_counts[b] += 1
process_end_time = time.time()

# Measure time for printing results
print_start_time = time.time()
print("Number of friends for each node:")
for node, count in sorted(friend_counts.items()):
    print(f"Node {node}: {count} friends")
print_end_time = time.time()

# End the timer for wall time
end_time = time.time()

# Calculate and print timing details
wall_time = end_time - start_time
read_time = read_end_time - read_start_time
process_time = process_end_time - process_start_time
print_time = print_end_time - print_start_time

print("\n--- Runtime Statistics ---")
print(f"Wall time (total script execution): {wall_time:.2f} seconds")
print(f"Time taken to read the file: {read_time:.2f} seconds")
print(f"Time taken to process edges: {process_time:.2f} seconds")
print(f"Time taken to print results: {print_time:.2f} seconds")