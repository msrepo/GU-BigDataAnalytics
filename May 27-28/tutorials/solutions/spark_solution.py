from pyspark import SparkContext

def parse_line(line):
    """
    Parse each line of the input file into (user, [friends]).
    """
    parts = line.strip().split("\t")
    user = int(parts[0])
    friends = list(map(int, parts[1].split(","))) if len(parts) > 1 else []
    return user, friends

def generate_friend_pairs(user, friends):
    """
    Generate all possible friend-of-friend pairs for a user.
    """
    pairs = []
    for friend in friends:
        for mutual_candidate in friends:
            if friend != mutual_candidate:
                pairs.append(((friend, mutual_candidate), 1))
    return pairs

def filter_existing_friends(user, recommendations, friends_set):
    """
    Filter out existing friends from the recommendations.
    """
    filtered = [(candidate, count) for candidate, count in recommendations if candidate not in friends_set]
    return sorted(filtered, key=lambda x: (-x[1], x[0]))[:10]  # Sort by count desc, then by ID asc

if __name__ == "__main__":
    # Initialize SparkContext
    sc = SparkContext("local", "People You Might Know")

    # Load and parse the data
    file_path = "datasets/soc-LiveJournal1Adj.txt"
    data = sc.textFile(file_path)
    parsed_data = data.map(parse_line)

    # Checkpoint 1: Inspect parsed data
    print("Checkpoint 1: Parsed Data")
    print(parsed_data.take(5))

    # Generate mutual friend pairs
    friend_pairs = parsed_data.flatMap(lambda x: generate_friend_pairs(x[0], x[1]))

    # Count mutual friends
    mutual_friend_counts = friend_pairs.reduceByKey(lambda a, b: a + b)

    # Checkpoint 3: Inspect mutual friend counts
    print("Checkpoint 3: Mutual Friend Counts")
    print(mutual_friend_counts.take(5))

    # Prepare recommendations
    recommendations = mutual_friend_counts.map(lambda x: (x[0][0], (x[0][1], x[1]))) \
                                           .groupByKey() \
                                           .mapValues(list)

    # Filter out existing friends and sort recommendations
    final_recommendations = parsed_data.join(recommendations) \
                                       .mapValues(lambda x: filter_existing_friends(x[1], x[0], set(x[0]))) \
                                       .map(lambda x: (x[0], x[1]))

    # Checkpoint 5: Inspect final recommendations
    print("Checkpoint 5: Final Recommendations")
    print(final_recommendations.take(5))

    # Save the output
    output_path = "output/recommendations"
    final_recommendations.map(lambda x: f"{x[0]}\t{','.join(map(str, x[1]))}").saveAsTextFile(output_path)

    print(f"Recommendations saved to {output_path}")

    # Stop SparkContext
    sc.stop()