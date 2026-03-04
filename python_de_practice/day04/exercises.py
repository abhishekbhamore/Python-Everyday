"""
DAY 04: FILE I/O & DATA PROCESSING
===================================
Focus: Reading, writing, and processing file data

AWS Context: Core skills for data engineering:
- Reading data from S3, local files, databases
- Processing and transforming data
- Writing results back to files
- Handling errors when files are corrupt or missing
"""

# ============================================================================
# SECTION 1: BASIC FILE READING
# ============================================================================

# Exercise 1.1: Opening and reading entire file
# Method 1: Traditional (not recommended - must remember to close)
# file = open("data.txt", "r")
# content = file.read()
# file.close()

# Method 2: Using 'with' statement (PREFERRED - auto closes file)
# with open("data.txt", "r") as file:
#     content = file.read()  # All content as one string

# Exercise 1.2: Reading line by line (memory efficient for large files)
# with open("data.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# Exercise 1.3: Reading all lines into a list
# with open("data.txt", "r") as file:
#     lines = file.readlines()  # ['line1\n', 'line2\n', ...]


# ============================================================================
# SECTION 2: BASIC FILE WRITING
# ============================================================================

# Exercise 2.1: Writing to a file (creates new file or overwrites existing)
# with open("output.txt", "w") as file:
#     file.write("This is line 1\n")
#     file.write("This is line 2\n")

# Exercise 2.2: Appending to a file (add to end without overwriting)
# with open("output.txt", "a") as file:
#     file.write("Added line\n")

# Exercise 2.3: Writing multiple lines
# with open("output.txt", "w") as file:
#     lines = ["Line 1", "Line 2", "Line 3"]
#     file.write("\n".join(lines))


# ============================================================================
# SECTION 3: PROCESSING FILES LINE BY LINE
# ============================================================================

# Exercise 3.1: Read and process transactions from a file
def process_transaction_file(filename):
    """Read transaction file and return processed data"""
    
    transactions = []
    
    try:
        with open(filename, "r") as file:
            # Skip header if present
            next(file)  # Skip first line
            
            for line in file:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                # Parse CSV: id,amount,status
                parts = line.split(",")
                try:
                    trans = {
                        "id": int(parts[0]),
                        "amount": float(parts[1]),
                        "status": parts[2]
                    }
                    transactions.append(trans)
                except (ValueError, IndexError):
                    print(f"Skipping invalid line: {line}")
    
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return transactions

# Exercise 3.2: Write processed results to file
def write_results(filename, results):
    """Write results to file"""
    
    try:
        with open(filename, "w") as file:
            file.write("ID,Amount,Status\n")  # Header
            
            for result in results:
                line = f"{result['id']},{result['amount']},{result['status']}\n"
                file.write(line)
        
        print(f"Results written to {filename}")
    
    except Exception as e:
        print(f"Error writing file: {e}")


# ============================================================================
# SECTION 4: WORKING WITH DIFFERENT FILE FORMATS
# ============================================================================

# Exercise 4.1: Delimited files (CSV, TSV, pipe-delimited)
def parse_delimited_file(filename, delimiter=","):
    """Parse file with custom delimiter"""
    
    rows = []
    
    try:
        with open(filename, "r") as file:
            header = next(file).strip().split(delimiter)
            
            for line in file:
                values = line.strip().split(delimiter)
                if len(values) == len(header):
                    row = dict(zip(header, values))
                    rows.append(row)
    
    except Exception as e:
        print(f"Error: {e}")
    
    return rows

# Exercise 4.2: Working with fixed-width files
# Fixed width: id in columns 0-4, name in 5-14, amount in 15-24
def parse_fixed_width(filename):
    """Parse fixed-width file"""
    
    rows = []
    
    try:
        with open(filename, "r") as file:
            for line in file:
                row = {
                    "id": line[0:5].strip(),
                    "name": line[5:15].strip(),
                    "amount": line[15:25].strip()
                }
                rows.append(row)
    
    except Exception as e:
        print(f"Error: {e}")
    
    return rows


# ============================================================================
# SECTION 5: ERROR HANDLING WITH FILES
# ============================================================================

