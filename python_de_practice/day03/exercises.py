"""
DAY 03: CONTROL FLOW & FUNCTIONS
=================================
Focus: Making decisions in code and writing reusable logic

AWS Context: Every data pipeline has:
- Decision logic (if/else): Handle different data states
- Loops: Process batches of records
- Functions: Reusable validation and transformation logic
"""

# ============================================================================
# SECTION 1: IF/ELIF/ELSE - DECISION MAKING
# ============================================================================

# Exercise 1.1: Simple if statement
age = 25
if age >= 18:
    print("Adult")

# Exercise 1.2: If/else
transaction_amount = 50
if transaction_amount > 100:
    priority = "high"
else:
    priority = "normal"

# Exercise 1.3: If/elif/else (multiple conditions)
order_status = "shipped"

if order_status == "pending":
    action = "Process payment"
elif order_status == "shipped":
    action = "Track delivery"
elif order_status == "delivered":
    action = "Request review"
else:
    action = "Unknown status"

# Exercise 1.4: Nested conditions (common in validation)
transaction_amount = 250
is_verified = True

if is_verified:
    if transaction_amount <= 1000:
        can_process = True
    else:
        can_process = False
else:
    can_process = False

# Exercise 1.5: Multiple conditions with and/or
age = 25
has_credit = True
has_id = True

if age >= 18 and has_credit and has_id:
    approved = True
else:
    approved = False

# Exercise 1.6: Practical example - Data validation
def validate_email(email):
    """Check if email looks valid"""
    if email and "@" in email and "." in email:
        return True
    return False

# Exercise 1.7: Ternary operator (one-line if/else)
status = "active" if is_verified else "inactive"
priority_level = "high" if transaction_amount > 500 else "normal"


# ============================================================================
# SECTION 2: LOOPS - PROCESSING DATA
# ============================================================================

# Exercise 2.1: For loop with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Processing item {i}")

# Exercise 2.2: For loop with list
customers = ["John", "Jane", "Bob"]
for customer in customers:
    print(f"Hello {customer}")

# Exercise 2.3: For loop with enumerate (getting index and value)
transactions = [100, 250, 50]
for index, amount in enumerate(transactions):
    print(f"Transaction {index}: ${amount}")

# Exercise 2.4: For loop with dictionary
customer = {"id": 1001, "name": "John", "email": "john@example.com"}
for key, value in customer.items():
    print(f"{key}: {value}")

# Exercise 2.5: While loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# Exercise 2.6: Break statement (exit loop early)
for i in range(10):
    if i == 3:
        break
    print(i)

# Exercise 2.7: Continue statement (skip to next iteration)
for i in range(5):
    if i == 2:
        continue
    print(i)

# Exercise 2.8: Nested loops (processing 2D data)
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in data:
    for value in row:
        print(value)

# Exercise 2.9: Practical example - Processing and filtering
transactions = [
    {"id": 1, "amount": 100, "status": "completed"},
    {"id": 2, "amount": 250, "status": "pending"},
    {"id": 3, "amount": 50, "status": "completed"}
]

total_completed = 0
for trans in transactions:
    if trans["status"] == "completed":
        total_completed += trans["amount"]


# ============================================================================
# SECTION 3: FUNCTIONS - REUSABLE LOGIC
# ============================================================================

# Exercise 3.1: Basic function definition
def greet(name):
    """Greet a person by name"""
    return f"Hello, {name}!"

# Exercise 3.2: Function with multiple parameters
def calculate_total(subtotal, tax_rate):
    """Calculate total including tax"""
    tax = subtotal * tax_rate
    return subtotal + tax

# Exercise 3.3: Function with default parameters
def process_transaction(amount, status="pending", priority="normal"):
    """Process a transaction with defaults"""
    return f"Processing ${amount} - Status: {status}, Priority: {priority}"

# Exercise 3.4: Function with multiple return values
def calculate_stats(numbers):
    """Return multiple statistics"""
    return min(numbers), max(numbers), sum(numbers), len(numbers)

# Exercise 3.5: Using function returns
min_val, max_val, total, count = calculate_stats([10, 20, 30, 40])

# Exercise 3.6: Function calling function
def validate_amount(amount):
    """Check if amount is valid"""
    return amount > 0 and amount <= 100000

def process_if_valid(amount):
    """Only process if amount is valid"""
    if validate_amount(amount):
        return f"Processing ${amount}"
    else:
        return f"Invalid amount: ${amount}"

# Exercise 3.7: Function that works with lists/dicts
def sum_amounts(transactions):
    """Sum all amounts in a transaction list"""
    total = 0
    for trans in transactions:
        total += trans["amount"]
    return total

def filter_by_status(transactions, target_status):
    """Return only transactions with specific status"""
    result = []
    for trans in transactions:
        if trans["status"] == target_status:
            result.append(trans)
    return result

# Exercise 3.8: Function with error handling (preview)
def safe_divide(a, b):
    """Divide safely"""
    if b == 0:
        return None
    return a / b

