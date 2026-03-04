# QUICK REFERENCE: YOUR DAILY WORKFLOW

## What You Already Know (Good!)
- You understand the concepts
- You know what variables, functions, etc. are

## What You Need to Learn (This Course!)
- HOW to write the code
- Syntax and structure
- How to practice and improve

---

## YOUR DAILY PRACTICE PATTERN

### 1. STUDY PHASE (15-20 minutes)
```
Open: exercises.py
Read: All the annotated examples at the top
Goal: Understand the concepts
```

### 2. EXECUTE PHASE (10 minutes)
```
Open: test.py
Run: python test.py
Goal: See working examples
```

### 3. PRACTICE PHASE (20-30 minutes)
```
Back to: exercises.py
Find: # TODO Exercise A, B, C, D
Write: Your solution code
Run: python exercises.py
Check: Does it work?
```

### 4. VERIFY PHASE (10 minutes)
```
Open: test.py
Compare: Your code vs. the solution
Goal: Understand if your approach was good
```

---

## WHERE YOU PRACTICE

### LOCATION 1: exercises.py (Main Practice)
```python
# TODO Exercise A: Create variables for a customer purchase
# - customer_name (string)
# - product_name (string)
# - unit_price (float)
# - quantity (integer)
# - tax_rate (float - use 0.08 for 8%)
# - Calculate: total_before_tax, tax_amount, total_with_tax

# <-- WRITE YOUR ANSWER HERE

customer_name = "???"
product_name = "???"
unit_price = ???
quantity = ???
tax_rate = 0.08
total_before_tax = ???
tax_amount = ???
total_with_tax = ???
```

### LOCATION 2: Create Your Own Files
```
Create: practice_pizza.py
Purpose: Practice variations
Example: Calculate pizza order with discounts
```

### LOCATION 3: Modify Examples
```
Edit: exercises.py
Change: The example values
Test: Does your understanding hold?
```

---

## THE COMPLETE CYCLE

```
1. Read exercises.py
        ↓
2. Run test.py to see solutions
        ↓
3. Write code in exercises.py TODO sections
        ↓
4. Run python exercises.py to test
        ↓
5. Compare your code with test.py solutions
        ↓
6. Understand why your approach worked (or didn't)
        ↓
7. Create your own practice files
        ↓
8. Move to next day
```

---

## EXERCISE A EXAMPLE - FILL IN THE BLANKS

### The Instructions:
```
# TODO Exercise A: Create variables for a customer purchase
# - customer_name (string)
# - product_name (string)
# - unit_price (float)
# - quantity (integer)
# - tax_rate (float - use 0.08 for 8%)
# - Calculate: total_before_tax, tax_amount, total_with_tax
```

### Your Code (FILL IN THE ???):
```python
customer_name = "John Doe"              # <- PUT A NAME HERE
product_name = "Laptop"                 # <- PUT A PRODUCT HERE
unit_price = 999.99                     # <- PUT A PRICE HERE
quantity = 1                            # <- PUT A QUANTITY HERE
tax_rate = 0.08                         # <- GIVEN (8%)

# NOW CALCULATE:
total_before_tax = unit_price * quantity  # <- MULTIPLY PRICE BY QUANTITY
tax_amount = total_before_tax * tax_rate  # <- MULTIPLY BY TAX RATE
total_with_tax = total_before_tax + tax_amount  # <- ADD TAX TO TOTAL
```

### Then Test It:
```bash
python exercises.py
```

### Expected Output:
```
Day 01: Python Fundamentals & Data Types
==================================================

Example 1: Full name = ...
Example 2: ...
Example 3: ...
Example 4: Total cost with tax = $...
Example 5: ...
```

---

## EXERCISE B EXAMPLE - PARSE DATA

### The Instructions:
```
# TODO Exercise B: Parse and validate a transaction record
# Given: "1001,John Doe,250.50,2024-01-01"
# Split it and create variables for each field
# Convert types appropriately
# Create a formatted message: "Customer John Doe (ID: 1001) spent $250.50"
```

### Your Code:
```python
# Start with the raw string
transaction_record = "1001,John Doe,250.50,2024-01-01"

# Split by comma
parts = transaction_record.split(",")

# Create variables and convert types
trans_id = int(parts[0])        # Convert to integer
customer_name = parts[1]        # Keep as string
amount = float(parts[2])        # Convert to float
date = parts[3]                 # Keep as string

# Create formatted message
formatted = f"Customer {customer_name} (ID: {trans_id}) spent ${amount}"
print(formatted)
```

