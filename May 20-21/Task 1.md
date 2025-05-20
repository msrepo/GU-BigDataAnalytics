**Title: Exploring MapReduce Through Problem-Based Implementation**

*Objective:*

To understand the working principles of the MapReduce paradigm and implement it to solve real-world problems involving large-scale data processing.

Part 1: Understanding MapReduce (Theoretical)

Task 1.1: Conceptual Questions

Answer the following questions in your own words:

    What is the MapReduce programming model?

    Describe the roles of the Mapper and Reducer functions.

    What are the benefits and limitations of using MapReduce for data processing?

    How does MapReduce handle data partitioning and fault tolerance?

Part 2: Implementing Simple MapReduce Programs (Practical)

Task 2.1: Largest Integer in a Large Dataset

    Problem Statement: Given a very large list of integers distributed across multiple files, implement a MapReduce algorithm to find the largest integer.

    Expected Output: A single integer representing the maximum value.

    Language Suggestion: Python using mrjob or Java with Hadoop.

Task 2.2: Word Frequency Counter

    Problem Statement: Given a collection of text documents, implement a MapReduce job that counts the number of occurrences of each word.

    Expected Output: A list of words along with their frequency.

Part 3: Problem-Based MapReduce Tasks

Task 3.1: Inverted Index Creation

    Problem Statement: Given a collection of documents, build an inverted index where each word maps to a list of document IDs in which it appears.

    Use Case: Basic search engine functionality.

Task 3.2: Average Temperature by Location

    Problem Statement: Given a large dataset of temperature records with fields (location, date, temperature), compute the average temperature for each location.

    Expected Output: List of locations with their corresponding average temperatures.

Task 3.3: Popular Product in E-Commerce Dataset

    Problem Statement: Given a dataset of e-commerce transactions (user_id, product_id, timestamp), identify the most frequently bought product.

    Expected Output: Product ID(s) with the highest purchase frequency.

Part 4: Reflection and Discussion

Task 4.1: Report Writing
Write a short report (1–2 pages) summarizing:

    Your understanding of the MapReduce model.

    Key challenges you faced during implementation.

    Potential use cases of MapReduce in modern data systems.

Submission Format

    Source code files (organized in folders per task)

    Output files for each task

    A PDF report for Part 4