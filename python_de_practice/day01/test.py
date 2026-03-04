"""
DAY 01: TEST FILE & SOLUTIONS
==============================
Run this file to see examples and expected output.
Compare your code with these examples.
"""

import os

print("=" * 70)
print("DAY 01: PYTHON FUNDAMENTALS & DATA TYPES - TEST & EXAMPLES")
print("=" * 70)


# ============================================================================
# TEST 1: VARIABLE AND DATA TYPE DEMONSTRATIONS
# ============================================================================
print("\n[TEST 1] Variables and Data Types")
print("-" * 70)

# Transaction data structure
transaction_id = 1001
transaction_date = "2024-01-01"
transaction_amount = 250.50
is_approved = True

print(f"Transaction ID (int): {transaction_id}, Type: {type(transaction_id)}")
print(f"Date (str): {transaction_date}, Type: {type(transaction_date)}")
print(f"Amount (float): {transaction_amount}, Type: {type(transaction_amount)}")
print(f"Approved (bool): {is_approved}, Type: {type(is_approved)}")


# ============================================================================
# TEST 2: TYPE CASTING IN DATA PIPELINES
# ============================================================================
print("\n[TEST 2] Type Casting - Converting Between Types")
print("-" * 70)

# Scenario: Receiving data from an API (everything comes as strings)
api_response = "1001|John Doe|249.99"
parts = api_response.split("|")
customer_id = int(parts[0])  # Convert string to int
customer_name = parts[1]      # Keep as string
amount = float(parts[2])      # Convert string to float

print(f"Raw API Response: {api_response}")
print(f"Parsed:")
print(f"  - Customer ID: {customer_id} (type: {type(customer_id).__name__})")
print(f"  - Customer Name: {customer_name} (type: {type(customer_name).__name__})")
print(f"  - Amount: {amount} (type: {type(amount).__name__})")


# ============================================================================
# TEST 3: STRING MANIPULATION - CRITICAL FOR DATA PROCESSING
# ============================================================================
print("\n[TEST 3] String Manipulation & F-strings")
print("-" * 70)

# Real-world example: formatting output for logs
log_timestamp = "2024-01-01 10:30:45"
log_level = "INFO"
log_message = "Transaction processed successfully"
transaction_amount = 250.50
customer_name = "John Doe"

# Method 1: F-string (PREFERRED - modern and readable)
formatted_log = f"[{log_timestamp}] {log_level}: {log_message} for {customer_name} (${transaction_amount})"
print(f"Formatted Log:\n  {formatted_log}")

# Method 2: String methods
dirty_email = "  CUSTOMER@EXAMPLE.COM  "
clean_email = dirty_email.strip().lower()
print(f"\nEmail cleaning:")
print(f"  Original: '{dirty_email}'")
print(f"  Cleaned:  '{clean_email}'")

# Method 3: Splitting CSV data
csv_line = "1001,John Doe,250.50,2024-01-01,completed"
fields = csv_line.split(",")
print(f"\nCSV Parsing:")
print(f"  Raw: {csv_line}")
print(f"  Parsed fields: {fields}")
print(f"  Customer ID: {fields[0]}, Name: {fields[1]}, Amount: ${fields[2]}")


# ============================================================================
# TEST 4: ARITHMETIC OPERATIONS FOR DATA CALCULATIONS
# ============================================================================
print("\n[TEST 4] Arithmetic Operations")
print("-" * 70)

# Scenario: Calculate invoice totals
products = [
    {"name": "Laptop", "price": 1000.00, "quantity": 1},
    {"name": "Mouse", "price": 25.00, "quantity": 2},
    {"name": "Keyboard", "price": 75.00, "quantity": 1}
]

total_before_tax = 0
for product in products:
    line_total = product["price"] * product["quantity"]
    total_before_tax += line_total
    print(f"  {product['name']}: ${product['price']} × {product['quantity']} = ${line_total}")

tax_rate = 0.08
tax_amount = total_before_tax * tax_rate
total_with_tax = total_before_tax + tax_amount

print(f"\nSummary:")
print(f"  Subtotal: ${total_before_tax:.2f}")
print(f"  Tax (8%): ${tax_amount:.2f}")
print(f"  Total: ${total_with_tax:.2f}")


# ============================================================================
# TEST 5: LOGICAL OPERATIONS & VALIDATION
# ============================================================================
print("\n[TEST 5] Logical Operations & Validation")
print("-" * 70)

def validate_transaction_record(trans_id, amount, email):
    """Validate a transaction record before processing"""
    
    # Check conditions
    valid_id = trans_id > 0 and trans_id < 1000000
    valid_amount = amount > 0 and amount <= 100000
    valid_email = "@" in email and "." in email
    
    # All conditions must be true
    is_valid = valid_id and valid_amount and valid_email
    
    # Build result message
    checks = {
        "ID Valid": valid_id,
        "Amount Valid": valid_amount,
        "Email Valid": valid_email,
        "Overall": is_valid
    }
    
    return is_valid, checks

