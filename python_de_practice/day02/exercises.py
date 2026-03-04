"""
DAY 02: DATA STRUCTURES - LISTS, DICTS, TUPLES, SETS
=====================================================
Focus: Working with collections that power data pipelines

AWS Context: Every data pipeline works with collections.
- Lists: Rows of data, processing sequences
- Dicts: JSON objects from APIs, database records
- Tuples: Immutable records, function returns
- Sets: Finding unique values, deduplication

This is one of the MOST IMPORTANT topics for data engineering!
"""

# ============================================================================
# SECTION 1: LISTS - THE FOUNDATION FOR DATA PIPELINES
# ============================================================================

# Exercise 1.1: Creating lists
transaction_ids = [1001, 1002, 1003, 1004, 1005]
customer_names = ["John Doe", "Jane Smith", "Bob Johnson"]
mixed_data = [1001, "John Doe", 250.50, True]  # Can mix types
empty_list = []

# Exercise 1.2: Accessing list elements (indexing)
# Remember: Python uses 0-based indexing
first_transaction = transaction_ids[0]  # 1001
last_transaction = transaction_ids[-1]  # 1005 (negative index)
second_customer = customer_names[1]  # "Jane Smith"

# Exercise 1.3: List slicing (getting subsets)
first_three_ids = transaction_ids[0:3]  # [1001, 1002, 1003]
all_but_last = transaction_ids[:-1]  # All except last
every_second = transaction_ids[::2]  # Every 2nd element

# Exercise 1.4: Adding elements to lists
transaction_ids.append(1006)  # Add to end
customer_names.extend(["Alice Brown", "Charlie Davis"])  # Add multiple
transaction_ids.insert(0, 1000)  # Insert at position

# Exercise 1.5: Removing elements
transaction_ids.pop()  # Remove last element
transaction_ids.remove(1000)  # Remove by value
del transaction_ids[0]  # Delete by index

# Exercise 1.6: Common list operations
length = len(transaction_ids)  # How many elements
contains_1002 = 1002 in transaction_ids  # Check membership
sorted_ids = sorted(transaction_ids)  # Sort list
reversed_ids = list(reversed(transaction_ids))  # Reverse

# Exercise 1.7: List iteration - VERY COMMON in data pipelines
for trans_id in transaction_ids:
    print(f"Processing transaction: {trans_id}")

# Exercise 1.8: Practical example - Processing transaction data
raw_amounts = ["100.50", "250.75", "abc", "50.00"]  # Some data might be corrupt
valid_amounts = []
for amount_str in raw_amounts:
    try:
        amount = float(amount_str)
        if amount > 0:  # Validation
            valid_amounts.append(amount)
    except ValueError:
        print(f"Invalid amount: {amount_str}")


# ============================================================================
# SECTION 2: DICTIONARIES - ESSENTIAL FOR API/JSON DATA
# ============================================================================

# Exercise 2.1: Creating dictionaries (key-value pairs)
customer = {
    "id": 1001,
    "name": "John Doe",
    "email": "john@example.com",
    "is_active": True
}

# Exercise 2.2: Accessing dictionary values
customer_id = customer["id"]  # Direct access
customer_name = customer.get("name")  # Safe access (returns None if not found)
missing_field = customer.get("phone", "N/A")  # Default value if missing

# Exercise 2.3: Adding/updating dictionary items
customer["phone"] = "555-1234"  # Add new key
customer["email"] = "newemail@example.com"  # Update existing

# Exercise 2.4: Removing items from dictionary
del customer["phone"]  # Delete by key
popped_value = customer.pop("is_active")  # Remove and get value

# Exercise 2.5: Dictionary methods
keys = customer.keys()  # Get all keys
values = customer.values()  # Get all values
items = customer.items()  # Get key-value pairs

# Exercise 2.6: Checking membership
has_id = "id" in customer  # Check if key exists
has_phone = "phone" in customer  # False (we deleted it)

# Exercise 2.7: Iterating over dictionaries
for key, value in customer.items():
    print(f"{key}: {value}")

# Exercise 2.8: Practical example - Processing API response (very common!)
api_response = {
    "status": "success",
    "data": [
        {"id": 1001, "amount": 250.50, "status": "completed"},
        {"id": 1002, "amount": 150.00, "status": "pending"},
        {"id": 1003, "amount": 75.25, "status": "completed"}
    ],
    "total_records": 3
}

# Extract and process data
if api_response["status"] == "success":
    transactions = api_response["data"]
    total_amount = 0
    for transaction in transactions:
        if transaction["status"] == "completed":
            total_amount += transaction["amount"]
    print(f"Total completed: ${total_amount}")


# ============================================================================
# SECTION 3: LIST OF DICTIONARIES - THE MOST COMMON DATA STRUCTURE
# ============================================================================

# Exercise 3.1: Creating records (list of dicts - like CSV rows)
transactions = [
    {"id": 1001, "customer": "John Doe", "amount": 250.50, "date": "2024-01-01"},
    {"id": 1002, "customer": "Jane Smith", "amount": 150.00, "date": "2024-01-02"},
    {"id": 1003, "customer": "Bob Johnson", "amount": 75.25, "date": "2024-01-03"}
]

# Exercise 3.2: Processing records
for transaction in transactions:
    print(f"Transaction {transaction['id']}: {transaction['customer']} - ${transaction['amount']}")

