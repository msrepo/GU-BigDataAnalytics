
# 📘 PySpark MapReduce Programming Assignment

## 🎯 Objective
To understand and implement MapReduce logic using PySpark’s RDD API for solving real-world problems on large datasets.

---

## ⚙️ Instructions
- Use **PySpark RDDs**, not DataFrames.
- Input files are in plain text format.
- Write and test your PySpark scripts using `SparkContext`.
- Include appropriate comments in your code.

---

## 📂 Input Assumptions
All input files will be located in the working directory and accessible via `sc.textFile()`.

---

## 📝 Questions

### **1. Word Count with Filtering**
**Input:** A file named `documents.txt`, each line containing a sentence.  
**Task:** Write PySpark code to:
- Count the frequency of each word (case-insensitive).
- Exclude stopwords like `["a", "the", "is", "in", "at", "on", "and"]`.
- Output should be sorted by frequency in descending order.

---

### **2. Most Purchased Product**
**Input:** A CSV file `transactions.csv` in the format: `user_id,product_id,timestamp`.  
**Task:** 
- Find the product(s) with the highest number of purchases.
- Save the result as: `("product_id", count)`.

---

### **3. Build an Inverted Index**
**Input:** `documents.txt` with lines like: `doc_id<TAB>text`.  
**Task:** 
- Create an inverted index mapping each unique word to a list of document IDs where it appears.
- Output format: `("word", "doc1,doc2,...")`.

---

### **4. Average Rating Per Product**
**Input:** A CSV file `reviews.csv` in the format: `user_id,product_id,rating`.  
**Task:** 
- Compute the **average rating** for each product.
- Output format: `("product_id", average_rating)` rounded to 2 decimal places.

---

### **5. Most Active User by Reviews**
**Input:** Same as above (`reviews.csv`).  
**Task:** 
- Identify the user(s) who submitted the **highest number of reviews**.
- Output format: `("user_id", review_count)`.

---

## ✅ Submission Checklist
- Code for all 5 questions.
- Use `saveAsTextFile()` to write output for each task.
- Document any assumptions in a `README.md`.
