# PySpark Popular Product - Code Explanation

This document explains a PySpark program that finds the most popular product from transaction data using RDDs.

---

## ✅ Code

```python
from pyspark import SparkContext

sc = SparkContext("local", "PopularProduct")

data = sc.textFile("transactions.csv")

# Format: user_id,product_id,timestamp
popular = data.map(lambda line: line.strip().split(',')) \\
             .map(lambda parts: (parts[1], 1)) \\
             .reduceByKey(lambda a, b: a + b)

max_count = popular.map(lambda x: x[1]).max()
popular.filter(lambda x: x[1] == max_count).saveAsTextFile("popular_product")
```

## 🧠 Line-by-Line Explanation
1. sc = SparkContext("local", "PopularProduct")

    Creates a local Spark context with the application name "PopularProduct".

2. data = sc.textFile("transactions.csv")

    Reads the transactions file into an RDD, each element is a line.

3. .map(lambda line: line.strip().split(','))

    Splits each line by comma into a list: [user_id, product_id, timestamp].

4. .map(lambda parts: (parts[1], 1))

    Extracts the product_id (parts[1]) and maps it to the pair (product_id, 1) for counting.

5. .reduceByKey(lambda a, b: a + b)

    Aggregates counts of each product by summing the 1's for all occurrences of that product.

6. max_count = popular.map(lambda x: x[1]).max()

    Finds the maximum count (highest number of purchases) among all products.

7. popular.filter(lambda x: x[1] == max_count).saveAsTextFile("popular_product")

    Filters the products that have the maximum count (most popular).

    Saves these products and their counts to the folder "popular_product".

## 📄 Input Assumption

Each line in transactions.csv is in the format:
```
user_id,product_id,timestamp
```
Example:
```
u1,p123,2025-05-20 10:00:00
u2,p234,2025-05-20 10:01:00
u1,p123,2025-05-20 10:05:00
```