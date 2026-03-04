# PySpark Development Environment

This folder contains a PySpark development setup for running Spark jobs using Python.

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment
- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Directory Structure
```
Pyspark/
├── venv/                  # Virtual environment
├── notebooks/             # Jupyter notebooks
├── scripts/              # PySpark scripts
├── data/                 # Data files
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Running PySpark Code

### Option 1: Interactive Shell
```bash
pyspark
```

### Option 2: Python Script
```bash
spark-submit scripts/your_script.py
```

### Option 3: Jupyter Notebook
```bash
jupyter notebook
```
Then navigate to `notebooks/` folder and create a new notebook.

## Example: First PySpark Job
Create `scripts/hello_spark.py`:
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HelloSpark").getOrCreate()

# Create a simple DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

df.show()
spark.stop()
```

Run it:
```bash
spark-submit scripts/hello_spark.py
```

## Troubleshooting

- **Java not found**: Install JDK 11 or later
- **SPARK_HOME not set**: Install PySpark via pip (it includes Spark)
- **Memory issues**: Set `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` environment variables
