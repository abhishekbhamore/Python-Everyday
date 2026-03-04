"""
DAY 03: CONTROL FLOW & FUNCTIONS - TEST & SOLUTIONS
====================================================
Run this file to see control flow and function examples.
"""

print("=" * 70)
print("DAY 03: CONTROL FLOW & FUNCTIONS - TEST & SOLUTIONS")
print("=" * 70)


# ============================================================================
# TEST 1: IF/ELIF/ELSE DECISION MAKING
# ============================================================================
print("\n[TEST 1] If/Elif/Else Decisions")
print("-" * 70)

# Scenario: Processing orders based on amount
amounts = [50, 250, 500, 1000, 2000]

for amount in amounts:
    if amount < 100:
        category = "Small"
        fee = 0
    elif amount < 500:
        category = "Medium"
        fee = 5
    elif amount < 1000:
        category = "Large"
        fee = 10
    else:
        category = "Enterprise"
        fee = 25
    
    print(f"${amount:5} → {category:12} (Fee: ${fee})")


# ============================================================================
# TEST 2: VALIDATION LOGIC
# ============================================================================
print("\n[TEST 2] Practical Validation")
print("-" * 70)

def validate_email(email):
    """Validate email format"""
    if not email:
        return False
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True

test_emails = [
    "john@example.com",
    "jane@domain.co.uk",
    "invalid.email",
    "no@domain",
    ""
]

for email in test_emails:
    valid = validate_email(email)
    status = "✓" if valid else "✗"
    print(f"{status} {email:20} - {'Valid' if valid else 'Invalid'}")


# ============================================================================
# TEST 3: FOR LOOPS - PROCESSING DATA
# ============================================================================
print("\n[TEST 3] For Loops - Data Processing")
print("-" * 70)

# Scenario: Processing transaction records
transactions = [
    {"id": 1001, "customer": "John Doe", "amount": 250.50},
    {"id": 1002, "customer": "Jane Smith", "amount": 150.00},
    {"id": 1003, "customer": "Bob Johnson", "amount": 500.25}
]

print("Processing transactions:")
total = 0
for index, trans in enumerate(transactions, 1):
    total += trans["amount"]
    print(f"  {index}. {trans['customer']:15} - ${trans['amount']:7.2f}")

print(f"Total: ${total:.2f}")


# ============================================================================
# TEST 4: FILTERING WITH LOOPS
# ============================================================================
print("\n[TEST 4] Filtering Data")
print("-" * 70)

# Method 1: Traditional for loop
orders = [
    {"id": 1, "amount": 75},
    {"id": 2, "amount": 250},
    {"id": 3, "amount": 50},
    {"id": 4, "amount": 500},
    {"id": 5, "amount": 100}
]

print("Method 1: Traditional for loop")
high_value = []
for order in orders:
    if order["amount"] > 100:
        high_value.append(order)

for order in high_value:
    print(f"  Order {order['id']}: ${order['amount']}")

# Method 2: List comprehension
print("\nMethod 2: List comprehension (more Pythonic)")
high_value_2 = [o for o in orders if o["amount"] > 100]
for order in high_value_2:
    print(f"  Order {order['id']}: ${order['amount']}")


# ============================================================================
# TEST 5: BASIC FUNCTIONS
# ============================================================================
print("\n[TEST 5] Functions - Reusable Code")
print("-" * 70)

# Simple calculation function
def calculate_total_with_tax(subtotal, tax_rate=0.08):
    """Calculate total including tax"""
    tax = subtotal * tax_rate
    total = subtotal + tax
    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": total,
        "tax_rate": tax_rate
    }

# Use the function
result = calculate_total_with_tax(100)
print(f"Invoice Calculation:")
print(f"  Subtotal: ${result['subtotal']:.2f}")
print(f"  Tax (8%): ${result['tax']:.2f}")
print(f"  Total: ${result['total']:.2f}")

# Use with custom tax rate
result_no_tax = calculate_total_with_tax(100, tax_rate=0)
print(f"\nNo Tax: ${result_no_tax['total']:.2f}")


# ============================================================================
# TEST 6: FUNCTIONS WITH LISTS & DICTS
# ============================================================================
print("\n[TEST 6] Functions for Data Processing")
print("-" * 70)

def sum_by_status(transactions, target_status):
    """Sum amounts for transactions with specific status"""
    total = 0
    count = 0
    
    for trans in transactions:
        if trans.get("status") == target_status:
            total += trans["amount"]
            count += 1
    
    return {
        "status": target_status,
        "count": count,
        "total": total,
        "average": total / count if count > 0 else 0
    }

