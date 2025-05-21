# PySpark MapReduce Examples and Assignment Guide

## Overview

This repository contains:

- Short PySpark MapReduce API usage examples (`PySpark MapReduce API Usage Examples.md`)
- MapReduce assignment questions and solutions (`pyspark_mapreduce_assignment.md`)
- Additional questions and solutions (`pyspark_mapreduce_additional_questions.md`)

This README explains how to set up your development environment in VSCode, run the example code, and how to proceed with the assignment files.

---

## Setup VSCode and Python Virtual Environment (venv)

1. **Install Python**

Make sure Python 3.7+ is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Open VSCode**

Launch Visual Studio Code.

3. **Create a Project Folder**

Create or open your project folder in VSCode.

4. **Open Terminal**

Open the integrated terminal in VSCode (`Ctrl + `` or `View > Terminal`).

5. **Create a Python Virtual Environment**

Run the following command:

```bash
python -m venv venv
````

6. **Activate the Virtual Environment**

* On Windows:

```bash
.\venv\Scripts\activate
```

* On macOS/Linux:

```bash
source venv/bin/activate
```

7. **Install PySpark**

With the virtual environment activated, install PySpark:

```bash
pip install pyspark
```

---

## Running the PySpark MapReduce Examples

1. **Open or create a Python script** (e.g., `mapreduce_examples.py`).

2. **Copy example snippets from `PySpark MapReduce API Usage Examples.md`** into your script.

3. **Run the script**

In the terminal with the virtual environment activated, run:

```bash
python mapreduce_examples.py
```

You should see output from the example snippets printed in the terminal.

---

## Reading the PySpark API Usage Examples

* Open `pyspark_mapreduce_examples.md` in VSCode or any Markdown viewer.
* Review short snippets demonstrating `map()`, `reduce()`, `reduceByKey()`, `flatMap()`, and combining transformations.
* These snippets will help you understand the MapReduce programming model in PySpark.

---

## Working on the MapReduce Assignment and Additional Questions

* Place your assignment questions and additional questions files in the project folder.
* For each question, create a corresponding Python script or notebook.
* Use the examples as a template to write your MapReduce jobs with PySpark.
* Test your solutions locally by running your Python scripts in the activated virtual environment.

---

## Tips for Development

* Use VSCode’s Python extension for code highlighting, linting, and debugging.
* Make sure your virtual environment is selected as the Python interpreter in VSCode (`Ctrl+Shift+P` → `Python: Select Interpreter` → choose `./venv`).
* Use small sample datasets initially to quickly test your MapReduce jobs.
* When done, deactivate the virtual environment by running:

```bash
deactivate
```

---

## Summary

* Set up Python venv in VSCode.
* Install PySpark with pip.
* Run provided MapReduce example snippets.
* Use the examples as references for your assignments.
* Organize assignment and additional questions logically in scripts.
* Utilize VSCode features for smooth development.

---
