# PySpark Inverted Index - Code Explanation

This document explains a PySpark program that builds an **Inverted Index** from a document dataset using the RDD API.

---

## ✅ Code

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

## 📄 Input Assumption

Each line in documents.txt is in the format:
```
doc1\tthis is a document
doc2\tanother document with text
```

## 🧠 Line-by-Line Explanation
1. sc = SparkContext("local", "InvertedIndex")

    Initializes a local Spark application named "InvertedIndex".

2. data = sc.textFile("documents.txt")

    Reads the input file into an RDD.

    Each element is a line containing a document ID and text, separated by a tab (\t).

## 🔄 Inverted Index Creation Logic
3. flatMap(...)

lambda line: [(word, doc_id) for word in set(text.split())]

    Splits each line into (doc_id, text) using tab (\t) as the delimiter.

    Converts the text into a set of unique words (to avoid duplicate (word, doc_id) pairs from the same document).

    Emits (word, doc_id) pairs.

Example:
```
Input line: "doc1\thello world hello"
Emitted pairs: [("hello", "doc1"), ("world", "doc1")]
```

4. groupByKey()

    Groups all (word, doc_id) pairs by word.

    Result: ("hello", ["doc1", "doc2", ...])

5. mapValues(lambda doc_ids: ','.join(set(doc_ids)))

    Removes duplicates in document IDs and joins them into a comma-separated string.

    Result: ("hello", "doc1,doc2")

6. index.saveAsTextFile("inverted_index")

    Saves the final inverted index as text files in the folder inverted_index.
## ✅ Final Output Example

Given:
```

doc1\tapple banana
doc2\tbanana cherry
doc3\tapple cherry banana
```
Output:
```
("apple", "doc1,doc3")
("banana", "doc1,doc2,doc3")
("cherry", "doc2,doc3")
```