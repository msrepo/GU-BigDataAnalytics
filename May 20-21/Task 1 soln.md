# MapReduce Assignment - Sample Solutions

## Part 1: Understanding MapReduce (Theoretical)

### Task 1.1: Conceptual Questions

**1. What is the MapReduce programming model?**
MapReduce is a programming model used for processing and generating large datasets with a parallel, distributed algorithm on a cluster. It involves two main tasks: Map and Reduce. The Map function processes input key/value pairs to generate intermediate key/value pairs, and the Reduce function merges all intermediate values associated with the same intermediate key.

**2. Describe the roles of the Mapper and Reducer functions.**

* **Mapper:** Processes input data and produces key-value pairs as intermediate data.
* **Reducer:** Aggregates or summarizes the intermediate data based on keys.

**3. What are the benefits and limitations of using MapReduce for data processing?**

* **Benefits:** Scalability, fault tolerance, ease of programming large-scale tasks.
* **Limitations:** High latency, limited flexibility compared to modern frameworks like Spark, not suitable for iterative computations.

**4. How does MapReduce handle data partitioning and fault tolerance?**
Data is automatically split into chunks (input splits). Hadoop re-executes failed tasks, and maintains multiple replicas of data blocks for fault tolerance.

---

## Part 2: Implementing Simple MapReduce Programs

### Task 2.1: Largest Integer in a Large Dataset


#### PySpark Implementation

```python
from pyspark import SparkContext

sc = SparkContext("local", "MaxInt")

data = sc.textFile("numbers.txt")
numbers = data.flatMap(lambda line: map(int, line.strip().split()))
max_val = numbers.max()

print("Maximum Value:", max_val)
```

### Task 2.2: Word Frequency Counter


#### PySpark Implementation

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

## Part 3: Problem-Based MapReduce Tasks

### Task 3.1: Inverted Index Creation


#### PySpark Implementation

```python
from pyspark import SparkContext

sc = SparkContext("local", "InvertedIndex")

data = sc.textFile("documents.txt")

# Assuming input as: doc_id<TAB>text
index = data.flatMap(lambda line: [(word, line.split('\t')[0]) 
                                   for word in set(line.split('\t')[1].split())]) \
             .groupByKey() \
             .mapValues(lambda doc_ids: ','.join(set(doc_ids)))

index.saveAsTextFile("inverted_index")
```

### Task 3.2: Average Temperature by Location

#### PySpark Implementation

```python
from pyspark import SparkContext

sc = SparkContext("local", "AvgTemp")

data = sc.textFile("temps.csv")

# Format: location,date,temp
averages = data.map(lambda line: line.strip().split(',')) \
              .map(lambda parts: (parts[0], (float(parts[2]), 1))) \
              .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1])) \
              .mapValues(lambda x: round(x[0] / x[1], 2))

averages.saveAsTextFile("average_temps")
```

### Task 3.3: Popular Product in E-Commerce Dataset


#### PySpark Implementation

```python
from pyspark import SparkContext

sc = SparkContext("local", "PopularProduct")

data = sc.textFile("transactions.csv")

# Format: user_id,product_id,timestamp
popular = data.map(lambda line: line.strip().split(',')) \
             .map(lambda parts: (parts[1], 1)) \
             .reduceByKey(lambda a, b: a + b)

max_count = popular.map(lambda x: x[1]).max()
popular.filter(lambda x: x[1] == max_count).saveAsTextFile("popular_product")
```

---

## Part 4: Reflection and Discussion

### Task 4.1: Report Summary (Sample)

* **Understanding:** This assignment provided practical exposure to how the MapReduce framework processes large-scale datasets efficiently by separating tasks into mappers and reducers.
* **Challenges:** Handling text parsing and ensuring correct output formatting were initial challenges. Debugging reducer logic was also non-trivial.
* **Use Cases:** MapReduce is effective for log analysis, search indexing, big data summarization, and batch processing in distributed environments. PySpark provided significant performance and code simplicity advantages for the same logic.
