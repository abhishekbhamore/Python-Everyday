
"""
DAY 01: Python Fundamentals & Data Types
==========================================
Focus: Variables, data types, type casting, string manipulation, and basic operations

AWS Context: These fundamentals are used in every data pipeline for data validation,
transformation, and preparing data for AWS services.
"""

# ============================================================================
# SECTION 1: VARIABLES AND NAMING CONVENTIONS
# ============================================================================

# Exercise 1.1: Create variables for transaction data
transaction_id = 1001
transaction_date = "2024-01-01"
transaction_amount = 250.50
is_approved = True

# Exercise 1.2: Use meaningful variable names (snake_case for Python)
customer_name = "John Doe"
order_value = 99.99
payment_method = "credit_card"


# ============================================================================
# SECTION 2: DATA TYPES - THE FOUNDATIONS
# ============================================================================

# Exercise 2.1: Integers (whole numbers, used for IDs, counts)
customer_id = 12345
transaction_count = 5
records_processed = 1000

# Exercise 2.2: Floats (decimal numbers, used for prices, measurements)
product_price = 19.99
tax_rate = 0.08
discount_percentage = 15.5

# Exercise 2.3: Strings (text data, very common in data pipelines)
customer_email = "customer@example.com"
order_status = "completed"
error_message = "Connection timeout"

# Exercise 2.4: Booleans (True/False, used for validation checks)
is_valid_data = True
is_duplicate = False
processing_successful = True


# ============================================================================
# SECTION 3: TYPE CASTING - CONVERTING BETWEEN TYPES
# ============================================================================

# Exercise 3.1: String to Integer (common when reading from files/APIs)
user_input_age = "25"
age_as_integer = int(user_input_age)  # "25" → 25

# Exercise 3.2: String to Float (prices often come as strings)
price_as_string = "99.99"
price_as_float = float(price_as_string)  # "99.99" → 99.99

# Exercise 3.3: Integer to String (preparing data for output/storage)
record_number = 42
record_as_string = str(record_number)  # 42 → "42"

# Exercise 3.4: To Boolean (checking if values are truthy/falsy)
value = 0
is_truthy = bool(value)  # 0 is False, any other number is True


# ============================================================================
# SECTION 4: STRING MANIPULATION - CORE TO DATA PROCESSING
# ============================================================================

# Exercise 4.1: String concatenation (joining strings together)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# Exercise 4.2: F-strings (modern, readable string formatting - PREFERRED)
customer_id = 1001
order_amount = 250.50
message = f"Customer {customer_id} ordered ${order_amount}"

# Exercise 4.3: String methods (common operations)
email = "  CUSTOMER@EXAMPLE.COM  "
email_cleaned = email.strip().lower()  # Remove spaces, convert to lowercase

# Exercise 4.4: String splitting (parsing CSV-like data)
csv_row = "1001,2024-01-01,250.50"
parts = csv_row.split(",")  # ["1001", "2024-01-01", "250.50"]

# Exercise 4.5: String joining (creating output)
transaction_parts = ["ID", "1001", "Date", "2024-01-01", "Amount", "250.50"]
formatted_output = " | ".join(transaction_parts)


# ============================================================================
# SECTION 5: BASIC ARITHMETIC OPERATIONS
# ============================================================================

# Exercise 5.1: Basic math operations
item_price = 50.00
quantity = 3
total_cost = item_price * quantity  # 150.00

# Exercise 5.2: Tax calculation (common in data pipelines)
subtotal = 100.00
tax_rate = 0.08
tax_amount = subtotal * tax_rate  # 8.00
total_with_tax = subtotal + tax_amount  # 108.00

# Exercise 5.3: Percentage calculations (used for metrics)
total_records = 1000
processed_records = 850
success_rate = (processed_records / total_records) * 100  # 85.0%

# Exercise 5.4: Power and modulo operations
# Power: useful for calculations
result = 2 ** 8  # 256 (2 to the power of 8)

# Modulo: useful for finding remainders (odd/even checks, batching)
remainder = 17 % 5  # 2


# ============================================================================
# SECTION 6: LOGICAL OPERATIONS - DECISION MAKING
# ============================================================================

# Exercise 6.1: Comparison operators
age = 25
is_adult = age >= 18  # True
is_senior = age >= 65  # False

# Exercise 6.2: Logical AND (all conditions must be true)
has_valid_id = True
has_payment_method = True
can_process = has_valid_id and has_payment_method  # True

# Exercise 6.3: Logical OR (at least one condition must be true)
payment_by_card = True
payment_by_cash = False
has_payment = payment_by_card or payment_by_cash  # True