# Test transactions
test_cases = [
    (1001, 250.50, "customer@example.com"),
    (0, 250.50, "customer@example.com"),  # Invalid ID
    (1001, -100, "customer@example.com"),  # Invalid amount
    (1001, 250.50, "invalid-email"),  # Invalid email
]

for trans_id, amount, email in test_cases:
    is_valid, checks = validate_transaction_record(trans_id, amount, email)
    print(f"\nTransaction: ID={trans_id}, Amount={amount}, Email={email}")
    for check_name, result in checks.items():
        print(f"  {check_name}: {'✓' if result else '✗'}")


# ============================================================================
# TEST 6: PRACTICAL DATA PIPELINE EXAMPLE
# ============================================================================
print("\n[TEST 6] Data Pipeline Example - Processing Raw Data")
print("-" * 70)

# Raw data as it might come from CSV file
raw_transaction = "1001,John Doe,250.50,2024-01-01,true"

print(f"Raw Input: {raw_transaction}")

# Parse and convert types
parts = raw_transaction.split(",")
trans_id = int(parts[0])
customer_name = parts[1].strip()
amount = float(parts[2])
date = parts[3]
is_approved = parts[4].lower() == "true"

# Validate
amount_is_valid = amount > 0
id_is_valid = trans_id > 0

if amount_is_valid and id_is_valid:
    # Format for output/storage
    output = f"TRANSACTION {trans_id}: {customer_name} | ${amount:.2f} | {date} | {'APPROVED' if is_approved else 'PENDING'}"
    print(f"Processed Output: {output}")
else:
    print("ERROR: Transaction data is invalid")


# ============================================================================
# TEST 7: EXERCISE SOLUTIONS
# ============================================================================
print("\n[TEST 7] Exercise Solutions")
print("-" * 70)

# Solution A: Customer Purchase Calculation
print("\nExercise A - Customer Purchase:")
customer_name = "John Doe"
product_name = "Laptop"
unit_price = 999.99
quantity = 1
tax_rate = 0.08

total_before_tax = unit_price * quantity
tax_amount = total_before_tax * tax_rate
total_with_tax = total_before_tax + tax_amount

print(f"  Customer: {customer_name}")
print(f"  Product: {product_name}")
print(f"  Unit Price: ${unit_price}")
print(f"  Quantity: {quantity}")
print(f"  Subtotal: ${total_before_tax:.2f}")
print(f"  Tax: ${tax_amount:.2f}")
print(f"  Total: ${total_with_tax:.2f}")

# Solution B: Parse Transaction Record
print("\nExercise B - Parse Transaction Record:")
transaction_record = "1001,John Doe,250.50,2024-01-01"
trans_id_str, customer_name_str, amount_str, date_str = transaction_record.split(",")

# Convert types
trans_id = int(trans_id_str)
amount = float(amount_str)

formatted = f"Customer {customer_name_str} (ID: {trans_id}) spent ${amount}"
print(f"  Input: {transaction_record}")
print(f"  Output: {formatted}")

# Solution C: Validation Function
print("\nExercise C - Validation Function:")

def is_valid_number(num):
    """Check if number is between 0 and 1000"""
    return 0 <= num <= 1000

test_numbers = [50, 500, 1000, 1500, -10, 0]
for num in test_numbers:
    result = is_valid_number(num)
    print(f"  {num}: {'Valid' if result else 'Invalid'}")

# Solution D: String Manipulation
print("\nExercise D - String Manipulation:")
original = "  AWS DATA ENGINEERING  "
cleaned = original.strip().lower()
final = f"Course: {cleaned}"
print(f"  Original: '{original}'")
print(f"  Cleaned: '{cleaned}'")
print(f"  Final: '{final}'")


# ============================================================================
# KEY TAKEAWAYS FOR AWS DATA ENGINEERING
# ============================================================================
print("\n" + "=" * 70)
print("KEY TAKEAWAYS FOR AWS DATA ENGINEERING")
print("=" * 70)
print("""
1. DATA TYPES: Every AWS data pipeline deals with types
   - Strings: Customer names, emails, addresses
   - Numbers: Prices, quantities, IDs
   - Booleans: Valid/invalid, approved/rejected
   - None: Missing values, optional fields

2. TYPE CONVERSION: Critical when reading from S3, APIs, databases
   - JSON/CSV always comes as strings initially
   - Must convert to appropriate types before calculations

3. STRING MANIPULATION: Processing text data is core to DE
   - Splitting: Parse CSV/delimited data
   - Joining: Combine fields for output
   - Cleaning: Remove whitespace, normalize case
   - Formatting: Create logs, messages, error reports

4. VALIDATION: Every pipeline needs data quality checks
   - Verify ranges (amount > 0, age < 150)
   - Check required fields (not None)
   - Validate formats (email has @, date format correct)

5. F-STRINGS: Use f"..." for all string formatting
   - More readable than format() or %
   - Allows expressions inside {}
   - Standard in modern Python (3.6+)

NEXT STEP: Work through the exercises in exercises.py
""")

print("=" * 70)