# Exercise 3.9: Practical example - Data transformation
def format_transaction(trans):
    """Transform transaction to string"""
    return f"{trans['id']}: {trans['amount']} ({trans['status']})"

def format_transactions(transactions):
    """Format a list of transactions"""
    result = []
    for trans in transactions:
        formatted = format_transaction(trans)
        result.append(formatted)
    return result


# ============================================================================
# SECTION 4: LAMBDA FUNCTIONS - SIMPLE ONE-LINE FUNCTIONS
# ============================================================================

# Exercise 4.1: Simple lambda
square = lambda x: x ** 2

# Exercise 4.2: Lambda with multiple parameters
add = lambda x, y: x + y

# Exercise 4.3: Lambdas with built-in functions like map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# Exercise 4.4: Lambdas with filter
amounts = [10, 250, 50, 500]
large_amounts = list(filter(lambda x: x > 100, amounts))

# Exercise 4.5: Lambdas with sorted
transactions = [
    {"id": 1, "amount": 250},
    {"id": 2, "amount": 100},
    {"id": 3, "amount": 500}
]
sorted_by_amount = sorted(transactions, key=lambda t: t["amount"])


# ============================================================================
# SECTION 5: SCOPE - WHERE VARIABLES EXIST
# ============================================================================

# Exercise 5.1: Global scope
global_var = "I'm global"

def show_global():
    print(global_var)  # Can access global

# Exercise 5.2: Local scope
def local_example():
    local_var = "I'm local"
    print(local_var)

# local_var here would cause an error - it doesn't exist outside the function

# Exercise 5.3: Parameter scope
def add_values(a, b):  # a and b are local to this function
    return a + b

# Exercise 5.4: Practical example - Variable scope in loops
results = []
for i in range(3):
    result = i * 2
    results.append(result)

# 'result' still exists here after loop (Python doesn't have block scope)


# ============================================================================
# SECTION 6: PRACTICAL REAL-WORLD EXAMPLES
# ============================================================================

# Example 1: Data validation pipeline
def validate_transaction(trans_dict):
    """Complete validation of a transaction"""
    
    # Check all required fields exist
    required_fields = ["id", "amount", "status"]
    for field in required_fields:
        if field not in trans_dict:
            return False, f"Missing field: {field}"
    
    # Validate amount
    if trans_dict["amount"] <= 0:
        return False, "Amount must be positive"
    
    if trans_dict["amount"] > 100000:
        return False, "Amount exceeds limit"
    
    # Validate status
    valid_statuses = ["pending", "completed", "failed"]
    if trans_dict["status"] not in valid_statuses:
        return False, f"Invalid status: {trans_dict['status']}"
    
    return True, "Valid transaction"

# Example 2: Data processing pipeline
def process_transactions(raw_transactions):
    """Process raw transactions and return results"""
    
    processed = []
    errors = []
    
    for trans in raw_transactions:
        is_valid, message = validate_transaction(trans)
        
        if is_valid:
            # Only keep completed transactions
            if trans["status"] == "completed":
                processed.append(trans)
        else:
            errors.append({"transaction": trans, "error": message})
    
    return {
        "processed": processed,
        "total": sum(t["amount"] for t in processed),
        "errors": errors
    }

# Example 3: Complex filter and transform
def get_high_value_customers(transactions, min_amount=500):
    """Find customers with high transaction amounts"""
    
    customers = {}
    for trans in transactions:
        customer = trans["customer"]
        amount = trans["amount"]
        
        if customer not in customers:
            customers[customer] = []
        customers[customer].append(amount)
    
    # Filter to customers with high transactions
    high_value = {}
    for customer, amounts in customers.items():
        total = sum(amounts)
        if total >= min_amount:
            high_value[customer] = {
                "count": len(amounts),
                "total": total,
                "average": total / len(amounts)
            }
    
    return high_value


# ============================================================================
# PRACTICAL EXERCISES FOR YOU TO COMPLETE
# ============================================================================

# TODO Exercise A: Write a function to validate email
# - Check if it has @
# - Check if it has a domain (. after @)
# - Return True if valid, False otherwise

# TODO Exercise B: Write a function to process order list
# - Take a list of orders with amounts
# - Filter orders > 100
# - Calculate total
# - Return dict with count and total

# TODO Exercise C: Write a function to categorize transactions
# - Take a list of transactions
# - Categorize by amount: small (< 100), medium (100-500), large (> 500)
# - Return a dict with counts for each category

# TODO Exercise D: Nested function example
# - Write a function that checks if a number is valid
# - Inside, write a nested function that checks if it's even
# - Use both in validation logic


if __name__ == "__main__":
    print("Day 03: Control Flow & Functions")
    print("=" * 60)
    
    # Test functions
    print(f"\nGreeting: {greet('John')}")
    print(f"Total with tax: ${calculate_total(100, 0.08)}")
    
    # Test validation
    trans = {"id": 1, "amount": 250, "status": "completed"}
    is_valid, msg = validate_transaction(trans)
    print(f"\nValidation: {msg}")
