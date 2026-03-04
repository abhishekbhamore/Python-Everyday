"""
DAY 04: FILE I/O & DATA PROCESSING - TEST & SOLUTIONS
======================================================
Run this file to see file operations and ETL pipeline examples.
"""

import os
import tempfile

print("=" * 70)
print("DAY 04: FILE I/O & DATA PROCESSING - TEST & SOLUTIONS")
print("=" * 70)


# ============================================================================
# TEST 1: BASIC FILE OPERATIONS
# ============================================================================
print("\n[TEST 1] Basic File Operations")
print("-" * 70)

# Create a temporary directory for testing
test_dir = tempfile.mkdtemp()
test_file = os.path.join(test_dir, "test.txt")

print(f"Test directory: {test_dir}")

# Writing to a file
with open(test_file, "w") as f:
    f.write("Hello, Data Engineering!\n")
    f.write("Line 2 of data\n")
    f.write("Line 3 of data\n")

print(f"✓ File created: {test_file}")

# Reading from a file
with open(test_file, "r") as f:
    content = f.read()

print(f"✓ File content:\n{content}")

# Check file size
file_size = os.path.getsize(test_file)
print(f"✓ File size: {file_size} bytes")


# ============================================================================
# TEST 2: READING FILES LINE BY LINE
# ============================================================================
print("\n[TEST 2] Reading Files Line by Line")
print("-" * 70)

# Create a CSV-like file
csv_file = os.path.join(test_dir, "transactions.txt")
with open(csv_file, "w") as f:
    f.write("ID,Amount,Status\n")
    f.write("1001,250.50,completed\n")
    f.write("1002,150.00,pending\n")
    f.write("1003,75.25,completed\n")

print("Created transactions file")

# Read and process line by line
print("\nProcessing transactions:")
with open(csv_file, "r") as f:
    header = f.readline().strip()
    print(f"Header: {header}")
    
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 3:
            trans_id, amount, status = parts
            print(f"  {trans_id}: ${amount} ({status})")


# ============================================================================
# TEST 3: PARSING CSV DATA
# ============================================================================
print("\n[TEST 3] Parsing CSV Data into Dictionaries")
print("-" * 70)

def parse_csv(filename):
    """Parse CSV file into list of dicts"""
    
    data = []
    
    try:
        with open(filename, "r") as f:
            # Get header
            header = f.readline().strip().split(",")
            
            # Parse each row
            for line in f:
                values = line.strip().split(",")
                if len(values) == len(header):
                    row = dict(zip(header, values))
                    data.append(row)
    
    except FileNotFoundError:
        print(f"File not found: {filename}")
    
    return data

# Parse the transactions file
transactions = parse_csv(csv_file)
print(f"Parsed {len(transactions)} records:")
for trans in transactions:
    print(f"  {trans}")


# ============================================================================
# TEST 4: WRITING PROCESSED DATA
# ============================================================================
print("\n[TEST 4] Writing Processed Data to File")
print("-" * 70)

# Process the data
output_file = os.path.join(test_dir, "processed.csv")
processed = []

for trans in transactions:
    try:
        processed.append({
            "id": trans["ID"],
            "amount": float(trans["Amount"]),
            "status": trans["Status"],
            "category": "High" if float(trans["Amount"]) > 200 else "Normal"
        })
    except:
        pass

# Write results
with open(output_file, "w") as f:
    f.write("ID,Amount,Status,Category\n")
    
    for trans in processed:
        f.write(f"{trans['id']},{trans['amount']},{trans['status']},{trans['category']}\n")

print(f"✓ Wrote {len(processed)} records to {output_file}")

# Verify
with open(output_file, "r") as f:
    print("\nOutput file content:")
    for line in f:
        print(f"  {line.strip()}")


# ============================================================================
# TEST 5: ERROR HANDLING IN FILE OPERATIONS
# ============================================================================
print("\n[TEST 5] Error Handling")
print("-" * 70)

# Try to read non-existent file
missing_file = os.path.join(test_dir, "missing.txt")

if not os.path.exists(missing_file):
    print(f"✓ Correctly detected missing file: {missing_file}")
else:
    print(f"✗ File should not exist")

# Safe file reading function
def safe_read_file(filename):
    """Read file with error handling"""
    
    if not os.path.exists(filename):
        return None, f"File not found: {filename}"
    
    try:
        with open(filename, "r") as f:
            return f.read(), None
    except PermissionError:
        return None, "Permission denied"
    except Exception as e:
        return None, f"Error: {e}"

# Test safe reading
content, error = safe_read_file(csv_file)
if content:
    print(f"✓ Successfully read file ({len(content)} characters)")