# Exercise 6.4: NOT operator (negation)
is_error = True
is_success = not is_error  # False


# ============================================================================
# SECTION 7: PRACTICAL DATA VALIDATION EXAMPLE
# ============================================================================

def validate_transaction():
    """Real-world example: validating a transaction for AWS data pipeline"""
    
    # Simulate receiving transaction data
    transaction_id = "1001"
    amount_str = "250.50"
    date_str = "2024-01-01"
    
    # Convert types
    trans_id = int(transaction_id)
    amount = float(amount_str)
    
    # Validate
    is_valid_amount = amount > 0
    is_valid_id = trans_id > 0
    
    # Create output message
    if is_valid_amount and is_valid_id:
        result = f"Transaction {trans_id} for ${amount} on {date_str} is VALID"
    else:
        result = "Transaction INVALID - check data"
    
    return result


# ============================================================================
# SECTION 8: WORKING WITH SPECIAL VALUES
# ============================================================================

# Exercise 8.1: None (represents absence of value - common in data)
optional_middle_name = None
discount_applied = None  # No discount given

# Exercise 8.2: Type checking
value = "100"
print(type(value))  # <class 'str'>
print(type(int(value)))  # <class 'int'>


# ============================================================================
# PRACTICAL EXERCISES FOR YOU TO COMPLETE
# ============================================================================

# TODO Exercise A: Create variables for a customer purchase
# - customer_name (string)
customer_name = "karan johoar"
# - product_name (string)
product_name = "laptop"
# - unit_price (float)
unit_price = 99.99
# - quantity (integer)
quantity = 2
# - tax_rate (float - use 0.08 for 8%)
tax_rate = 0.08  # Changed from 0.3 to 0.08 as instructed
# - Calculate: total_before_tax, tax_amount, total_with_tax
total_before_tax = unit_price * quantity
tax_amount = total_before_tax * tax_rate
total_with_tax = total_before_tax + tax_amount


# TODO Exercise B: Parse and validate a transaction record
# Given: "1001,John Doe,250.50,2024-01-01"
# Split it and create variables for each field
# Convert types appropriately
# Create a formatted message: "Customer John Doe (ID: 1001) spent $250.50"

transaction_record = "1001,John Doe,250.50,2024-01-01"
parts = transaction_record.split(",")
trans_id = int(parts[0])
customer_name_b = parts[1]
amount = float(parts[2])
date = parts[3]
formatted_message = f"Customer {customer_name_b} (ID: {trans_id}) spent ${amount}"


# TODO Exercise C: Create a data validation function
# Function should check if a number is between 0 and 1000
# Return True if valid, False otherwise

def is_valid_number(num):
    """Check if number is between 0 and 1000"""
    return 0 <= num <= 1000


# TODO Exercise D: String manipulation
# Take the string: "  AWS DATA ENGINEERING  "
# Clean it (remove spaces), convert to lowercase
# Add a prefix: "Course: "
# Print the result

original_string = "  AWS DATA ENGINEERING  "
cleaned_string = original_string.strip().lower()
final_string = f"Course: {cleaned_string}"


if __name__ == "__main__":
    # This runs when script is executed directly
    print("Day 01: Python Fundamentals & Data Types")
    print("=" * 70)
    
    # Exercise A Results
    print("\n[Exercise A] Customer Purchase Calculation:")
    print(f"  Customer: {customer_name}")
    print(f"  Product: {product_name}")
    print(f"  Unit Price: ${unit_price}")
    print(f"  Quantity: {quantity}")
    print(f"  Subtotal: ${total_before_tax:.2f}")
    print(f"  Tax (8%): ${tax_amount:.2f}")
    print(f"  Total: ${total_with_tax:.2f}")
    
    # Exercise B Results
    print("\n[Exercise B] Parse Transaction Record:")
    print(f"  {formatted_message}")
    
    # Exercise C Results
    print("\n[Exercise C] Validation Function:")
    test_values = [50, 500, 1000, 1001, -10, 0]
    for val in test_values:
        result = is_valid_number(val)
        status = "Valid" if result else "Invalid"
        print(f"  {val}: {status}")
    
    # Exercise D Results
    print("\n[Exercise D] String Manipulation:")
    print(f"  Original: '{original_string}'")
    print(f"  Result: '{final_string}'")
    
    # Original examples from earlier sections
    print("\n" + "=" * 70)
    print("[Earlier Examples]")
    print(f"Example 1: Full name = {full_name}")
    print(f"Example 2: {message}")
    print(f"Example 3: {formatted_output}")
    print(f"Example 4: Total cost with tax = ${total_with_tax}")
    print(f"Example 5: {validate_transaction()}")
