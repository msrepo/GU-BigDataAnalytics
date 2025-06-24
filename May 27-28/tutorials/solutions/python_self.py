### ✅ Checkpoint 1: Load and Inspect Data

# - Read `soc-LiveJournal1Adj.txt` into an RDD.
# - Parse each line into `(user, [friend1, friend2, ...])`


file_path = "datasets/soc-LiveJournal1Adj.txt"

with open(file_path, "r") as f:
    lines = f.readlines()

# when testing and exploring, we will work with only a small subset
subset_size = 50

# Parse lines into (user, [friend1, friend2, ...])
for line in lines[:subset_size]:
    user_id, friends_ids = line.split("\t")
    user_id = int(user_id)
    # parse friend IDs
    friends_ids = friends_ids.split(",")
    # convert to int
    friends_ids = [int(id) for id in friends_ids]
    print(f"User {user_id} Friends {friends_ids}")

# Understand the Dataset
# - find the average number of friends
# - User with the maximum number of friends (also, what is the largest number of friends)

# to have this, we will use list, each list contains a tuple of (user_id, [friend_id,...,friend_id])
parsed_data = []
parsed_data_dict = {}
for line in lines[:subset_size]:
    user_id, friends_ids = line.split("\t")
    user_id = int(user_id)
    friends_ids = friends_ids.split(",")
    friends_ids = [int(id) for id in friends_ids]
    parsed_data.append((user_id, friends_ids))
    parsed_data_dict[user_id] = friends_ids

friends_counts = [len(friends_ids) for user_id, friends_ids in parsed_data]
average_friends_counts = sum(friends_counts) / len(friends_counts)
max_friends_counts = max(friends_counts)

print(
    f"Each user on average has {average_friends_counts} friends and atmost {max_friends_counts} friends"
)

# how many friend-of-friend on average are there? if (A,B) are friends and (B,C) are friends, then (A,C) are friends-of-friends?

"""
### ✅ Checkpoint 2: Generate Mutual Friend Pairs

- For each user, generate all possible friend-of-friend pairs (excluding direct friends).
- Emit intermediate pairs in the format `((user1, user2), 1)`

"""
friends_of_friends_dict = {}
for user_id, friends_ids in parsed_data:
    friends_of_friends = []
    for id in friends_ids:
        friends_of_friends.extend(parsed_data[id])
    friends_of_friends_set = set(friends_of_friends)
    # remove direct friends
    direct_friends = set(friends_ids)
    friends_of_friends_set = friends_of_friends_set.difference(direct_friends)
    friends_of_friends_dict[user_id] = friends_of_friends_set

'''
### ✅ Checkpoint 3: Count Mutual Friends
'''
friends_recommendation = {}
for user_id, friends_of_friends in friends_of_friends_dict.items():
    mutual_friends_count = {}
    
    

