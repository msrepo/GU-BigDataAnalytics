from pyspark.sql import SparkSession
import json
import time

# Start the timer for wall time
start_time = time.time()

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Path to the text file
file_path = "datasets/LargeText-wordcount/TheAdventuresOfTomSawyer_MarkTwain_English.txt"

# Read the text file into an RDD
text_rdd = spark.sparkContext.textFile(file_path)

# Start profiling for the map operation
map_start_time = time.time()
mapped_rdd = text_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1))
map_end_time = time.time()

# Start profiling for the reduce operation
reduce_start_time = time.time()
word_counts = mapped_rdd.reduceByKey(lambda a, b: a + b)
reduce_end_time = time.time()

# Collect the results
collect_start_time = time.time()
word_counts_dict = dict(word_counts.collect())
collect_end_time = time.time()

# Save the results to a JSON file
output_file = "word_counts.json"
with open(output_file, "w") as json_file:
    json.dump(word_counts_dict, json_file)

print(f"Word counts saved to {output_file}")

# Stop the Spark session
spark.stop()

# End the timer for wall time
end_time = time.time()

# Calculate and print timing details
wall_time = end_time - start_time
map_time = map_end_time - map_start_time
reduce_time = reduce_end_time - reduce_start_time
collect_time = collect_end_time - collect_start_time

print("\n--- Profiling Details ---")
print(f"Wall time (total script execution): {wall_time:.2f} seconds")
print(f"Time taken for map operation: {map_time:.2f} seconds")
print(f"Time taken for reduce operation: {reduce_time:.2f} seconds")
print(f"Time taken for collect operation: {collect_time:.2f} seconds")