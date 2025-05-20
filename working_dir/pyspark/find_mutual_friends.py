from collections import defaultdict
import time
import json

# Path to the input file
input_file = "datasets/cs246/hw1-bundle/q1/data/soc-LiveJournal1Adj.txt"
output_file = "working_dir/pyspark/output/mutual_friends.json"

# Start the timer for wall time
start_time = time.time()

# Read the file and parse the data
read_start_time = time.time()
user_friends = defaultdict(set)
with open(input_file, "r") as file:
    for line in file:
        line = line.strip()
        if not line or "\t" not in line:  # Skip empty or invalid lines
            continue
        user, friends = line.split("\t")
        user = int(user)
        friends = set(map(int, friends.split(","))) if friends else set()
        user_friends[user] = friends
read_end_time = time.time()

# Find the user with the most mutual friends for each user
process_start_time = time.time()
mutual_friends_result = {}
for user, friends in user_friends.items():
    mutual_friend_counts = defaultdict(int)

    # Check mutual friends for non-friends
    for friend in friends:
        for mutual_candidate in user_friends[friend]:
            if mutual_candidate != user and mutual_candidate not in friends:
                mutual_friend_counts[mutual_candidate] += 1

    # Find the user with the most mutual friends
    if mutual_friend_counts:
        best_match = max(mutual_friend_counts, key=mutual_friend_counts.get)
        mutual_friends_result[user] = {
            "most_mutual_friend": best_match,
            "mutual_friend_count": mutual_friend_counts[best_match]
        }
    else:
        mutual_friends_result[user] = {
            "most_mutual_friend": None,
            "mutual_friend_count": 0
        }
process_end_time = time.time()

# Save the results to a JSON file
save_start_time = time.time()
with open(output_file, "w") as json_file:
    json.dump(mutual_friends_result, json_file, indent=4)
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