else:
    print(f"✗ {error}")

# Test with missing file
content, error = safe_read_file(missing_file)
if error:
    print(f"✓ Handled missing file: {error}")


# ============================================================================
# TEST 6: ETL PIPELINE EXAMPLE
# ============================================================================
print("\n[TEST 6] Complete ETL Pipeline")
print("-" * 70)
print("Scenario: Read transaction data, validate, and export results\n")

# Create test data with some corrupt records
etl_input = os.path.join(test_dir, "etl_input.txt")
with open(etl_input, "w") as f:
    f.write("ID|Customer|Amount|Date|Status\n")
    f.write("1001|John Doe|250.50|2024-01-01|completed\n")
    f.write("1002|Jane Smith|150.00|2024-01-02|pending\n")
    f.write("1003|Bob Johnson|abc|2024-01-03|completed\n")  # Corrupt amount
    f.write("1004|Alice Brown|-100|2024-01-04|completed\n")  # Negative
    f.write("1005|Charlie Davis|500.00|2024-01-05|completed\n")

# EXTRACT
print("STEP 1: EXTRACT")
print("-" * 40)

raw_data = []

try:
    with open(etl_input, "r") as f:
        next(f)  # Skip header
        
        for line_num, line in enumerate(f, start=2):
            parts = line.strip().split("|")
            if len(parts) == 5:
                raw_data.append({
                    "line": line_num,
                    "id": parts[0],
                    "customer": parts[1],
                    "amount": parts[2],
                    "date": parts[3],
                    "status": parts[4]
                })

except FileNotFoundError:
    print("Error: Input file not found")

print(f"✓ Extracted {len(raw_data)} records")

# TRANSFORM & VALIDATE
print("\nSTEP 2: TRANSFORM & VALIDATE")
print("-" * 40)

valid_records = []
invalid_records = []

for record in raw_data:
    try:
        amount = float(record["amount"])
        
        # Validation
        if amount <= 0:
            invalid_records.append({
                "record": record,
                "error": "Amount must be positive"
            })
        elif amount > 100000:
            invalid_records.append({
                "record": record,
                "error": "Amount exceeds limit"
            })
        elif record["status"] not in ["completed", "pending", "failed"]:
            invalid_records.append({
                "record": record,
                "error": f"Invalid status: {record['status']}"
            })
        else:
            valid_records.append({
                "id": int(record["id"]),
                "customer": record["customer"],
                "amount": amount,
                "date": record["date"],
                "status": record["status"],
                "category": "High" if amount > 200 else "Normal"
            })
            print(f"✓ Valid: {record['customer']} - ${amount:.2f}")
    
    except ValueError as e:
        invalid_records.append({
            "record": record,
            "error": f"Cannot parse amount: {record['amount']}"
        })
        print(f"✗ Invalid: {record['customer']} - {invalid_records[-1]['error']}")

print(f"\nValid: {len(valid_records)}, Invalid: {len(invalid_records)}")

# LOAD
print("\nSTEP 3: LOAD")
print("-" * 40)

# Load valid records
output_file = os.path.join(test_dir, "etl_output.csv")
with open(output_file, "w") as f:
    f.write("ID,Customer,Amount,Date,Status,Category\n")
    
    for record in sorted(valid_records, key=lambda x: x["amount"], reverse=True):
        f.write(f"{record['id']},{record['customer']},{record['amount']:.2f},{record['date']},{record['status']},{record['category']}\n")

print(f"✓ Wrote {len(valid_records)} valid records")

# Load error report
error_file = os.path.join(test_dir, "etl_errors.txt")
with open(error_file, "w") as f:
    f.write("Error Report\n")
    f.write("=" * 50 + "\n\n")
    
    for item in invalid_records:
        f.write(f"Line {item['record']['line']}: {item['error']}\n")
        f.write(f"  Record: {item['record']}\n\n")

print(f"✓ Wrote {len(invalid_records)} error records")

# Display results
print("\n" + "=" * 70)
print("ETL Pipeline Results:")
print("=" * 70)

print("\nValid Output (etl_output.csv):")
with open(output_file, "r") as f:
    for line in f:
        print(f"  {line.strip()}")

print("\nError Report (etl_errors.txt):")
with open(error_file, "r") as f:
    for line in f:
        print(f"  {line.rstrip()}")


# ============================================================================
# TEST 7: PRACTICAL DATA PROCESSING PATTERNS
# ============================================================================
print("\n[TEST 7] Common Data Processing Patterns")
print("-" * 70)

