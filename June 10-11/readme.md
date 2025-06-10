Module Title: Finding Similar Items in Large Datasets
Module Duration: 2 sessions (90 minutes each)
Learning Objectives

By the end of this module, students should be able to:

    Understand and apply shingling to represent documents as sets.

    Explain and compute MinHash signatures to estimate Jaccard similarity.

    Implement Locality Sensitive Hashing to efficiently retrieve similar items.

    Build basic indexing structures for similarity search at scale.

Lecture Flow and Problem-Based Prompts
Session 1: Shingling, MinHashing, and Estimating Similarity
Part 1: Problem Prompt

    Your company is building a plagiarism detection engine that must scan millions of student essays submitted each semester. You need to detect near-duplicates in real-time. How do you represent and compare these documents at scale?

Activity 1: Understanding Shingling (20 minutes)

Prompt:

    What is a scalable way to compare documents based on their content, not just metadata or exact matches?

Instructor Explanation:

    Introduce k-shingles (contiguous substrings of length k).

    Discuss how shingling transforms documents into sets.

Discussion Takeaways:

    Shingling captures textual structure.

    Choice of k affects granularity of similarity.

    Representing documents as sets enables use of Jaccard similarity.

Activity 2: Introducing MinHashing (30 minutes)

Prompt:

    If two documents are similar, their shingle sets will have a high Jaccard similarity. But computing exact Jaccard similarity is expensive for large datasets. How can we estimate similarity efficiently?

Hands-on Exercise:

    Manually compute MinHash signatures for two small shingle sets using 2–3 hash functions.

Instructor Explanation:

    Define MinHash.

    Show how it approximates Jaccard similarity.

Discussion Takeaways:

    MinHash reduces dimensionality.

    Each hash function approximates one permutation.

    Signatures can be compared with high efficiency.

Wrap-Up Prompt:

    What trade-offs are we making by using MinHashing over exact comparisons?

Key Takeaways:

    Estimations are fast and scalable.

    Accept small errors in similarity for huge performance gains.

Session 2: Locality Sensitive Hashing (LSH) and Indexing
Part 1: Problem Prompt

    Given a collection of 100 million web pages, how would you instantly retrieve pages that are similar to a query page? Linear scans are too slow.

Activity 1: Understanding Locality Sensitive Hashing (30 minutes)

Prompt:

    How do we efficiently find similar MinHash signatures without comparing all pairs?

Instructor Explanation:

    Explain LSH using banding technique.

    Divide MinHash signatures into bands and rows.

    Only compare signatures that match in at least one band.

Interactive Demo:

    Students simulate LSH on small signature matrices with 2–3 bands.

Discussion Takeaways:

    LSH dramatically reduces the number of comparisons.

    Similar documents hash to the same bucket with high probability.

    Balancing number of bands/rows affects precision and recall.

Activity 2: Building an Index (20 minutes)

Prompt:

    You’ve implemented LSH. Now how do you store and retrieve candidate matches efficiently?

Instructor Explanation:

    Use hash tables to store LSH buckets.

    Design inverted index with document IDs.

Discussion Takeaways:

    Indexes allow constant time lookup of candidates.

    Index structure depends on LSH output.

Capstone Problem Prompt (Final 20 minutes)

    You are tasked with building a similarity search engine for a job portal that needs to match CVs to job descriptions in real time. Design the data pipeline from raw text to similarity output.

Small Group Discussion:
Students break into teams to design:

    Preprocessing (tokenization, shingling)

    Signature computation

    LSH buckets

    Candidate ranking

Presentations (5 mins per group)

Instructor Feedback & Summary
Assessment / Homework

    Implement a basic MinHashing + LSH pipeline on a small dataset (e.g., news articles or Reddit comments).

    Reflective essay: What are the advantages and limitations of using LSH in real-world systems like search engines or recommender systems?

Optional Extensions

    Compare LSH with other approximate nearest neighbor methods like KD-Trees or Annoy.

    Explore Spark/MapReduce implementation for large-scale similarity joins.

