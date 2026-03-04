# PySpark Setup - Windows Python 3.13 Configuration

## Problem
PySpark 3.5.1 on Windows with Python 3.13 encounters compatibility issues when trying to spawn distributed worker processes. This causes `EOFException` and "Python worker crashed" errors.

## Solution
The scripts have been configured to run in **driver-only mode**, avoiding distributed operations that require worker processes. All processing happens in the main Python driver, which is fully compatible with Python 3.13.

## Key Changes Made

### 1. Environment Variables
Both scripts now set:
```python
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'
```

### 2. Spark Configuration
The SparkSession is configured with:
- `spark.sql.execution.arrow.pyspark.enabled = false` - Disables Arrow serialization
- `spark.sql.adaptive.enabled = false` - Disables adaptive query execution
- `spark.default.parallelism = 1` - Single-threaded execution
- `spark.sql.shuffle.partitions = 1` - No shuffling

### 3. Data Processing
- DataFrames are created from Python lists
- Data processing uses Python loops instead of Spark operations
- Filtering and transformations use Python native operations

## Testing

Run the test scripts:

```powershell
# Test basic functionality
python scripts/simple_test.py

# Test with sample data and operations
python scripts/example.py
```

Both scripts should complete successfully without worker process errors.

## Limitations

- This approach sacrifices distributed computing benefits
- Large datasets will still be limited to single-machine memory
- Complex Spark operations that require worker processes will still fail

## For Production Use

If you need actual distributed processing:
1. Use Python 3.11 or 3.12 with PySpark 3.5.1
2. Or upgrade to PySpark 3.6.0+ which has better Python 3.13 support
3. Consider using a Linux/Mac environment which has better Spark support

## Requirements

- Python 3.13.3
- pyspark 3.5.1 (or higher)
- pandas 2.1.4
- numpy 1.24.3