# Pattern 1: Aggregation
print("\n1. Aggregation (Sum by category):")

def aggregate_by_status(records):
    """Sum amounts by status"""
    
    result = {}
    for record in records:
        status = record["status"]
        
        if status not in result:
            result[status] = {"count": 0, "total": 0}
        
        result[status]["count"] += 1
        result[status]["total"] += record["amount"]
    
    return result

summary = aggregate_by_status(valid_records)
for status, stats in summary.items():
    print(f"   {status}: {stats['count']} records, ${stats['total']:.2f}")

# Pattern 2: Filtering
print("\n2. Filtering (High value transactions):")

high_value = [r for r in valid_records if r["amount"] > 200]
print(f"   Found {len(high_value)} high-value transactions:")
for record in high_value:
    print(f"     {record['customer']}: ${record['amount']:.2f}")

# Pattern 3: Sorting
print("\n3. Sorting (By amount, descending):")

sorted_records = sorted(valid_records, key=lambda x: x["amount"], reverse=True)
for record in sorted_records[:3]:  # Top 3
    print(f"   {record['customer']}: ${record['amount']:.2f}")


# ============================================================================
# EXERCISE SOLUTIONS
# ============================================================================
print("\n[SOLUTIONS] Exercise Answers")
print("-" * 70)

# Solution A: CSV Reader Function
print("\nExercise A - CSV Reader Function:")

def read_csv_file(filename):
    """Read CSV and return list of dicts"""
    
    if not os.path.exists(filename):
        print(f"  Error: File not found")
        return []
    
    data = []
    try:
        with open(filename, "r") as f:
            header = f.readline().strip().split(",")
            
            for line in f:
                values = line.strip().split(",")
                if len(values) == len(header):
                    row = dict(zip(header, values))
                    data.append(row)
    
    except Exception as e:
        print(f"  Error: {e}")
    
    return data

print(f"  Function created - would read from file")

# Solution B: CSV Writer Function
print("\nExercise B - CSV Writer Function:")

def write_csv_file(filename, records):
    """Write list of dicts to CSV"""
    
    if not records:
        print(f"  Error: No records to write")
        return False
    
    try:
        with open(filename, "w") as f:
            # Header
            header = list(records[0].keys())
            f.write(",".join(header) + "\n")
            
            # Data
            for record in records:
                values = [str(record.get(key, "")) for key in header]
                f.write(",".join(values) + "\n")
        
        return True
    
    except Exception as e:
        print(f"  Error: {e}")
        return False

print(f"  Function created - writes records to CSV")

# Solution C: Complete ETL
print("\nExercise C - Complete ETL Pipeline:")
print(f"  ✓ Extract: Read and parse input")
print(f"  ✓ Transform: Validate and clean data")
print(f"  ✓ Load: Write results to file")
print(f"  ✓ See TEST 6 above for full example")

# Solution D: File operations
print("\nExercise D - File Operations:")

print(f"  File exists: {os.path.exists(csv_file)}")
print(f"  File size: {os.path.getsize(csv_file)} bytes")

# List files in directory
files = [f for f in os.listdir(test_dir) if f.endswith('.txt') or f.endswith('.csv')]
print(f"  Files in directory: {files}")


# ============================================================================
# CLEANUP
# ============================================================================
print("\n[CLEANUP] Removing test files...")

import shutil
shutil.rmtree(test_dir)
print(f"✓ Test directory removed")


print("\n" + "=" * 70)
print("KEY TAKEAWAYS FOR DATA ENGINEERING")
print("=" * 70)
print("""
1. ALWAYS USE 'with' STATEMENT:
   with open(file, "r") as f:
       data = f.read()
   - Automatically closes file
   - Handles errors properly

2. FILE MODES:
   - "r": Read only
   - "w": Write (overwrites existing)
   - "a": Append (add to end)
   - "r+": Read and write

3. READING PATTERNS:
   - file.read(): All content at once (small files)
   - file.readlines(): All lines in list
   - for line in file: Line by line (memory efficient)

4. PARSING PATTERNS:
   - Split by delimiter: line.split(",")
   - Parse to dict: dict(zip(header, values))
   - Type conversion: int(), float(), str()

5. ERROR HANDLING:
   - Check file exists: os.path.exists()
   - Handle ValueError for type conversion
   - Handle FileNotFoundError
   - Handle PermissionError

6. ETL PIPELINES:
   - Extract: Read and parse
   - Transform: Validate and clean
   - Load: Write results
   - Log: Track errors and success

PRACTICE: Create a sample CSV file and try the exercises!
""")

print("=" * 70)
