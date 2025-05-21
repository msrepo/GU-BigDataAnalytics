
# ✅ PySpark MapReduce Assignment Solutions with Explanations

This document provides PySpark MapReduce solutions to 30 assignment questions. Each problem is followed by a detailed, line-by-line explanation of the code used to solve it.

---

## 1. Line Count

**Task:** Count the number of lines in a text file.

```python
from pyspark import SparkContext
sc = SparkContext("local", "LineCount")

data = sc.textFile("lines.txt")          # Read file as RDD
line_count = data.count()                # Count the number of lines

print(line_count)                        # Output the result
```

**Explanation:**
- `textFile(...)` reads the file as an RDD of lines.
- `count()` is an action that returns the number of elements in the RDD.

---

## 2. Character Frequency

**Task:** Count frequency of each character (excluding whitespace).

```python
data = sc.textFile("char.txt")

char_freq = data.flatMap(lambda line: list(line.replace(" ", "")))  # Flatten to chars
                 .map(lambda c: (c, 1))                              # Map each char to 1
                 .reduceByKey(lambda a, b: a + b)                    # Count by char

char_freq.collect()
```

**Explanation:**
- `flatMap(...)` splits lines into characters (whitespace removed).
- `map(...)` creates (char, 1) tuples.
- `reduceByKey(...)` aggregates counts for each character.

---

## 3. Find All Unique Words

**Task:** Extract all unique words.

```python
data = sc.textFile("words.txt")

unique_words = data.flatMap(lambda line: line.split())                    .distinct()

unique_words.collect()
```

**Explanation:**
- `flatMap(...)` splits lines into words.
- `distinct()` filters out duplicates.

---

## 4. Longest Word in Each Line

```python
data = sc.textFile("lines.txt")

longest = data.map(lambda line: max(line.split(), key=len))

longest.collect()
```

**Explanation:**
- `map(...)` finds the longest word in each line using `max(..., key=len)`.

---

## 5. Filter Stop Words

```python
stop_words = set(["the", "is", "at", "which", "on"])

data = sc.textFile("text.txt")

filtered = data.map(lambda line: " ".join([word for word in line.split() if word not in stop_words]))

filtered.collect()
```

**Explanation:**
- Removes common stop words using list comprehension.

---

## 6. Average Word Length per Line

```python
data = sc.textFile("lines.txt")

avg_length = data.map(lambda line: round(sum(len(word) for word in line.split()) / len(line.split()), 2))

avg_length.collect()
```

**Explanation:**
- Calculates the average word length for each line.

---

## 7. Top 3 Most Frequent Words

```python
data = sc.textFile("text.txt")

top3 = data.flatMap(lambda line: line.split())            .map(lambda word: (word, 1))            .reduceByKey(lambda a, b: a + b)            .takeOrdered(3, key=lambda x: -x[1])

top3
```

**Explanation:**
- Counts word frequency and selects top 3 using `takeOrdered()`.

---

## 8. Movie Ratings Aggregator

```python
data = sc.textFile("ratings.csv")

movie_ratings = data.map(lambda line: line.split(','))                     .map(lambda parts: (parts[1], (float(parts[2]), 1)))                     .reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1]))                     .mapValues(lambda x: round(x[0]/x[1], 2))

movie_ratings.collect()
```

**Explanation:**
- Aggregates total and count, then computes average rating per movie.

---

## 9. Join Users and Purchases

```python
users = sc.textFile("users.csv").map(lambda line: line.split(','))                                 .map(lambda parts: (parts[0], parts[1]))

purchases = sc.textFile("purchases.csv").map(lambda line: line.split(','))                                         .map(lambda parts: (parts[0], parts[1]))

joined = users.join(purchases)

joined.map(lambda x: (x[1][0], x[1][1])).collect()
```

**Explanation:**
- Performs a join on user ID to get (username, item) tuples.

---

## 10. Session Length per User

```python
data = sc.textFile("session.txt")

session_counts = data.map(lambda line: line.split()[0])                      .map(lambda user_id: (user_id, 1))                      .reduceByKey(lambda a, b: a + b)

session_counts.collect()
```

**Explanation:**
- Extracts user ID and counts occurrences (actions) per user.

---
