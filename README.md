# Project Overview

This project provides tools and scripts for working with the CISI dataset, which contains 1,460 documents with metadata such as titles, authors, abstracts, and cross-references. It is designed for training and evaluating Information Retrieval (IR) models.

## Setting Up the Environment

To set up the environment, follow these steps:

### On Linux/Mac:
1. Run the following command to set up a virtual environment and install dependencies:
```sh
   ./setup_env.sh
```
### On Windows:
```sh
setup_env.bat
```
## Install PySpark to your current virtual environment

1. Activate the current virtual environment
```sh
     source <venv_path>/bin/activate
```
Replace `<venv_path>` with the path to your virtual environment.

2. **Install PySpark**:
   - Use `pip` to install PySpark in your virtual environment:
     
```bash
     pip install pyspark
```
3. **Verify the installation**:
   - After installation, verify that PySpark is installed by running:
     
```bash
     python -c "import pyspark; print(pyspark.__version__)"
```
This should print the installed version of PySpark.


