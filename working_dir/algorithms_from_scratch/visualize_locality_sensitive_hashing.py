import random
import matplotlib.pyplot as plt
from collections import defaultdict

'''
This script visualizes Locality Sensitive Hashing (LSH) for 2D vectors.
It generates random 2D vectors, applies LSH to hash them into buckets, and visualizes the results.
The visualization will show:
- The original vectors in a 2D space.
- The hyperplanes used for hashing.
- The buckets formed by the hash functions.
Explanation:

- Vectors:
    The script generates random 2D vectors for demonstration purposes. You can replace this with your actual dataset.
- Hash Function:
    Each hash function is defined by a random hyperplane (a vector of random values).
    The hash value is determined by the dot product of the input vector and the hyperplane.
- Bands and Buckets:
    The hash functions are divided into bands, and each band hashes the vectors into buckets.
    Vectors that hash to the same bucket in at least one band are considered candidates.
- Candidate Pairs:
    Candidate pairs are identified as pairs of vectors that share at least one bucket in any band.
Parameters:
- num_hash_functions: Total number of hash functions.
- num_bands: Number of bands to divide the hash functions into.
Example output:
Vectors:
Vector 0: [0.5, -0.2]
Vector 1: [-0.3, 0.8]
...
Hash Tables:
Band 0:
  Bucket (1, 0): [0, 3]
  Bucket (0, 1): [1, 2]
Candidate Pairs:
(0, 3)
(1, 2)
'''

# Generate random 2D vectors for demonstration
def generate_random_2d_vectors(num_vectors):
    return [[random.uniform(-1, 1), random.uniform(-1, 1)] for _ in range(num_vectors)]

# Hash function for LSH
def hash_function(vector, random_hyperplane):
    # Compute the dot product of the vector and the hyperplane
    dot_product = sum(v * h for v, h in zip(vector, random_hyperplane))
    # Return 1 if dot product >= 0, else 0
    return 1 if dot_product >= 0 else 0

# Perform LSH
def locality_sensitive_hashing(vectors, num_hash_functions, num_bands):
    vector_size = len(vectors[0])
    hash_tables = [defaultdict(list) for _ in range(num_bands)]
    hyperplanes = [[random.uniform(-1, 1) for _ in range(vector_size)] for _ in range(num_hash_functions)]

    # Split hash functions into bands
    hash_functions_per_band = num_hash_functions // num_bands
    for vector_index, vector in enumerate(vectors):
        for band_index in range(num_bands):
            # Compute hash values for the current band
            start = band_index * hash_functions_per_band
            end = start + hash_functions_per_band
            band_hash = tuple(hash_function(vector, hyperplanes[i]) for i in range(start, end))
            # Add the vector index to the corresponding bucket
            hash_tables[band_index][band_hash].append(vector_index)

    return hash_tables, hyperplanes

# Visualize LSH
def visualize_lsh(vectors, hyperplanes, hash_tables):
    plt.figure(figsize=(10, 10))

    # Plot vectors
    for i, vector in enumerate(vectors):
        plt.scatter(vector[0], vector[1], label=f"Vector {i}")
        plt.text(vector[0], vector[1], f"{i}", fontsize=9, ha='right')

    # Plot hyperplanes
    for i, hyperplane in enumerate(hyperplanes):
        x = [-1, 1]
        y = [-(hyperplane[0] * x_val) / hyperplane[1] if hyperplane[1] != 0 else 0 for x_val in x]
        plt.plot(x, y, label=f"Hyperplane {i}", linestyle="--")

    # Annotate buckets
    for band_index, hash_table in enumerate(hash_tables):
        for bucket, indices in hash_table.items():
            if len(indices) > 1:
                bucket_center = [sum(vectors[i][0] for i in indices) / len(indices),
                                 sum(vectors[i][1] for i in indices) / len(indices)]
                # plt.text(bucket_center[0], bucket_center[1], f"Bucket {bucket}", fontsize=10, color="red")

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    # plt.legend()
    plt.title("Locality Sensitive Hashing (LSH) Visualization")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
    plt.show()

# Example usage
if __name__ == "__main__":
    # Parameters
    num_vectors = 10
    num_hash_functions = 4
    num_bands = 2

    # Generate random 2D vectors
    vectors = generate_random_2d_vectors(num_vectors)

    # Perform LSH
    hash_tables, hyperplanes = locality_sensitive_hashing(vectors, num_hash_functions, num_bands)

    # Visualize LSH
    visualize_lsh(vectors, hyperplanes, hash_tables)