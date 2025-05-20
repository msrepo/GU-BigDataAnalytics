from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("MatrixVectorMultiplication") \
    .getOrCreate()

# Example square matrix and vector
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
vector = [1, 2, 3]

# Parallelize the matrix and vector
matrix_rdd = spark.sparkContext.parallelize(enumerate(matrix))  # (row_index, row_values)
vector_rdd = spark.sparkContext.parallelize(enumerate(vector))  # (index, value)

# Perform matrix-vector multiplication
result_rdd = matrix_rdd.map(lambda row: (row[0], sum(row[1][i] * vector[i] for i in range(len(vector)))))

# Collect the result
result = result_rdd.collect()

# Print the result
print("Matrix-Vector Multiplication Result:")
for row_index, value in result:
    print(f"Row {row_index}: {value}")

# Stop the Spark session
spark.stop()