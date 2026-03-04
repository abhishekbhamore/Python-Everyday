"""
DAY 02: DATA STRUCTURES TEST FILE & SOLUTIONS
==============================================
Run this file to understand lists, dicts, and data processing patterns.
"""

import json

print("=" * 70)
print("DAY 02: DATA STRUCTURES - TEST & SOLUTIONS")
print("=" * 70)


# ============================================================================
# TEST 1: WORKING WITH LISTS
# ============================================================================
print("\n[TEST 1] Lists - The Foundation of Data Processing")
print("-" * 70)

# Real scenario: Processing transaction IDs from a database query
transaction_ids = [1001, 1002, 1003, 1004, 1005]

print(f"Original list: {transaction_ids}")
print(f"First ID: {transaction_ids[0]}")
print(f"Last ID: {transaction_ids[-1]}")
print(f"First 3 IDs: {transaction_ids[0:3]}")

# Common operation: Finding if transaction exists
target_id = 1003
if target_id in transaction_ids:
    print(f"Transaction {target_id} found in list")

# Processing amounts with validation
raw_amounts = ["100.50", "250.75", "corrupt", "50.00"]
processed_amounts = []

for amount_str in raw_amounts:
    try:
        amount = float(amount_str)
        if amount > 0:
            processed_amounts.append(amount)
            print(f"[OK] Valid amount: {amount}")
        else:
            print(f"[ERROR] Invalid amount: {amount} (negative)")
    except ValueError:
        print(f"[ERROR] Cannot parse: {amount_str}")

print(f"Processed amounts: {processed_amounts}")
print(f"Total: ${sum(processed_amounts):.2f}")


# ============================================================================
# TEST 2: WORKING WITH DICTIONARIES
# ============================================================================
print("\n[TEST 2] Dictionaries - Representing Records")
print("-" * 70)

# Real scenario: Customer record from database
customer = {
    "customer_id": 1001,
    "name": "John Doe",
    "email": "john@example.com",
    "created_date": "2024-01-01",
    "total_purchases": 5000.00,
    "is_active": True
}

print(f"Customer Record:")
for key, value in customer.items():
    print(f"  {key}: {value}")

# Safe access (won't error if key missing)
phone = customer.get("phone", "Not provided")
print(f"\nPhone: {phone}")

# Modifying records
customer["last_purchase_date"] = "2024-01-15"
customer["total_purchases"] = 5500.00
print(f"\nUpdated total purchases: ${customer['total_purchases']}")


# ============================================================================
# TEST 3: LIST OF DICTIONARIES - THE MOST COMMON DATA STRUCTURE
# ============================================================================
print("\n[TEST 3] List of Dictionaries - Processing Records")
print("-" * 70)

# Scenario: Query results from database
transactions = [
    {"id": 1001, "customer": "John Doe", "amount": 250.50, "date": "2024-01-01", "status": "completed"},
    {"id": 1002, "customer": "Jane Smith", "amount": 150.00, "date": "2024-01-02", "status": "pending"},
    {"id": 1003, "customer": "Bob Johnson", "amount": 75.25, "date": "2024-01-03", "status": "completed"},
    {"id": 1004, "customer": "Alice Brown", "amount": 500.00, "date": "2024-01-04", "status": "failed"},
]

print("All Transactions:")
for trans in transactions:
    status_symbol = "[C]" if trans["status"] == "completed" else "[P]" if trans["status"] == "pending" else "[X]"
    print(f"  {status_symbol} {trans['id']}: {trans['customer']} - ${trans['amount']:.2f}")

# Filtering records
completed = [t for t in transactions if t["status"] == "completed"]
print(f"\nCompleted Transactions: {len(completed)}")
for trans in completed:
    print(f"  ${trans['amount']:.2f} - {trans['customer']}")

# Extracting a column
all_amounts = [t["amount"] for t in transactions]
total_amount = sum(all_amounts)
avg_amount = total_amount / len(all_amounts)
print(f"\nAmount Statistics:")
print(f"  Total: ${total_amount:.2f}")
print(f"  Average: ${avg_amount:.2f}")
print(f"  Highest: ${max(all_amounts):.2f}")
print(f"  Lowest: ${min(all_amounts):.2f}")

