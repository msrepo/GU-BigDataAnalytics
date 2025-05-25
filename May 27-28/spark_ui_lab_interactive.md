
# 🧪 Interactive Lab Assignment: Exploring Apache Spark UI

Welcome to this interactive lab! This assignment will guide you through running a Spark job and exploring the Spark Web UI to analyze performance, inspect execution plans, and detect bottlenecks.

---

## 🎯 Learning Objectives

By the end of this lab, you will:

- Understand the structure and purpose of the Spark UI.
- Analyze Jobs, Stages, and Tasks using the UI.
- Explore memory and storage tabs.
- Identify performance issues like skew and long tasks.

---

## 🛠️ Prerequisites

- Apache Spark installed
- Python and PySpark installed
- A web browser
- Basic Spark knowledge

---

## 🚀 Step 1: Setup and Run Spark Job

Create a Python file named `spark_ui_lab.py` with the following content:

```python
from pyspark.sql import SparkSession
import time

spark = SparkSession.builder     .appName("Spark UI Lab")     .master("local[*]")     .config("spark.sql.shuffle.partitions", "8")     .getOrCreate()

# Load synthetic data
data = [(i, f"record_{i % 100}") for i in range(1, 5000000)]
df = spark.createDataFrame(data, ["id", "label"])

# Apply transformation
grouped = df.groupBy("label").count()

# Trigger action
grouped.show()

# Keep Spark UI alive
print("Sleeping for 120 seconds to allow UI inspection...")
time.sleep(120)

spark.stop()
```

Run it with:

```bash
python spark_ui_lab.py
```

Open the Spark UI: [http://localhost:4040](http://localhost:4040)

---

## ✅ Checkpoint 1: Jobs Tab

- [ ] How many jobs were triggered?
- [ ] Click on a job and inspect its DAG.
- [ ] How many stages are there in one job?

📝 _Write your observations here:_

---

## ✅ Checkpoint 2: Stages Tab

- [ ] Which stage took the most time?
- [ ] Do all tasks in a stage take similar time?
- [ ] Look at Shuffle Read/Write values.

📝 _Observations:_

---

## ✅ Checkpoint 3: Tasks Tab

- [ ] Sort tasks by duration. Are there any stragglers?
- [ ] Check if some partitions have significantly more data.

📝 _Observations:_

---

## ✅ Checkpoint 4: Executors Tab

- [ ] How many executors are shown (including driver)?
- [ ] What is the memory usage per executor?
- [ ] Any task failures?

📝 _Observations:_

---

## ✅ Checkpoint 5: SQL Tab

- [ ] View the physical plan for groupBy().count().
- [ ] Was there a shuffle in the plan?
- [ ] Which operations were performed?

📝 _Observations:_

---

## 🧪 Bonus Activity: Caching and Storage Tab

Modify the script:

```python
df_filtered = df.filter(df.id % 2 == 0).cache()
df_filtered.count()
```

Re-run and:

- [ ] Observe time difference in repeated actions.
- [ ] View memory usage in the Storage tab.

📝 _Observations:_

---

## 🧼 Cleanup

- Stop the script or let it finish.
- Close the browser tab.

---

## 🧠 Reflection Questions

1. What causes a job to split into multiple stages?
2. Why is task skew problematic?
3. How can caching improve performance?

---

Happy learning! 🚀
