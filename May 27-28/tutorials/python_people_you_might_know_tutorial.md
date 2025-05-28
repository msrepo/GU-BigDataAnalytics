## 💡 Python Tutorial: "People You Might Know" Social Network Recommendation

### 🎯 Objective
Build a Python program that implements a simple “People You Might Know” algorithm. If two users have many mutual friends, recommend them to each other.

#### 📁 Dataset
File Name: soc-LiveJournal1Adj.txt

Format (per line):
```
<User><TAB><Friends>
```
```
<User>: Unique user ID (integer)
<Friends>: Comma-separated list of friends (user IDs)
Example: 0 1,2,3
```
Friendships are mutual (undirected), and the data respects this.

### 🧠 Algorithm Description
1. For each user U, recommend **up to 10 users** who are **not already friends** with U, but share the most mutual friends with U.
2. If there are fewer than 10 recommendations, include all.
3. Sort recommendations by:
 - Descending number of mutual friends.
 - Ascending numerical user ID in case of ties.

### 🛠️ Implementation Steps
#### Step 1: Load and Parse the Data
The adjacency list is stored in the file soc-LiveJournal1Adj.txt. Each line contains a user ID and their friends.

**Explanation**:
    - Each line is split into a user ID and their friends.

**Things to consider**
    - Do we need to check If a user has no friends?
    - How should we store the adjacency list - List of Lists? dictionary?

**Example output**
```
{0: [1, 2, 3], 1: [0, 5, 20], ...}
```

#### Step 2: Generate Mutual Friends
For each user, compute the mutual friends they share with other users.

**Explanation**:
    - For each user, iterate through their friends.
        - For each friend, iterate through their friends (second-degree connections).
            - Count the number of mutual friends for each second-degree connection.
            - Store the results
**Things to consider**
    - How should we store the number of mutual friends?
    - when testing and exploring, please work with only a small subset, say first 50 users
    - Understand the Dataset
       - find the average number of friends
       - User with the maximum number of friends (also, what is the largest number of friends)




#### Step 3: Generate Recommendations
For each user, recommend up to 10 users based on the number of mutual friends.

**Explanation**:
    - Sort the candidates by:
        - Descending number of mutual friends.
    - Select the top N recommendations (default is 10).

**Things to consider**
- What should we do in case of ties?

#### Step 4: Save the Output
Save the recommendations to a file in the required format.

**Explanation**:
Write the recommendations to a file in the format:
```
<User><TAB><Recommendations>
```

🧩 Example Output
- For testing: **User 11** should output:
  ```
  11    27552,7785,27573,27574,27589,27590,27600,27617,27620,27667
  ```


### ✅ Key Takeaways
1. Pure Python Implementation:
   - No external libraries like Spark are used.
   - The program processes the adjacency list directly.
2. Scalability:
   - This implementation is suitable for small to medium datasets.
   - For larger datasets, consider using distributed frameworks like Spark.
3. Output Format:
   - <User><TAB><Recommendations> where recommendations are sorted by mutual friends and user ID.
