
# 📘 Tutorial Session: Apache Spark – Internal Workings and MapReduce Comparison

## 🎯 Session Objectives

By the end of this tutorial, participants will be able to:

- Understand the architecture and internal execution model of Apache Spark
- Compare Spark with Hadoop MapReduce
- Describe key Spark concepts like RDDs, DAG, stages, tasks, and lineage
- Understand Spark’s lazy evaluation and in-memory computing

---

## 🕒 Session Duration: 1.5 – 2 hours

## 🧠 Target Audience

- Data Engineering / Computer Science students
- Developers or analysts moving from Hadoop to Spark
- Professionals working with big data systems

---

## 🗂️ Session Outline

### 1. 🔥 What is Apache Spark? (10 min)

- Distributed data processing engine
- Originally developed at UC Berkeley (AMP Lab)
- Open source; now part of the Apache Software Foundation

**Key Features:**
- In-memory computation
- Fast and general-purpose
- Supports batch, streaming, SQL, ML, graph processing

---

### 2. 🛠️ Hadoop MapReduce Overview (10 min)

- Two-phase data processing model:
  - **Map**: Transform input data into key-value pairs
  - **Reduce**: Aggregate values by key
- Disk I/O intensive – intermediate results written to disk
- Good for batch but slow for iterative jobs (ML, graph)

---

### 3. ⚡ Spark vs MapReduce (10 min)

| Feature              | Hadoop MapReduce     | Apache Spark             |
|---------------------|----------------------|---------------------------|
| Execution Model      | Disk-based           | In-memory                |
| Performance          | Slower               | Up to 100x faster        |
| Ease of Use          | Java-centric         | APIs in Python, Scala, Java |
| Support for ML/Graph | Limited              | Native APIs (MLlib, GraphX) |
| Fault Tolerance      | Data replication     | Lineage-based recovery   |

---

### 4. 🧬 Spark Internal Architecture (20 min)

**Components:**
- **Driver Program**: Entry point; creates SparkContext, defines job
- **Cluster Manager**: YARN, Mesos, Standalone, Kubernetes
- **Executors**: Run tasks and return results to the driver
- **Tasks**: Smallest unit of execution
- **Jobs > Stages > Tasks**

**Key Concepts:**
- **RDD (Resilient Distributed Dataset)**: Core abstraction
- **Transformations (lazy)** vs **Actions (trigger execution)**

---

### 5. 🧭 DAG Scheduler and Lineage (15 min)

- Spark builds a **Directed Acyclic Graph (DAG)** of transformations
- Divides DAG into **stages** at shuffle boundaries
- Each stage contains multiple **tasks** (one per partition)

**RDD Lineage:**
- RDDs remember how they were derived
- Used for **fault recovery** (no need for replication like HDFS)

---

### 6. 💾 In-Memory Computing and Lazy Evaluation (10 min)

- **In-memory caching** avoids disk I/O
- Transformations like `map()`, `filter()` are lazy
- Execution happens only when an **action** (e.g., `count()`, `collect()`) is called

---

### 7. 👨‍💻 Live Demo: Word Count in Spark vs MapReduce (15 min)

**Spark (PySpark):**

```python
from pyspark import SparkContext

sc = SparkContext("local", "WordCount")
text = sc.textFile("sample.txt")
counts = text.flatMap(lambda line: line.split()) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.collect()
```

**Compare with MapReduce:**
- Mapper.java and Reducer.java (verbose)
- Uses HDFS for input/output and intermediate results

---

### 8. 🧪 Interactive Quiz or Discussion (10 min)

Example Questions:
- What is the purpose of a DAG in Spark?
- How does Spark achieve fault tolerance?
- Why is caching useful in iterative algorithms?

---

## 📌 Materials Needed

- Spark installed locally or use Databricks/Google Colab
- Sample text file (`sample.txt`)
- Projector/slides
- Access to Spark UI (optional)

---

## 📘 Supplementary Reading

- [Spark: The Definitive Guide (O’Reilly)](https://www.oreilly.com/library/view/spark-the-definitive/9781491912218/)
- Spark documentation: https://spark.apache.org/docs/latest/
