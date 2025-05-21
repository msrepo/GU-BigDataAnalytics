
# 🧠 PySpark RDD MapReduce API Summary

PySpark provides a rich set of APIs to perform distributed data processing using the MapReduce paradigm. Below is a categorized list of core and advanced transformations and actions.

---

## 🔁 Transformations (Lazy Operations)

These operations define a new RDD and are evaluated only when an action is performed.

### 1. `map(func)`
Apply `func` to each element and return a new RDD.

### 2. `flatMap(func)`
Like `map()`, but flattens the result.

### 3. `filter(func)`
Return only elements where `func` returns `True`.

### 4. `distinct()`
Remove duplicate elements.

### 5. `sample(withReplacement, fraction, seed=None)`
Randomly sample a fraction of the data.

### 6. `union(otherRDD)`
Return a new RDD containing all elements from both RDDs.

### 7. `intersection(otherRDD)`
Return only common elements between RDDs.

### 8. `subtract(otherRDD)`
Remove elements from the first RDD that are present in the second.

### 9. `cartesian(otherRDD)`
Return all possible pairs of elements from both RDDs.

### 10. `groupBy(func)`
Group elements using a function instead of key-based grouping.

---

## 🔑 Key-Value Pair Transformations

Work on RDDs with (key, value) format:

### 11. `reduceByKey(func)`
Merge values for each key using `func`.

### 12. `groupByKey()`
Group values under each key.

### 13. `combineByKey(createCombiner, mergeValue, mergeCombiners)`
Generalized aggregation; useful for computing averages.

### 14. `aggregateByKey(zeroValue)(seqOp, combOp)`
Aggregate values using different logic at partition and global level.

### 15. `mapValues(func)`
Apply a function to each value while preserving the key.

### 16. `flatMapValues(func)`
Apply a function to each value that returns an iterable and flatten results.

### 17. `sortByKey(ascending=True)`
Sort RDD by keys.

---

## 🔗 Joins and Co-Groups

### 18. `join(otherRDD)`
Inner join on keys.

### 19. `leftOuterJoin(otherRDD)`
Left outer join on keys.

### 20. `rightOuterJoin(otherRDD)`
Right outer join on keys.

### 21. `fullOuterJoin(otherRDD)`
Full outer join on keys.

### 22. `cogroup(otherRDD)`
Group data from both RDDs by key.

---

## ⚡ Actions (Trigger Execution)

These return results or save output.

### 23. `collect()`
Return all elements as a list (avoid on large data).

### 24. `take(n)`
Return first `n` elements.

### 25. `top(n)`
Return top `n` elements (using natural ordering).

### 26. `takeOrdered(n, key=...)`
Return the first `n` elements ordered by a custom key.

### 27. `count()`
Return number of elements.

### 28. `countByValue()`
Return frequency of each element.

### 29. `reduce(func)`
Aggregate all elements using a function.

### 30. `fold(zeroValue)(func)`
Like `reduce()`, but with a zero value for empty partitions.

### 31. `aggregate(zeroValue)(seqOp, combOp)`
Perform aggregation with separate logic per partition and across partitions.

### 32. `foreach(func)`
Apply a function to each element (used for side effects like printing or writing).

---

## 💾 Output Actions

### 33. `saveAsTextFile(path)`
Save elements to a text file.

### 34. `saveAsSequenceFile(path)`
Write as Hadoop SequenceFile (used with key-value RDDs).

### 35. `saveAsObjectFile(path)`
Serialize RDD elements to files (for reloading later).
