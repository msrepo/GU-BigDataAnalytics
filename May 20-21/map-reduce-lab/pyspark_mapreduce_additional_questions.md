# Additional PySpark MapReduce Assignment Questions

Below are additional PySpark-based MapReduce assignment tasks with sample input and expected output. These vary in difficulty from beginner to advanced.

---

## 1. **Line Count (Beginner)**

**Task:** Count the number of lines in a text file.

**Sample Input (lines.txt):**

```
Hello world
Welcome to PySpark
This is a test file
```

**Expected Output:**

```
3
```

---

## 2. **Character Frequency (Beginner)**

**Task:** Count the frequency of each character (excluding whitespace).

**Sample Input:**

```
abc a
bca
```

**Expected Output:**

```
a	2
b	2
c	2
```

---

## 3. **Find All Unique Words (Beginner)**

**Task:** Extract and return all unique words in the file.

**Sample Input:**

```
hello world
hello spark
```

**Expected Output:**

```
hello
world
spark
```

---

## 4. **Longest Word in Each Line (Intermediate)**

**Task:** Return the longest word from each line of the file.

**Sample Input:**

```
this is line
spark transformation
```

**Expected Output:**

```
this
transformation
```

---

## 5. **Filter Stop Words (Intermediate)**

**Task:** Remove common stop words from the input text and return cleaned lines.

**Stop Words:** \["the", "is", "at", "which", "on"]

**Sample Input:**

```
the spark is fast
python is fun
```

**Expected Output:**

```
spark fast
python fun
```

---

## 6. **Average Word Length per Line (Intermediate)**

**Task:** Compute the average word length in each line.

**Sample Input:**

```
hello world
spark is great
```

**Expected Output:**

```
5.0
4.33
```

---

## 7. **Top 3 Most Frequent Words (Intermediate)**

**Task:** Return the top 3 most frequent words.

**Sample Input:**

```
apple banana apple
banana fruit apple
```

**Expected Output:**

```
apple	3
banana	2
fruit	1
```

---

## 8. **Movie Ratings Aggregator (Advanced)**

**Task:** Compute average rating per movie.

**Sample Input (ratings.csv):**

```
user1,movie1,3
user2,movie1,4
user3,movie2,5
```

**Expected Output:**

```
movie1	3.5
movie2	5.0
```

---

## 9. **Join Users and Purchases (Advanced)**

**Task:** Perform a join between user data and purchases.

**users.csv:**

```
1,Alice
2,Bob
```

**purchases.csv:**

```
1,Book
2,Pen
1,Notebook
```

**Expected Output:**

```
Alice	Book
Bob	Pen
Alice	Notebook
```

---

## 10. **Session Length per User (Advanced)**

**Task:** Compute the number of actions (lines) per user.

**Sample Input:**

```
1 click
2 click
1 search
2 buy
1 buy
```

**Expected Output:**

```
1	3
2	2
```

---

## 11. **Hashtag Frequency (Advanced)**

**Task:** Count the number of times each hashtag appears in tweets.

**Sample Input:**

```
#spark is awesome
learning #spark and #bigdata
```

**Expected Output:**

```
#spark	2
#bigdata	1
```

---

## 12. **Hourly Log Count (Advanced)**

**Task:** Count number of log entries per hour.

**Sample Input:**

```
2024-01-01 14:00:01 Login
2024-01-01 14:32:05 Logout
2024-01-01 15:01:11 Login
```

**Expected Output:**

```
14	2
15	1
```

---

## 13. **Product Co-Purchases (Advanced)**

**Task:** Given user purchases, find product pairs bought together.

**Sample Input:**

```
user1,apple,banana
user2,banana,orange
```

**Expected Output:**

```
apple,banana
banana,orange
```

---

## 14. **Common Friends (Advanced)**

**Task:** For each pair of users, find mutual friends.

**Sample Input:**

```
A:B,C,D
B:A,C
C:A,B
```

**Expected Output:**

```
A,B:C
A,C:B
B,C:A
```

---