# Exercise 3.3: Filtering records (find specific ones)
high_value_transactions = [t for t in transactions if t["amount"] > 100]  # List comprehension

# Exercise 3.4: Transforming records
transaction_summaries = [
    f"{t['customer']}: ${t['amount']}" for t in transactions
]

# Exercise 3.5: Extracting a column
all_amounts = [t["amount"] for t in transactions]
total = sum(all_amounts)
average = total / len(all_amounts)


# ============================================================================
# SECTION 4: TUPLES - IMMUTABLE SEQUENCES
# ============================================================================

# Exercise 4.1: Creating tuples (immutable = can't change after creation)
coordinates = (40.7128, -74.0060)  # Latitude, Longitude
rgb_color = (255, 0, 0)  # Red
record = (1001, "John Doe", 250.50)  # Mixed types

# Exercise 4.2: Accessing tuple elements (same as lists)
lat = coordinates[0]
lng = coordinates[1]

# Exercise 4.3: Unpacking tuples (convenient!)
lat, lng = coordinates
id_val, name, amount = record

# Exercise 4.4: Tuples are useful for returning multiple values
def get_min_max(numbers):
    """Return both min and max"""
    return (min(numbers), max(numbers))

min_amount, max_amount = get_min_max([100, 250, 50])

# Exercise 4.5: Iterating over tuples
for value in rgb_color:
    print(f"Value: {value}")

# Note: You cannot modify tuples - this would cause an error:
# coordinates[0] = 40.7200  # ERROR!


# ============================================================================
# SECTION 5: SETS - UNIQUE VALUES AND OPERATIONS
# ============================================================================

# Exercise 5.1: Creating sets (unique values only)
unique_ids = {1001, 1002, 1003, 1001}  # Duplicates removed automatically
# unique_ids = {1001, 1002, 1003}

unique_statuses = {"completed", "pending", "failed"}
empty_set = set()  # Empty set (must use set(), not {})

# Exercise 5.2: Adding/removing from sets
unique_ids.add(1004)
unique_ids.discard(1001)  # Remove if exists (no error if missing)

# Exercise 5.3: Set operations (very powerful!)
ids_batch1 = {1001, 1002, 1003}
ids_batch2 = {1003, 1004, 1005}

# Union: all unique IDs from both batches
all_ids = ids_batch1 | ids_batch2  # {1001, 1002, 1003, 1004, 1005}

# Intersection: IDs in both batches
common_ids = ids_batch1 & ids_batch2  # {1003}

# Difference: IDs in batch1 but not batch2
unique_to_batch1 = ids_batch1 - ids_batch2  # {1001, 1002}

# Exercise 5.4: Checking membership
has_1001 = 1001 in ids_batch1
has_1006 = 1006 in ids_batch1  # False

# Exercise 5.5: Converting between types
list_of_ids = [1001, 1002, 1003, 1001, 1002]  # Has duplicates
unique_from_list = set(list_of_ids)  # Remove duplicates
back_to_list = list(unique_from_list)


# ============================================================================
# SECTION 6: NESTED STRUCTURES - REAL-WORLD COMPLEXITY
# ============================================================================

# Exercise 6.1: Nested dictionaries (common in JSON from APIs)
customer_with_details = {
    "id": 1001,
    "name": "John Doe",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    },
    "recent_purchases": [
        {"item": "Laptop", "amount": 1000},
        {"item": "Mouse", "amount": 25}
    ]
}

# Accessing nested data
city = customer_with_details["address"]["city"]
first_purchase = customer_with_details["recent_purchases"][0]["item"]

# Exercise 6.2: Nested lists
teams = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eve"],
    ["Frank", "Grace", "Henry"]
]

first_team_second_member = teams[0][1]  # "Bob"


# ============================================================================
# PRACTICAL EXERCISES FOR YOU TO COMPLETE
# ============================================================================

# TODO Exercise A: Work with transaction list
# Given transactions = [
#     {"id": 1, "amount": 100, "status": "completed"},
#     {"id": 2, "amount": 250, "status": "pending"},
#     {"id": 3, "amount": 50, "status": "completed"}
# ]
# 1. Extract all amounts into a list
# 2. Calculate total of completed transactions
# 3. Filter pending transactions

# TODO Exercise B: Deduplicate data using sets
# Given: customers = ["John", "Jane", "John", "Bob", "Jane", "Alice"]
# 1. Get unique customers
# 2. Count unique customers
# 3. Convert back to sorted list

# TODO Exercise C: Parse a complex API response
# Build a dictionary representing an API response with:
# - status (string)
# - data (list of transaction objects)
# - metadata (dict with total_count and timestamp)
# Extract and process the data

# TODO Exercise D: Tuple unpacking
# Create a function that returns (min_value, max_value, average) for a list of numbers
# Call it with [10, 20, 30, 40, 50] and unpack the results


if __name__ == "__main__":
    print("Day 02: Data Structures - Lists, Dicts, Tuples, Sets")
    print("=" * 60)
    
    # Show some examples
    print(f"\nExample - Transaction Processing:")
    for trans in transactions[:2]:  # First 2
        print(f"  {trans['customer']}: ${trans['amount']} on {trans['date']}")
    
    print(f"\nExample - Set Operations:")
    print(f"  Batch 1 IDs: {ids_batch1}")
    print(f"  Batch 2 IDs: {ids_batch2}")
    print(f"  Common IDs: {common_ids}")
    print(f"  All IDs: {all_ids}")
