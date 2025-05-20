
# PySpark Maximum Integer - Code Explanation

This document explains a simple PySpark program to find the maximum integer in a text file using RDD operations.

---

## Code

```python
numbers = data.flatMap(lambda line: map(int, line.strip().split()))
max_val = numbers.max()
```

---

## Assumption

- `data` is an RDD created from a text file:
```python
data = sc.textFile("numbers.txt")
```

- Sample file content (`numbers.txt`):
```
10 20 30
5 100
25
```

---

## Explanation

### 1. `flatMap(lambda line: map(int, line.strip().split()))`

- `line.strip().split()`:
  - Strips leading/trailing whitespace.
  - Splits the line into words (string numbers).
  - E.g., `"10 20 30"` → `["10", "20", "30"]`

- `map(int, ...)`:
  - Converts each string to an integer.
  - E.g., `["10", "20", "30"]` → `[10, 20, 30]`

- `flatMap(...)`:
  - Flattens the resulting lists from all lines into a single RDD of integers.
  - Result: `[10, 20, 30, 5, 100, 25]`

### 2. `numbers.max()`

- Computes the **maximum value** in the RDD `numbers`.
- In this case, the result is:
```python
max_val = 100
```

---

## Final Result

The code finds the highest number from a potentially very large text file, using distributed computation with PySpark.

---
