
# 💡 Spark Tutorial: "People You Might Know" Social Network Recommendation

## 🎯 Objective

Build a Spark program that implements a simple **“People You Might Know”** algorithm. If two users have many mutual friends, recommend them to each other.

---

## 📁 Dataset

- **File Name:** `soc-LiveJournal1Adj.txt`
- **Path:** `datasets/soc-LiveJournal1Adj.txt`
- **Format (per line):**

  ```
  <User><TAB><Friends>
  ```

  - `<User>`: Unique user ID (integer)
  - `<Friends>`: Comma-separated list of friends (user IDs)
  - Example: `0	1,2,3`

> Friendships are **mutual** (undirected), and the data respects this.

---

## 🧠 Algorithm Description

- For each user `U`, recommend **up to 10 users** who are **not already friends** with `U`, but share the **most mutual friends** with `U`.
- If there are fewer than 10 recommendations, include all.
- **Sort** recommendations by:
  1. **Descending** number of mutual friends
  2. **Ascending** numerical user ID in case of ties

---

## 🛠️ Checkpoints

### ✅ Checkpoint 1: Load and Inspect Data

- Read `soc-LiveJournal1Adj.txt` into an RDD.
- Parse each line into `(user, [friend1, friend2, ...])`
- Inspect first few entries using `.take()`

### ✅ Checkpoint 2: Generate Mutual Friend Pairs

- For each user, generate all possible friend-of-friend pairs (excluding direct friends).
- Emit intermediate pairs in the format `((user1, user2), 1)`

### ✅ Checkpoint 3: Count Mutual Friends

- Use `reduceByKey` to sum up counts of each `(user1, user2)` pair → gives number of mutual friends.

### ✅ Checkpoint 4: Filter & Prepare Recommendations

- Exclude existing friends from recommendations.
- Group recommendations by user.
- Sort each recommendation list as required (desc by mutual count, asc by ID).

### ✅ Checkpoint 5: Final Output Format

- Output per user:

  ```
  <User><TAB><Recommendations>
  ```

  - Example: `11	27552,7785,27573,...`
  - Use `.map()` and `.sortBy()` for formatting.

- For testing: **User 11** should output:
  ```
  27552,7785,27573,27574,27589,27590,27600,27617,27620,27667
  ```

---

## 🧪 Testing & Debugging Tips

- Use `.take(N)` to inspect RDD contents step-by-step.
- Print outputs at intermediate stages to validate format.
- Use Colab + Spark setup (Colab 0) for smoother experience.

---

## 🔁 Pipeline Sketch (3–4 sentences)

We first load the data as an adjacency list RDD. For each user, we emit all second-degree friend pairs and mark existing friendships to avoid recommending them. We then aggregate mutual friend counts using `reduceByKey` and group recommendations per user. Finally, we sort and format the recommendations as specified and write the output.

---

## 📤 Submission Instructions

1. Upload your Spark program `.py` or `.ipynb` to Gradescope.
2. Include this writeup and pipeline sketch in your submission.
