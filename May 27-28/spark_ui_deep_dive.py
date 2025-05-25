from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Spark UI Lab") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

# Step 1: Load large synthetic dataset
data = [(i, f"record_{i%100}") for i in range(1, 5000000)]
df = spark.createDataFrame(data, ["id", "label"])

# Step 2: Apply a wide transformation (shuffle)
grouped = df.groupBy("label").count()

# Step 3: Trigger an action
grouped.show()

# Step 4: Wait to keep UI accessible
# Step 4: Wait to keep UI accessible
print("Press Enter to exit and stop the Spark application...")
input()  # Waits for the user to press Enter


spark.stop()
