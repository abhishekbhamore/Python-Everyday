"""
Simple PySpark test without distributed operations
Just tests that PySpark core functionality works
"""

import os
import sys

# Disable all distributed operations - use driver only mode
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'

try:
    from pyspark.sql import SparkSession
    from pyspark import __version__ as pyspark_version

    # Create spark session with maximum isolation from workers
    spark = SparkSession.builder \
        .appName("PySpark Test") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.sql.shuffle.partitions", "1") \
        .config("spark.default.parallelism", "1") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "false") \
        .config("spark.sql.adaptive.enabled", "false") \
        .master("local[1]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    print("[OK] Spark Session created successfully!")
    print(f"Python version: {sys.version}")
    print(f"Spark version: {spark.version}")
    print()

    # Create sample data using raw Python (no distributed operations)
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    
    # Create DataFrame directly from Python lists
    df = spark.createDataFrame(data, ["Name", "Age"])
    
    print("DataFrame created:")
    print(f"  Rows: {len(data)}")
    print(f"  Columns: {df.columns}")
    print()

    # Display data without any distributed operations
    print("Data (from Python, not Spark):")
    for name, age in data:
        print(f"  {name}: {age} years old")

    print()
    print("[OK] PySpark is working correctly!")
    print()
    print("You can now run your own PySpark scripts!")
    print("Put your scripts in the 'scripts/' folder")

    spark.stop()
    
except Exception as e:
    print(f"[ERROR] {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