transactions = [
    {"id": 1, "amount": 100, "status": "completed"},
    {"id": 2, "amount": 250, "status": "pending"},
    {"id": 3, "amount": 150, "status": "completed"},
    {"id": 4, "amount": 75, "status": "failed"},
    {"id": 5, "amount": 200, "status": "completed"}
]

for status in ["completed", "pending", "failed"]:
    result = sum_by_status(transactions, status)
    print(f"{status.upper()}:")
    print(f"  Count: {result['count']}")
    print(f"  Total: ${result['total']:.2f}")
    print(f"  Average: ${result['average']:.2f}")


# ============================================================================
# TEST 7: FUNCTIONS WITH MULTIPLE RETURNS
# ============================================================================
print("\n[TEST 7] Multiple Return Values")
print("-" * 70)

def analyze_amounts(amounts):
    """Analyze a list of numbers"""
    if not amounts:
        return None, None, None, None
    
    return (
        min(amounts),
        max(amounts),
        sum(amounts),
        sum(amounts) / len(amounts)
    )

values = [100, 250, 50, 500, 200]
min_val, max_val, total, avg = analyze_amounts(values)

print(f"Data: {values}")
print(f"Statistics:")
print(f"  Min: ${min_val}")
print(f"  Max: ${max_val}")
print(f"  Total: ${total}")
print(f"  Average: ${avg:.2f}")


# ============================================================================
# TEST 8: VALIDATION FUNCTION
# ============================================================================
print("\n[TEST 8] Complete Validation Function")
print("-" * 70)

def validate_transaction(trans):
    """Comprehensive transaction validation"""
    
    # Check required fields
    required = ["id", "amount", "customer", "status"]
    for field in required:
        if field not in trans:
            return False, f"Missing: {field}"
    
    # Validate ID
    if trans["id"] <= 0:
        return False, "ID must be positive"
    
    # Validate amount
    if trans["amount"] <= 0:
        return False, "Amount must be positive"
    if trans["amount"] > 100000:
        return False, "Amount exceeds limit"
    
    # Validate customer
    if not trans["customer"] or len(trans["customer"]) < 2:
        return False, "Invalid customer name"
    
    # Validate status
    valid_statuses = ["pending", "completed", "failed", "cancelled"]
    if trans["status"] not in valid_statuses:
        return False, f"Invalid status: {trans['status']}"
    
    return True, "Valid"

# Test transactions
test_transactions = [
    {"id": 1, "amount": 250, "customer": "John Doe", "status": "completed"},
    {"id": 0, "amount": 250, "customer": "Jane Smith", "status": "completed"},  # Invalid ID
    {"id": 2, "amount": -100, "customer": "Bob Johnson", "status": "completed"},  # Negative amount
    {"id": 3, "amount": 250, "customer": "X", "status": "completed"},  # Invalid name
    {"id": 4, "amount": 250, "customer": "Alice Brown", "status": "unknown"},  # Invalid status
]

for trans in test_transactions:
    is_valid, message = validate_transaction(trans)
    status = "✓" if is_valid else "✗"
    print(f"{status} {trans['customer']:15} - {message}")


# ============================================================================
# TEST 9: DATA PIPELINE EXAMPLE
# ============================================================================
print("\n[TEST 9] Complete Data Processing Pipeline")
print("-" * 70)
print("Pipeline: Validate → Filter → Transform → Analyze\n")

raw_data = [
    {"id": 1, "amount": 250, "customer": "John", "status": "completed"},
    {"id": 2, "amount": -100, "customer": "Jane", "status": "completed"},  # Corrupt
    {"id": 3, "amount": 150, "customer": "Bob", "status": "pending"},
    {"id": 4, "amount": 500, "customer": "Alice", "status": "completed"},
    {"id": 5, "amount": 75, "customer": "Charlie", "status": "completed"},
]

# Step 1: Validate
print("Step 1: Validating transactions...")
valid_transactions = []
errors = []

for trans in raw_data:
    is_valid, message = validate_transaction(trans)
    if is_valid:
        valid_transactions.append(trans)
        print(f"  ✓ {trans['customer']}")
    else:
        errors.append({"trans": trans, "error": message})
        print(f"  ✗ {trans.get('customer', 'Unknown')} - {message}")

# Step 2: Filter (only completed)
print("\nStep 2: Filtering completed transactions...")
completed = [t for t in valid_transactions if t["status"] == "completed"]
print(f"  Found {len(completed)} completed transactions")

