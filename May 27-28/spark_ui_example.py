from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Spark UI Example") \
    .master("local[*]") \
    .getOrCreate()

# Generate dummy data
data = [(i, i*i) for i in range(1000000)]
df = spark.createDataFrame(data, ["number", "square"])

# A simple transformation
df_filtered = df.filter(df.number % 2 == 0)

# Trigger an action
df_filtered.count()

# Keep SparkContext alive to inspect UI
print("Go to http://localhost:4040 to inspect the Spark UI.")
time.sleep(60)  # Keeps Spark app running for 60 seconds

spark.stop()
