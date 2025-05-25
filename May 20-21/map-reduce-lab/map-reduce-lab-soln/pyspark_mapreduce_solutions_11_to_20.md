
# ✅ PySpark MapReduce Assignment Solutions (Questions 11–20)

---

## 11. Word Count with Minimum Length Filter

**Task:** Count only words with more than 3 characters.

```python
data = sc.textFile("words.txt")

filtered_counts = data.flatMap(lambda line: line.split())                       .filter(lambda word: len(word) > 3)                       .map(lambda word: (word, 1))                       .reduceByKey(lambda a, b: a + b)

filtered_counts.collect()
```

**Explanation:**
- `filter()` excludes short words.
- Standard word count logic follows.

---

## 12. Total Sales per Product

**Input Format:** `product,price`

```python
data = sc.textFile("sales.csv")

total_sales = data.map(lambda line: line.split(','))                   .map(lambda parts: (parts[0], float(parts[1])))                   .reduceByKey(lambda a, b: a + b)

total_sales.collect()
```

**Explanation:**
- Aggregates revenue per product.

---

## 13. Maximum Temperature per Day

**Input Format:** `day,temp`

```python
data = sc.textFile("temperature.csv")

max_temp = data.map(lambda line: line.split(','))                .map(lambda parts: (parts[0], float(parts[1])))                .reduceByKey(lambda a, b: max(a, b))

max_temp.collect()
```

**Explanation:**
- Keeps max value per day.

---

## 14. Word Pair Co-Occurrences

**Input Format:** Phrases

```python
data = sc.textFile("text.txt")

pairs = data.flatMap(lambda line: [(a, b) for a in line.split() for b in line.split() if a != b])             .map(lambda pair: (pair, 1))             .reduceByKey(lambda a, b: a + b)

pairs.collect()
```

**Explanation:**
- Creates all possible pairs (excluding self) and counts them.

---

## 15. Sort Words by Frequency

```python
data = sc.textFile("words.txt")

word_counts = data.flatMap(lambda line: line.split())                   .map(lambda word: (word, 1))                   .reduceByKey(lambda a, b: a + b)                   .map(lambda x: (x[1], x[0]))                   .sortByKey(False)

word_counts.collect()
```

**Explanation:**
- Maps (word, count) to (count, word) for sorting.

---

## 16. Most Active User

**Input Format:** `user_id,action`

```python
data = sc.textFile("activity.csv")

active_user = data.map(lambda line: (line.split(',')[0], 1))                   .reduceByKey(lambda a, b: a + b)

max_count = active_user.map(lambda x: x[1]).max()

active_user.filter(lambda x: x[1] == max_count).collect()
```

**Explanation:**
- Tallies action count per user, selects user(s) with max.

---

## 17. Join Product and Category

**products.csv:** `id,name,category_id`  
**categories.csv:** `id,name`

```python
products = sc.textFile("products.csv")              .map(lambda line: line.split(','))              .map(lambda x: (x[2], x[1]))

categories = sc.textFile("categories.csv")                .map(lambda line: line.split(','))                .map(lambda x: (x[0], x[1]))

joined = products.join(categories)

joined.collect()
```

**Explanation:**
- Join product with category name using `category_id`.

---

## 18. User's Total Spending

**Input Format:** `user_id,amount`

```python
data = sc.textFile("spending.csv")

user_spend = data.map(lambda line: line.split(','))                  .map(lambda x: (x[0], float(x[1])))                  .reduceByKey(lambda a, b: a + b)

user_spend.collect()
```

**Explanation:**
- Sums up spending per user.

---

## 19. Reverse Inverted Index

**Input Format:** `word 	 doc_id`

```python
data = sc.textFile("inverted.txt")

reverse_index = data.map(lambda line: line.strip().split('	'))                     .map(lambda parts: (parts[1], parts[0]))                     .groupByKey()                     .mapValues(lambda words: list(set(words)))

reverse_index.collect()
```

**Explanation:**
- Inverts index to show which words are in each document.

---

## 20. Average Session Time

**Input Format:** `user_id,timestamp`

```python
from datetime import datetime

def parse_time(t): return datetime.strptime(t, "%Y-%m-%d %H:%M:%S")

data = sc.textFile("session.csv")

times = data.map(lambda line: line.split(','))             .map(lambda parts: (parts[0], parse_time(parts[1])))             .groupByKey()             .mapValues(lambda ts: (max(ts) - min(ts)).total_seconds())             .map(lambda x: x[1])

average_time = times.mean()
average_time
```

**Explanation:**
- Groups timestamps per user and computes session duration.

---
