# PySpark MapReduce API Usage Examples

This document shows short snippets demonstrating how to use the MapReduce API in PySpark.

---

## Setup SparkContext

```python
from pyspark import SparkContext

sc = SparkContext("local", "MapReduceExample")
```

## Map Example: Square each number
```python
nums = sc.parallelize([1, 2, 3, 4, 5])
squares = nums.map(lambda x: x * x).collect()
print(squares)  # Output: [1, 4, 9, 16, 25]

```

## Reduce Example: Sum all numbers

```python
nums = sc.parallelize([1, 2, 3, 4, 5])
sum_all = nums.reduce(lambda a, b: a + b)
print(sum_all)  # Output: 15

```

## Map + ReduceByKey: Word Count Example
```python
lines = sc.parallelize([
    "hello world",
    "hello from pyspark",
    "hello world again"
])

words = lines.flatMap(lambda line: line.split(" "))
word_pairs = words.map(lambda word: (word, 1))
word_counts = word_pairs.reduceByKey(lambda a, b: a + b).collect()

print(word_counts)
# Output: [('hello', 3), ('world', 2), ('from', 1), ('pyspark', 1), ('again', 1)]

```


## Combining map, filter, and reduceByKey
```python
lines = sc.parallelize([
    "apple banana apple",
    "banana orange apple",
    "banana banana orange"
])

word_counts = (lines
    .flatMap(lambda line: line.split(" "))
    .filter(lambda word: word != "orange")
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
    .collect()
)

print(word_counts)
# Output: [('apple', 3), ('banana', 4)]

```
## Stop SparkContext
```python
sc.stop()

```