# Step 3: Analyze
print("\nStep 3: Analysis...")
amounts = [t["amount"] for t in completed]
total = sum(amounts)
average = total / len(amounts) if amounts else 0

print(f"  Total records processed: {len(raw_data)}")
print(f"  Valid records: {len(valid_transactions)}")
print(f"  Completed records: {len(completed)}")
print(f"  Total amount: ${total:.2f}")
print(f"  Average amount: ${average:.2f}")


# ============================================================================
# TEST 10: PRACTICAL EXAMPLES FROM REAL PIPELINES
# ============================================================================
print("\n[TEST 10] Real-World Pipeline Patterns")
print("-" * 70)

# Pattern 1: Aggregation
def aggregate_by_customer(transactions):
    """Group transactions by customer and sum amounts"""
    
    result = {}
    for trans in transactions:
        customer = trans["customer"]
        
        if customer not in result:
            result[customer] = {"count": 0, "total": 0}
        
        result[customer]["count"] += 1
        result[customer]["total"] += trans["amount"]
    
    return result

# Pattern 2: Transformation
def transform_for_report(transactions):
    """Transform data for reporting"""
    
    report = []
    for trans in transactions:
        report.append({
            "customer": trans["customer"],
            "amount": f"${trans['amount']:.2f}",
            "type": "Large" if trans["amount"] > 200 else "Normal"
        })
    
    return report

# Use the patterns
sample_trans = [
    {"id": 1, "customer": "John", "amount": 250},
    {"id": 2, "customer": "John", "amount": 100},
    {"id": 3, "customer": "Jane", "amount": 500},
]

print("Customer Summary:")
summary = aggregate_by_customer(sample_trans)
for customer, stats in summary.items():
    print(f"  {customer}: {stats['count']} transactions, ${stats['total']:.2f}")

print("\nReport Format:")
report = transform_for_report(sample_trans)
for item in report:
    print(f"  {item['customer']:10} {item['amount']:>10} ({item['type']})")


# ============================================================================
# EXERCISE SOLUTIONS
# ============================================================================
print("\n[SOLUTIONS] Exercise Answers")
print("-" * 70)

# Solution A: Email validation
print("\nExercise A - Email Validation:")

def is_valid_email(email):
    """Validate email format"""
    if not email or "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    if "." not in parts[1]:
        return False
    return True

test_emails = ["john@example.com", "invalid.email", "jane@domain.co.uk"]
for email in test_emails:
    result = is_valid_email(email)
    print(f"  {email:20} - {'✓' if result else '✗'}")

# Solution B: Order processing
print("\nExercise B - Order Processing:")

def process_orders(orders, min_amount=100):
    """Process orders and calculate stats"""
    
    filtered = [o for o in orders if o["amount"] > min_amount]
    total = sum(o["amount"] for o in filtered)
    
    return {
        "count": len(filtered),
        "total": total
    }

orders = [
    {"id": 1, "amount": 75},
    {"id": 2, "amount": 250},
    {"id": 3, "amount": 150}
]

result = process_orders(orders)
print(f"  Orders > $100: {result['count']}")
print(f"  Total: ${result['total']}")

# Solution C: Categorize transactions
print("\nExercise C - Categorize Transactions:")

def categorize_amounts(transactions):
    """Categorize by amount"""
    
    categories = {"small": 0, "medium": 0, "large": 0}
    
    for trans in transactions:
        amount = trans["amount"]
        if amount < 100:
            categories["small"] += 1
        elif amount < 500:
            categories["medium"] += 1
        else:
            categories["large"] += 1
    
    return categories

trans = [
    {"amount": 50},
    {"amount": 250},
    {"amount": 1000}
]

cats = categorize_amounts(trans)
print(f"  Small: {cats['small']}, Medium: {cats['medium']}, Large: {cats['large']}")

print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. IF/ELIF/ELSE: Decision making based on conditions
   - Use for validation and routing
   - Always validate data before using it

2. FOR LOOPS: Process sequences of data
   - Iterate through lists, dicts, ranges
   - Use enumerate() for index and value

3. LIST COMPREHENSIONS: Pythonic filtering and transformation
   - [x for x in list if condition]
   - Much cleaner than traditional for loops

4. FUNCTIONS: Reusable logic
   - Define once, use many times
   - Include validation in your functions
   - Return dicts/tuples for multiple values

5. VALIDATION: Critical for data pipelines
   - Check required fields
   - Validate ranges and formats
   - Return both success flag and message

PRACTICE: Implement the exercises and run this test file!
""")

print("=" * 70)