## 15. **PageRank Iteration Step (Advanced)**

**Task:** Implement one iteration of PageRank.

**Sample Input:**

```
A 1.0 B C
B 1.0 C
C 1.0 A
```

**Expected Output:** *(approximate values)*

```
A	0.35
B	0.5
C	0.65
```

---

## 16. **TF-IDF Calculation (Advanced)**

**Task:** Compute TF-IDF score of words across multiple documents.

**Sample Input:**

```
doc1: spark hadoop
doc2: spark
```

**Expected Output:**

```
spark	TF:0.5 IDF:0.0 TF-IDF:0.0
hadoop	TF:0.5 IDF:0.3 TF-IDF:0.15
```

---

## 17. **User Purchase History Join (Advanced)**

**Task:** Join user profiles with their entire purchase list.

**Input:**

```
users.csv: 1,Alice\n2,Bob
purchases.csv: 1,apple\n1,banana\n2,apple
```

**Expected Output:**

```
Alice	apple,banana
Bob	apple
```

---

## 18. **Session Time per User (Advanced)**

**Task:** Compute total session time per user.

**Input:**

```
user1,login,10:00
user1,logout,10:30
user2,login,11:00
user2,logout,11:45
```

**Expected Output:**

```
user1	30
user2	45
```

---

## 19. **Top Rated Product by Category (Advanced)**

**Task:** From reviews, get highest-rated product per category.

**Input:**

```
product1,category1,5
product2,category1,4
product3,category2,5
```

**Expected Output:**

```
category1	product1
category2	product3
```

---

## 20. **Anomaly Detection (Advanced)**

**Task:** Find values that deviate by more than 2 standard deviations.

**Input:**

```
10
12
13
9
50
```

**Expected Output:**

```
50
```

---

## 21. **Transaction Sum per User (Advanced)**

**Task:** Compute total transaction amount per user.

**Input:**

```
user1,100
user2,50
user1,200
```

**Expected Output:**

```
user1	300
user2	50
```

---

## 22. **Text N-Gram Generation (Advanced)**

**Task:** Generate bigrams from each line.

**Input:**

```
I love Spark
Spark is fast
```

**Expected Output:**

```
I love
love Spark
Spark is
is fast
```

---

## 23. **Top-K Users by Activity (Advanced)**

**Task:** Identify top-K active users.

**Input:**

```
user1 login
user2 login
user1 logout
user3 login
user1 click
```

**Expected Output (Top 2):**

```
user1	3
user2	1
```

---

## 24. **Detect Duplicate Lines (Advanced)**

**Task:** Identify all duplicate lines in a file.

**Input:**

```
hello
spark
hello
pyspark
```

**Expected Output:**

```
hello	2
```

---

## 25. **Normalize Scores (Advanced)**

**Task:** Normalize values between 0 and 1.

**Input:**

```
5
10
15
```

**Expected Output:**

```
5	0.0
10	0.5
15	1.0
```

---

## 26. **Word Length Frequency (Advanced)**

**Task:** Count how many words have each length.

**Input:**

```
hi hello spark world
```

**Expected Output:**

```
2	1
5	3
```

---

## 27. **Hourly Peak Access (Advanced)**

**Task:** Find the hour with the most accesses.

**Input:**

```
2024-01-01 14:00
2024-01-01 14:30
2024-01-01 15:00
```

**Expected Output:**

```
14
```

---

## 28. **Reverse Index by Word Length (Advanced)**

**Task:** Group words by their length.

**Input:**

```
hello world hi
```

**Expected Output:**

```
2	hi
5	hello,world
```

---

## 29. **Find Longest Palindrome Word (Advanced)**

**Task:** Return the longest palindrome.

**Input:**

```
madam racecar apple civic
```

**Expected Output:**

```
racecar
```

---

## 30. **URL Click Frequency (Advanced)**

**Task:** Count how often each URL was clicked.

**Input:**

```
click google.com
click yahoo.com
click google.com
```

**Expected Output:**

```
google.com	2
yahoo.com	1
```
