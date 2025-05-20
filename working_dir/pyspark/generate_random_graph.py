import random

# Parameters
num_nodes = 1000
num_edges = 5000  # Adjust the number of edges as needed
output_file = "datasets/undirected_graph.txt"

# Generate random edges
edges = set()
while len(edges) < num_edges:
    # Randomly select two nodes
    a = random.randint(1, num_nodes)
    b = random.randint(1, num_nodes)
    # Ensure no self-loops and no duplicate edges
    if a != b:
        edge = tuple(sorted((a, b)))  # Sort to ensure undirected edge representation
        edges.add(edge)

# Save edges to a text file
with open(output_file, "w") as file:
    for edge in edges:
        file.write(f"{edge[0]},{edge[1]}\n")

print(f"Undirected graph with {num_nodes} nodes and {len(edges)} edges saved to {output_file}")