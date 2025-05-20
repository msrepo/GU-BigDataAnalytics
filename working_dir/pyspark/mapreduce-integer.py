from pyspark.sql import SparkSession
import time

# Start the timer for wall time
start_time = time.time()

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("FindLargestAndAverage") \
    .getOrCreate()

# Path to the text file
file_path = "datasets/LargeInteger-mapreduce.txt"

# Read the text file into an RDD
read_start_time = time.time()
numbers_rdd = spark.sparkContext.textFile(file_path)
read_end_time = time.time()

# Convert each line to an integer
map_start_time = time.time()
integers_rdd = numbers_rdd.map(lambda x: int(x))
map_end_time = time.time()

# Find the largest integer
reduce_start_time = time.time()
largest_integer = integers_rdd.max()
reduce_end_time = time.time()

# Calculate the average of all integers
sum_start_time = time.time()
total_sum = integers_rdd.sum()
count = integers_rdd.count()
average = total_sum / count
sum_end_time = time.time()

# the same set of integers, but with each integer appearing only once
collect_start_time = time.time()
unique_integers = integers_rdd.distinct().collect()
collect_end_time = time.time()

# the count of number of distinct integers in the input
distinct_count = len(unique_integers)

# End the timer for wall time
end_time = time.time()

# Print the results
print(f"Largest Integer: {largest_integer}")
print(f"Average of Integers: {average}")
print(f"Unique Integers: {unique_integers[:10]}...")  # Print first 10 unique integers for brevity
print(f"Count of Distinct Integers: {distinct_count}")

# Stop the Spark session
spark.stop()

# Calculate and print timing details
wall_time = end_time - start_time
read_time = read_end_time - read_start_time
map_time = map_end_time - map_start_time
reduce_time = reduce_end_time - reduce_start_time
sum_time = sum_end_time - sum_start_time

print("\n--- Profiling Details ---")
print(f"Wall time (total script execution): {wall_time:.2f} seconds")
print(f"Time taken to read the file: {read_time:.2f} seconds")
print(f"Time taken for map operation: {map_time:.2f} seconds")
print(f"Time taken for reduce operation (max): {reduce_time:.2f} seconds")
print(f"Time taken for sum and count operations: {sum_time:.2f} seconds")