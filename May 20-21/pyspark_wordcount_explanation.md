
# PySpark Word Count - Code Explanation

This document explains a basic PySpark program for counting word frequencies in a text file.

---

## Code

```python
from pyspark import SparkContext

sc = SparkContext("local", "WordCount")

data = sc.textFile("documents.txt")
counts = data.flatMap(lambda line: line.strip().split()) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

counts.saveAsTextFile("word_counts")
```

---

## Explanation

### 1. `from pyspark import SparkContext`
- Imports the `SparkContext`, which is the entry point to PySpark’s RDD API.

### 2. `sc = SparkContext("local", "WordCount")`
- Initializes the Spark context.
  - `"local"`: Run on local machine.
  - `"WordCount"`: Application name.

### 3. `data = sc.textFile("documents.txt")`
- Loads the file `documents.txt` into an RDD named `data`.
- Each element of `data` is a line from the text file.

### 4. Word Count Transformation Chain

#### a. `flatMap(lambda line: line.strip().split())`
- Splits each line into words and flattens the result.
- Example: `["hello world", "hello Spark"]` becomes `["hello", "world", "hello", "Spark"]`.

#### b. `map(lambda word: (word, 1))`
- Maps each word to a tuple `(word, 1)`.

#### c. `reduceByKey(lambda a, b: a + b)`
- Aggregates word counts by key (i.e., the word), summing their values.

### 5. `counts.saveAsTextFile("word_counts")`
- Saves the resulting word counts to the folder `word_counts` as part files.

---

## Output Example

Assuming the input file contains:
```
hello world
hello Spark
```

The output would be something like:
```
("hello", 2)
("world", 1)
("Spark", 1)
```

---
