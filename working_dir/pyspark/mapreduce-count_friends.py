from pyspark.sql import SparkSession
import time

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("CountFriends") \
    .getOrCreate()

# Path to the input file
input_file = "datasets/undirected_graph.txt"

# Start the timer for wall time
start_time = time.time()

# Measure time for reading the file
read_start_time = time.time()
edges_rdd = spark.sparkContext.textFile(input_file)
read_end_time = time.time()

# Measure time for processing edges
process_start_time = time.time()
# Parse edges and count friends
friend_counts_rdd = (
    edges_rdd.flatMap(lambda line: line.split(","))  # Split each line into node pairs
    .map(lambda node: (int(node), 1))               # Map each node to (node, 1)
    .reduceByKey(lambda a, b: a + b)                # Reduce by key to count friends
)
process_end_time = time.time()

# Measure time for collecting results
collect_start_time = time.time()
friend_counts = friend_counts_rdd.collect()
collect_end_time = time.time()

# Print the results
print("Number of friends for each node:")
for node, count in sorted(friend_counts):
    print(f"Node {node}: {count} friends")

# End the timer for wall time
end_time = time.time()

# Calculate and print timing details
wall_time = end_time - start_time
read_time = read_end_time - read_start_time
process_time = process_end_time - process_start_time
collect_time = collect_end_time - collect_start_time

print("\n--- Runtime Statistics ---")
print(f"Wall time (total script execution): {wall_time:.2f} seconds")
print(f"Time taken to read the file: {read_time:.2f} seconds")
print(f"Time taken to process edges: {process_time:.2f} seconds")
print(f"Time taken to collect results: {collect_time:.2f} seconds")

# Stop the Spark session
spark.stop()