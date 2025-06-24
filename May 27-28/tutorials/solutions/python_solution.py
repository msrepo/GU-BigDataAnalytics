from collections import defaultdict

# Step 1: Load and Parse the Data
def load_data(file_path):
    adjacency_list = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                user = int(parts[0])
                friends = list(map(int, parts[1].split(",")))
                adjacency_list[user] = friends
            elif len(parts) == 1:  # Handle users with no friends
                user = int(parts[0])
                adjacency_list[user] = []
    return adjacency_list

# Step 2: Compute Mutual Friends
def compute_mutual_friends(adjacency_list):
    mutual_friends = defaultdict(lambda: defaultdict(int))

    for user, friends in adjacency_list.items():
        for friend in friends:
            for mutual_candidate in adjacency_list[friend]:
                if mutual_candidate != user and mutual_candidate not in friends:
                    mutual_friends[user][mutual_candidate] += 1

    return mutual_friends

# Step 3: Generate Recommendations
def generate_recommendations(mutual_friends, top_n=10):
    recommendations = {}

    for user, candidates in mutual_friends.items():
        # Sort candidates by mutual friend count (descending) and user ID (ascending)
        sorted_candidates = sorted(candidates.items(), key=lambda x: (-x[1], x[0]))
        recommendations[user] = [candidate for candidate, _ in sorted_candidates[:top_n]]

    return recommendations

# Step 4: Save Recommendations
def save_recommendations(recommendations, output_path):
    with open(output_path, "w") as file:
        for user, recs in recommendations.items():
            recs_str = ",".join(map(str, recs))
            file.write(f"{user}\t{recs_str}\n")

# Main Function
if __name__ == "__main__":
    file_path = "datasets/soc-LiveJournal1Adj.txt"
    output_path = "recommendations.txt"

    # Load the data
    adjacency_list = load_data(file_path)

    # Compute mutual friends
    mutual_friends = compute_mutual_friends(adjacency_list)

    # Generate recommendations
    recommendations = generate_recommendations(mutual_friends)

    # Save recommendations
    save_recommendations(recommendations, output_path)
    print(f"Recommendations saved to {output_path}")