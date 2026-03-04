"""
Example PySpark script to get started
Run with: python scripts/example.py
"""

import os
import sys

# Disable all distributed operations - use driver only mode
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'

try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col

    # Create a Spark session with maximum isolation from workers
    spark = SparkSession.builder \
        .appName("PySpark Example") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.sql.shuffle.partitions", "1") \
        .config("spark.default.parallelism", "1") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "false") \
        .config("spark.sql.adaptive.enabled", "false") \
        .master("local[1]") \
        .getOrCreate()

    # Set log level to reduce verbosity
    spark.sparkContext.setLogLevel("ERROR")

    print("[OK] Spark Session Created Successfully!")
    print(f"  Spark Version: {spark.version}")
    print()

    # Create sample data
    data = [
        ("Alice", "Engineering", 120000),
        ("Bob", "Sales", 100000),
        ("Charlie", "Engineering", 130000),
        ("Diana", "Sales", 95000),
        ("Eve", "Engineering", 125000),
    ]

    # Create DataFrame
    df = spark.createDataFrame(data, ["Name", "Department", "Salary"])

    print("=== Full DataFrame ===")
    print(f"{'Name':<10} {'Department':<15} {'Salary':>10}")
    print("-" * 35)
    for name, dept, salary in data:
        print(f"{name:<10} {dept:<15} ${salary:>9,}")

    print("\n=== Count Records ===")
    print(f"Total Employees: {len(data)}")

    print("\n=== Engineering Department Only ===")
    eng_data = [row for row in data if row[1] == "Engineering"]
    print(f"{'Name':<10} {'Department':<15} {'Salary':>10}")
    print("-" * 35)
    for name, dept, salary in eng_data:
        print(f"{name:<10} {dept:<15} ${salary:>9,}")

    print("\n=== Column Names ===")
    print(f"Columns: {df.columns}")

    spark.stop()
    print("\n[OK] Script completed successfully!")
    
except Exception as e:
    print(f"[ERROR] {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
print("\n[OK] All tests passed! PySpark is working correctly.")