# Grouping by status
status_groups = {}
for trans in transactions:
    status = trans["status"]
    if status not in status_groups:
        status_groups[status] = []
    status_groups[status].append(trans)

print(f"\nGrouped by Status:")
for status, items in status_groups.items():
    print(f"  {status}: {len(items)} transactions (${sum(t['amount'] for t in items):.2f})")


# ============================================================================
# TEST 4: WORKING WITH TUPLES
# ============================================================================
print("\n[TEST 4] Tuples - Immutable Data")
print("-" * 70)

# Scenario: GPS coordinates, RGB colors, or returning multiple values
location = (40.7128, -74.0060)  # NYC coordinates
print(f"Location: Latitude {location[0]}, Longitude {location[1]}")

# Unpacking is very convenient
lat, lng = location
print(f"Unpacked: lat={lat}, lng={lng}")

# Functions often return tuples
def calculate_stats(numbers):
    """Return min, max, average as tuple"""
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))

amounts = [100, 250, 50, 300]
min_val, max_val, avg_val = calculate_stats(amounts)
print(f"\nAmount Statistics: min={min_val}, max={max_val}, avg={avg_val:.2f}")


# ============================================================================
# TEST 5: WORKING WITH SETS - DEDUPLICATION
# ============================================================================
print("\n[TEST 5] Sets - Finding Unique Values")
print("-" * 70)

# Scenario: Processing customer list with duplicates
customers_raw = ["John", "Jane", "John", "Bob", "Jane", "Alice", "Bob"]
print(f"Raw customer list: {customers_raw}")
print(f"Count: {len(customers_raw)}")

# Remove duplicates using set
customers_unique = set(customers_raw)
print(f"\nUnique customers: {sorted(customers_unique)}")
print(f"Count: {len(customers_unique)}")

# Scenario: Finding transaction IDs in common between two batches
batch1_ids = {1001, 1002, 1003, 1004}
batch2_ids = {1003, 1004, 1005, 1006}

print(f"\nBatch 1 IDs: {batch1_ids}")
print(f"Batch 2 IDs: {batch2_ids}")

common = batch1_ids & batch2_ids
unique_batch1 = batch1_ids - batch2_ids
unique_batch2 = batch2_ids - batch1_ids
all_combined = batch1_ids | batch2_ids

print(f"Common IDs: {common}")
print(f"Only in Batch 1: {unique_batch1}")
print(f"Only in Batch 2: {unique_batch2}")
print(f"All IDs: {all_combined}")


# ============================================================================
# TEST 6: NESTED STRUCTURES - JSON FROM APIS
# ============================================================================
print("\n[TEST 6] Nested Structures - Processing Complex JSON")
print("-" * 70)

# Scenario: API response with nested data
api_response = {
    "status": "success",
    "message": "Data retrieved successfully",
    "data": {
        "customer": {
            "id": 1001,
            "name": "John Doe",
            "account": {
                "created": "2024-01-01",
                "status": "active"
            }
        },
        "recent_transactions": [
            {"id": 101, "amount": 250.00},
            {"id": 102, "amount": 150.00},
            {"id": 103, "amount": 75.50}
        ]
    }
}

print("API Response Structure:")
print(json.dumps(api_response, indent=2))

# Extract nested data
customer_name = api_response["data"]["customer"]["name"]
account_status = api_response["data"]["customer"]["account"]["status"]
transaction_total = sum(t["amount"] for t in api_response["data"]["recent_transactions"])

print(f"\nExtracted Data:")
print(f"  Customer: {customer_name}")
print(f"  Account Status: {account_status}")
print(f"  Transaction Total: ${transaction_total:.2f}")


# ============================================================================
# TEST 7: PRACTICAL DATA PIPELINE EXAMPLE
# ============================================================================
print("\n[TEST 7] Complete Data Pipeline Example")
print("-" * 70)
print("Scenario: Read transactions, validate, process, and generate report\n")

# Step 1: Read raw data (simulating CSV or API response)
raw_data = [
    "1001|John Doe|250.50|2024-01-01|completed",
    "1002|Jane Smith|150.00|2024-01-02|pending",
    "1003|Bob Johnson|abc|2024-01-03|completed",  # Corrupt
    "1004|Alice Brown|500.00|2024-01-04|completed",
]

