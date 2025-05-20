import random
from collections import defaultdict

'''

This script implements a simplified version of Locality Sensitive Hashing (LSH) for binary vectors.
It generates random binary vectors, applies LSH to hash them into buckets, and finds candidate pairs.


Explanation:
Binary Vectors:

The script generates random binary vectors for demonstration purposes. You can replace this with your actual dataset.
Hash Function:

Each hash function is defined by a random hyperplane (a vector of random values).
The hash value is determined by the dot product of the input vector and the hyperplane.
Bands and Buckets:

The hash functions are divided into bands, and each band hashes the vectors into buckets.
Vectors that hash to the same bucket in at least one band are considered candidates.
Candidate Pairs:

Candidate pairs are identified as pairs of vectors that share at least one bucket in any band.
Parameters:

num_hash_functions: Total number of hash functions.
num_bands: Number of bands to divide the hash functions into.

Example output:
Vectors:
Vector 0: [1, 0, 1, 1, 0, 1, 0, 1]
Vector 1: [0, 1, 0, 1, 1, 0, 1, 0]
...

Hash Tables:
Band 0:
  Bucket (1, 0): [0, 3]
  Bucket (0, 1): [1, 2]
...

Candidate Pairs:
(0, 3)
(1, 2)



'''
# Generate random binary vectors for demonstration
def generate_random_binary_vectors(num_vectors, vector_size):
    return [[random.randint(0, 1) for _ in range(vector_size)] for _ in range(num_vectors)]

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

    return hash_tables

# Find candidate pairs
def find_candidate_pairs(hash_tables):
    candidate_pairs = set()
    for band_index, hash_table in enumerate(hash_tables):
        for bucket in hash_table.values():
            if len(bucket) > 1:
                # Add all pairs of indices in the bucket
                for i in range(len(bucket)):
                    for j in range(i + 1, len(bucket)):
                        candidate_pairs.add((bucket[i], bucket[j]))
    return candidate_pairs

# Example usage
if __name__ == "__main__":
    # Parameters
    num_vectors = 10
    vector_size = 8
    num_hash_functions = 6
    num_bands = 3

    # Generate random binary vectors
    vectors = generate_random_binary_vectors(num_vectors, vector_size)
    print("Vectors:")
    for i, vector in enumerate(vectors):
        print(f"Vector {i}: {vector}")

    # Perform LSH
    hash_tables = locality_sensitive_hashing(vectors, num_hash_functions, num_bands)

    # Print hash tables
    print("\nHash Tables:")
    for band_index, hash_table in enumerate(hash_tables):
        print(f"Band {band_index}:")
        for bucket, indices in hash_table.items():
            print(f"  Bucket {bucket}: {indices}")

    # Find candidate pairs
    candidate_pairs = find_candidate_pairs(hash_tables)
    print("\nCandidate Pairs:")
    for pair in candidate_pairs:
        print(pair)