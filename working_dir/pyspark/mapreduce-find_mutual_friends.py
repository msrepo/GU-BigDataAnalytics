from pyspark.sql import SparkSession
from collections import defaultdict
import time
import json

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("FindMutualFriends") \
    .getOrCreate()

# Path to the input and output files
input_file = "datasets/cs246/hw1-bundle/q1/data/soc-LiveJournal1Adj.txt"
output_file = "working_dir/pyspark/output/mapreduce-mutual_friends.json"

# Start the timer for wall time
start_time = time.time()

# Read the file and parse the data
read_start_time = time.time()
lines_rdd = spark.sparkContext.textFile(input_file)

# Parse the data into (user, friends) pairs
user_friends_rdd = lines_rdd.map(lambda line: line.strip()) \
    .filter(lambda line: line and "\t" in line) \
    .map(lambda line: (int(line.split("\t")[0]), 
                       set(map(int, line.split("\t")[1].split(","))) if line.split("\t")[1] else set()))
read_end_time = time.time()

# Find the user with the most mutual friends for each user
process_start_time = time.time()

def find_mutual_friends(user_friends_pair):
    user, friends = user_friends_pair
    mutual_friend_counts = defaultdict(int)
    for friend in friends:
        for mutual_candidate in user_friends_broadcast.value.get(friend, set()):
            if mutual_candidate != user and mutual_candidate not in friends:
                mutual_friend_counts[mutual_candidate] += 1
    if mutual_friend_counts:
        best_match = max(mutual_friend_counts, key=mutual_friend_counts.get)
        return user, {"most_mutual_friend": best_match, "mutual_friend_count": mutual_friend_counts[best_match]}
    else:
        return user, {"most_mutual_friend": None, "mutual_friend_count": 0}

# Broadcast the user_friends dictionary to all workers
user_friends_dict = user_friends_rdd.collectAsMap()
user_friends_broadcast = spark.sparkContext.broadcast(user_friends_dict)

# Process each user to find the most mutual friends
mutual_friends_rdd = user_friends_rdd.map(find_mutual_friends)
mutual_friends_result = mutual_friends_rdd.collect()
process_end_time = time.time()

# Save the results to a JSON file
save_start_time = time.time()
with open(output_file, "w") as json_file:
    json.dump(dict(mutual_friends_result), json_file, indent=4)
save_end_time = time.time()

# End the timer for wall time
end_time = time.time()

# Calculate and print timing details
wall_time = end_time - start_time
read_time = read_end_time - read_start_time
process_time = process_end_time - process_start_time
save_time = save_end_time - save_start_time

print("\n--- Runtime Statistics ---")
print(f"Wall time (total script execution): {wall_time:.2f} seconds")
print(f"Time taken to read the file: {read_time:.2f} seconds")
print(f"Time taken to process mutual friends: {process_time:.2f} seconds")
print(f"Time taken to save results: {save_time:.2f} seconds")

print(f"\nMutual friends data saved to {output_file}")

# Stop the Spark session
spark.stop()