# Step 2: Parse and validate
transactions = []
for line in raw_data:
    parts = line.split("|")
    try:
        trans = {
            "id": int(parts[0]),
            "customer": parts[1],
            "amount": float(parts[2]),
            "date": parts[3],
            "status": parts[4]
        }
        if trans["amount"] > 0:  # Validation
            transactions.append(trans)
            print(f"[OK] Valid: {trans['customer']} - ${trans['amount']:.2f}")
        else:
            print(f"[ERROR] Invalid: Negative amount")
    except (ValueError, IndexError) as e:
        print(f"[ERROR] Error parsing: {line[:20]}... ({str(e)[:30]})")

# Step 3: Analyze
print(f"\nAnalysis:")
print(f"  Total records: {len(transactions)}")
print(f"  Total amount: ${sum(t['amount'] for t in transactions):.2f}")

completed = [t for t in transactions if t["status"] == "completed"]
print(f"  Completed: {len(completed)} - ${sum(t['amount'] for t in completed):.2f}")

# Step 4: Generate report
print(f"\nFinal Report:")
for trans in sorted(transactions, key=lambda x: x["amount"], reverse=True):
    print(f"  {trans['customer']:15} | ${trans['amount']:8.2f} | {trans['status']}")


# ============================================================================
# EXERCISE SOLUTIONS
# ============================================================================
print("\n[SOLUTIONS] Exercise Answers")
print("-" * 70)

# Solution A: Transaction processing
print("\nExercise A - Transaction Processing:")
transactions_ex = [
    {"id": 1, "amount": 100, "status": "completed"},
    {"id": 2, "amount": 250, "status": "pending"},
    {"id": 3, "amount": 50, "status": "completed"}
]

# 1. Extract amounts
all_amounts = [t["amount"] for t in transactions_ex]
print(f"  All amounts: {all_amounts}")

# 2. Total completed
completed_total = sum(t["amount"] for t in transactions_ex if t["status"] == "completed")
print(f"  Completed total: ${completed_total}")

# 3. Filter pending
pending = [t for t in transactions_ex if t["status"] == "pending"]
print(f"  Pending: {pending}")

# Solution B: Deduplication
print("\nExercise B - Deduplication:")
customers = ["John", "Jane", "John", "Bob", "Jane", "Alice"]
unique_customers = set(customers)
print(f"  Original: {customers}")
print(f"  Unique: {sorted(unique_customers)}")
print(f"  Count: {len(unique_customers)}")

# Solution C: Complex API response
print("\nExercise C - API Response:")
api_data = {
    "status": "success",
    "data": [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ],
    "metadata": {
        "total_count": 2,
        "timestamp": "2024-01-01T10:00:00"
    }
}

total = sum(item["amount"] for item in api_data["data"])
print(f"  Status: {api_data['status']}")
print(f"  Total amount: ${total}")
print(f"  Records: {api_data['metadata']['total_count']}")

# Solution D: Tuple unpacking
print("\nExercise D - Tuple Unpacking:")
def get_stats(numbers):
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))

min_v, max_v, avg_v = get_stats([10, 20, 30, 40, 50])
print(f"  Min: {min_v}, Max: {max_v}, Avg: {avg_v:.1f}")


print("\n" + "=" * 70)
print("KEY TAKEAWAYS FOR DATA ENGINEERING")
print("=" * 70)
print("""
1. LISTS: Iterate through rows of data
   - Use list comprehensions for filtering/transforming
   - Append/extend for building result sets

2. DICTIONARIES: Represent individual records
   - Use .get() for safe access with defaults
   - Iterate with .items() for key-value pairs
   - Perfect for JSON from APIs

3. LIST OF DICTS: The most common data structure
   - Each dict is a row of data
   - Filter with list comprehensions
   - Extract columns with list comprehensions
   - Group by key values

4. SETS: Find unique values and intersections
   - Remove duplicates with set()
   - Find common items with &
   - Perfect for deduplication

5. TUPLES: Return multiple values from functions
   - Use unpacking for clean code
   - More memory efficient than lists
   - Used for returning min/max/avg together

PRACTICE: Try the exercises and run this test file to see examples!
""")

print("=" * 70)