# Exercise 5.1: Handling missing files
def safe_read_file(filename):
    """Read file safely"""
    
    if not os.path.exists(filename):
        print(f"Error: File not found - {filename}")
        return None
    
    try:
        with open(filename, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Exercise 5.2: Handling file access errors
def safe_write_file(filename, content):
    """Write file safely"""
    
    try:
        with open(filename, "w") as file:
            file.write(content)
            print(f"File written successfully: {filename}")
        return True
    except PermissionError:
        print(f"Permission denied: {filename}")
        return False
    except IOError:
        print(f"Cannot write to file: {filename}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Exercise 5.3: File operations
import os

def file_exists(filename):
    """Check if file exists"""
    return os.path.exists(filename)

def get_file_size(filename):
    """Get file size in bytes"""
    try:
        return os.path.getsize(filename)
    except:
        return None

def delete_file(filename):
    """Delete a file"""
    try:
        os.remove(filename)
        print(f"File deleted: {filename}")
    except:
        print(f"Cannot delete file: {filename}")

def list_files(directory, extension=None):
    """List files in directory"""
    try:
        files = os.listdir(directory)
        if extension:
            files = [f for f in files if f.endswith(extension)]
        return files
    except:
        return []


# ============================================================================
# SECTION 6: PRACTICAL DATA PIPELINE EXAMPLE
# ============================================================================

# Scenario: ETL Pipeline (Extract, Transform, Load)

def extract_data(input_file):
    """Extract: Read data from file"""
    
    print(f"Extracting from {input_file}...")
    transactions = []
    
    try:
        with open(input_file, "r") as file:
            next(file)  # Skip header
            
            for line_num, line in enumerate(file, start=2):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    parts = line.split("|")
                    trans = {
                        "id": int(parts[0]),
                        "customer": parts[1].strip(),
                        "amount": float(parts[2]),
                        "date": parts[3].strip(),
                        "status": parts[4].strip()
                    }
                    transactions.append(trans)
                except Exception as e:
                    print(f"  Error on line {line_num}: {e}")
    
    except FileNotFoundError:
        print(f"  Error: File not found")
    
    return transactions


def transform_data(transactions):
    """Transform: Process and validate data"""
    
    print(f"Transforming {len(transactions)} records...")
    
    valid = []
    invalid = []
    
    for trans in transactions:
        # Validation
        if trans["amount"] <= 0:
            invalid.append({"trans": trans, "reason": "Negative amount"})
        elif trans["amount"] > 100000:
            invalid.append({"trans": trans, "reason": "Amount exceeds limit"})
        elif trans["status"] not in ["completed", "pending", "failed"]:
            invalid.append({"trans": trans, "reason": "Invalid status"})
        else:
            # Transformation
            trans["amount_usd"] = f"${trans['amount']:.2f}"
            trans["valid"] = True
            valid.append(trans)
    
    return valid, invalid


def load_data(transactions, output_file):
    """Load: Write results to file"""
    
    print(f"Loading to {output_file}...")
    
    try:
        with open(output_file, "w") as file:
            # Write header
            file.write("ID,Customer,Amount,Date,Status,Formatted Amount\n")
            
            # Write data
            for trans in transactions:
                line = f"{trans['id']},{trans['customer']},{trans['amount']},{trans['date']},{trans['status']},{trans['amount_usd']}\n"
                file.write(line)
        
        print(f"  Successfully wrote {len(transactions)} records")
        return True
    
    except Exception as e:
        print(f"  Error writing file: {e}")
        return False


# ============================================================================
# PRACTICAL EXERCISES FOR YOU TO COMPLETE
# ============================================================================

# TODO Exercise A: Create a function to read a CSV file
# - Read from input.csv
# - Parse lines (id,name,amount)
# - Return list of dicts
# - Handle missing files gracefully

# TODO Exercise B: Create a function to write results
# - Write list of dicts to output.csv
# - Include header row
# - Format amounts with 2 decimals
# - Handle write errors

# TODO Exercise C: Create a complete ETL pipeline
# - Read from input.txt
# - Validate each record
# - Filter invalid records
# - Write valid records to output.txt
# - Write error report to errors.txt

# TODO Exercise D: File operations
# - Check if file exists
# - Get file size
# - List all CSV files in a directory
# - Delete a file safely


if __name__ == "__main__":
    print("Day 04: File I/O & Data Processing")
    print("=" * 60)
    print("\nNote: File operations examples are included.")
    print("Uncomment the file paths to test with actual files.")