### Output:
```
Customer John Doe (ID: 1001) spent $250.5
```

---

## EXERCISE C EXAMPLE - WRITE A FUNCTION

### The Instructions:
```
# TODO Exercise C: Create a data validation function
# Function should check if a number is between 0 and 1000
# Return True if valid, False otherwise
```

### Your Code:
```python
def is_valid_number(num):
    """Check if number is between 0 and 1000"""
    if num >= 0 and num <= 1000:
        return True
    else:
        return False

# Test it:
print(is_valid_number(50))      # Should print: True
print(is_valid_number(1001))    # Should print: False
print(is_valid_number(500))     # Should print: True
```

---

## EXERCISE D EXAMPLE - STRING MANIPULATION

### The Instructions:
```
# TODO Exercise D: String manipulation
# Take the string: "  AWS DATA ENGINEERING  "
# Clean it (remove spaces), convert to lowercase
# Add a prefix: "Course: "
# Print the result
```

### Your Code:
```python
original = "  AWS DATA ENGINEERING  "
cleaned = original.strip()      # Remove spaces
lowercase = cleaned.lower()     # Convert to lowercase
final = f"Course: {lowercase}"  # Add prefix
print(final)
```

### Output:
```
Course: aws data engineering
```

---

## HOW TO TEST YOUR CODE

### Method 1: Run the File
```bash
cd day01
python exercises.py
```

### Method 2: Run in VS Code
```
Click on exercises.py
Press F5 (or Ctrl+F5)
See output in terminal at bottom
```

### Method 3: Create a New Test File
```bash
# Create: my_test.py
# Write your code there
# Run: python my_test.py
```

---

## IF YOU GET STUCK

### Step 1: Check the Instructions
```
What does the TODO say?
Did you miss something?
```

### Step 2: Look at test.py
```
Open: day01/test.py
Find: The same exercise solution
Compare with your code
```

### Step 3: Try Smaller Pieces
```
Instead of writing all at once
Test one line at a time
Use print() to check values
```

### Step 4: Check Your Syntax
```
Python is case-sensitive!
Indentation matters!
Quotes must match ("..." or '...')
```

---

## PRACTICE FILES YOU CAN CREATE

### practice_pizza.py
```python
# Calculate pizza order with discount
pizza_name = "Pepperoni"
quantity = 2
price_per_pizza = 15.99
discount_percentage = 10

subtotal = price_per_pizza * quantity
discount_amount = subtotal * discount_percentage / 100
final_price = subtotal - discount_amount

print(f"Order: {quantity} {pizza_name} pizzas")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount ({discount_percentage}%): ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")
```

### practice_email.py
```python
# Clean and validate emails
email1 = "  JOHN@EXAMPLE.COM  "
email2 = "  JANE@DOMAIN.CO.UK  "

for email in [email1, email2]:
    cleaned = email.strip().lower()
    print(f"Original: '{email}'")
    print(f"Cleaned:  '{cleaned}'")
    print()
```

### practice_transaction.py
```python
# Parse multiple transactions
transactions = [
    "1001,250.50,completed",
    "1002,150.00,pending",
    "1003,75.25,completed"
]

for trans in transactions:
    parts = trans.split(",")
    trans_id = int(parts[0])
    amount = float(parts[1])
    status = parts[2]
    
    print(f"Transaction {trans_id}: ${amount:.2f} ({status})")
```

---

## PROGRESSION

### Week 1 (Days 1-2)
- Learn fundamentals (types, variables)
- Work with data structures (lists, dicts)
- Complete all exercises
- Create 2-3 practice files

### Week 2 (Days 3-4)
- Learn control flow (if/else, loops)
- Learn functions
- Learn file operations
- Complete all exercises
- Create 2-3 practice files

### Week 3+ (Days 5-10)
- Learn JSON/CSV
- Learn error handling
- Learn AWS basics (boto3)
- Build complete pipelines

---

## YOUR GOAL

After Day 1, you should be able to:
1. Create variables of different types
2. Do basic calculations
3. Work with strings
4. Convert between types
5. Run your code and see results
6. Understand WHY your code works

---

## REMEMBER

**The only way to learn programming is by DOING it!**

- Don't just read
- Write the code yourself
- Test it
- Break it
- Fix it
- Learn from it

Good luck! You've got this! 🚀
