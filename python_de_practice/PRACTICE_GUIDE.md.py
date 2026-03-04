"""
PRACTICE GUIDE: HOW TO WORK THROUGH THE EXERCISES
===================================================

This file shows you EXACTLY how to complete each exercise.
Follow along step-by-step and learn by doing!

READ THIS FIRST BEFORE STARTING EXERCISES!
"""

print("=" * 70)
print("HOW TO USE THE EXERCISES - COMPLETE WALKTHROUGH")
print("=" * 70)

# ============================================================================
# STEP 1: UNDERSTANDING THE STRUCTURE
# ============================================================================
print("\n[STEP 1] Understanding the Structure")
print("-" * 70)
print("""
Each exercise has 3 parts:

1. COMMENTS (instructions)
   # TODO Exercise A: Create variables for a customer purchase
   # - customer_name (string)
   # - product_name (string)
   
2. YOUR CODE (where you write)
   # Write your answer here

3. THE MAIN BLOCK (where you test)
   if __name__ == "__main__":
       # This runs when you press F5 or python exercises.py
       print(your_variables)
""")

# ============================================================================
# STEP 2: COMPLETE WALKTHROUGH OF EXERCISE A
# ============================================================================
print("\n[STEP 2] Complete Example: Exercise A")
print("-" * 70)

print("\nTHE TODO INSTRUCTIONS:")
print("""
# TODO Exercise A: Create variables for a customer purchase
# - customer_name (string)
# - product_name (string)
# - unit_price (float)
# - quantity (integer)
# - tax_rate (float - use 0.08 for 8%)
# - Calculate: total_before_tax, tax_amount, total_with_tax
""")

print("\nSTEP-BY-STEP SOLUTION:")

# STEP 1: Create the variables
print("\nStep 1: Create the variables")
customer_name = "John Doe"
product_name = "Laptop"
unit_price = 999.99
quantity = 1
tax_rate = 0.08
print(f"""
customer_name = "John Doe"
product_name = "Laptop"
unit_price = 999.99
quantity = 1
tax_rate = 0.08
""")

# STEP 2: Calculate total_before_tax
print("Step 2: Calculate total before tax")
total_before_tax = unit_price * quantity
print(f"""
total_before_tax = unit_price * quantity
                 = {unit_price} * {quantity}
                 = {total_before_tax}
""")

# STEP 3: Calculate tax_amount
print("Step 3: Calculate tax amount")
tax_amount = total_before_tax * tax_rate
print(f"""
tax_amount = total_before_tax * tax_rate
           = {total_before_tax} * {tax_rate}
           = {tax_amount}
""")

# STEP 4: Calculate total_with_tax
print("Step 4: Calculate total with tax")
total_with_tax = total_before_tax + tax_amount
print(f"""
total_with_tax = total_before_tax + tax_amount
               = {total_before_tax} + {tax_amount}
               = {total_with_tax}
""")

# STEP 5: Print results
print("Step 5: Print results to verify")
print(f"""
OUTPUT:
  Customer: {customer_name}
  Product: {product_name}
  Unit Price: ${unit_price}
  Quantity: {quantity}
  Subtotal: ${total_before_tax:.2f}
  Tax (8%): ${tax_amount:.2f}
  Total: ${total_with_tax:.2f}
""")

# ============================================================================
# STEP 3: COMPLETE WALKTHROUGH OF EXERCISE B
# ============================================================================
print("\n[STEP 3] Complete Example: Exercise B")
print("-" * 70)

print("\nTHE TODO INSTRUCTIONS:")
print("""
# TODO Exercise B: Parse and validate a transaction record
# Given: "1001,John Doe,250.50,2024-01-01"
# Split it and create variables for each field
# Convert types appropriately
# Create a formatted message: "Customer John Doe (ID: 1001) spent $250.50"
""")

print("\nSTEP-BY-STEP SOLUTION:")

# STEP 1: The raw data (as a string)
transaction_record = "1001,John Doe,250.50,2024-01-01"
print(f"\nStep 1: Start with raw data")
print(f"""
transaction_record = "1001,John Doe,250.50,2024-01-01"
""")

# STEP 2: Split the string
parts = transaction_record.split(",")
print(f"\nStep 2: Split by comma")
print(f"""
parts = transaction_record.split(",")
Result: {parts}
""")

# STEP 3: Create variables and convert types
trans_id = int(parts[0])  # Convert to integer
customer_name = parts[1]
amount = float(parts[2])  # Convert to float
date = parts[3]

print(f"\nStep 3: Create variables and convert types")
print(f"""
trans_id = int(parts[0])      # "1001" -> 1001 (integer)
customer_name = parts[1]       # "John Doe" -> John Doe (string)
amount = float(parts[2])       # "250.50" -> 250.50 (float)
date = parts[3]                # "2024-01-01" -> 2024-01-01 (string)

Variables created:
  trans_id = {trans_id} (type: {type(trans_id).__name__})
  customer_name = {customer_name} (type: {type(customer_name).__name__})
  amount = {amount} (type: {type(amount).__name__})
  date = {date} (type: {type(date).__name__})
""")

# STEP 4: Create the formatted message
formatted_message = f"Customer {customer_name} (ID: {trans_id}) spent ${amount}"

print(f"\nStep 4: Create formatted message")
print(f"""
formatted_message = f"Customer {{customer_name}} (ID: {{trans_id}}) spent ${{amount}}"

Result: {formatted_message}
""")

# ============================================================================
# STEP 4: COMPLETE WALKTHROUGH OF EXERCISE C
# ============================================================================
print("\n[STEP 4] Complete Example: Exercise C")
print("-" * 70)

print("\nTHE TODO INSTRUCTIONS:")
print("""
# TODO Exercise C: Create a data validation function
# Function should check if a number is between 0 and 1000
# Return True if valid, False otherwise
""")

print("\nSTEP-BY-STEP SOLUTION:")

print("\nStep 1: Create the function")
print("""
def is_valid_number(num):
    # Check if number is between 0 and 1000
    if num >= 0 and num <= 1000:
        return True
    else:
        return False
""")

def is_valid_number(num):
    """Check if number is between 0 and 1000"""
    if num >= 0 and num <= 1000:
        return True
    else:
        return False

# Alternative (shorter):
def is_valid_number_v2(num):
    """Check if number is between 0 and 1000 (shorter version)"""
    return 0 <= num <= 1000

print("\nStep 2: Test the function with examples")
test_numbers = [50, 0, 1000, 1001, -10]

for num in test_numbers:
    result = is_valid_number(num)
    print(f"""
Testing: {num}
Result: {result}
{"[VALID]" if result else "[INVALID]"}
""")

# ============================================================================
# STEP 5: COMPLETE WALKTHROUGH OF EXERCISE D
# ============================================================================
print("\n[STEP 5] Complete Example: Exercise D")
print("-" * 70)

print("\nTHE TODO INSTRUCTIONS:")
print("""
# TODO Exercise D: String manipulation
# Take the string: "  AWS DATA ENGINEERING  "
# Clean it (remove spaces), convert to lowercase
# Add a prefix: "Course: "
# Print the result
""")

print("\nSTEP-BY-STEP SOLUTION:")

# STEP 1: Start with original string
original = "  AWS DATA ENGINEERING  "
print(f"\nStep 1: Original string")
print(f"""
original = "  AWS DATA ENGINEERING  "
(Notice the spaces at the beginning and end)
""")

# STEP 2: Remove spaces (strip)
cleaned = original.strip()
print(f"\nStep 2: Remove spaces using .strip()")
print(f"""
cleaned = original.strip()
Result: "{cleaned}"
""")

# STEP 3: Convert to lowercase
lowercase = cleaned.lower()
print(f"\nStep 3: Convert to lowercase using .lower()")
print(f"""
lowercase = cleaned.lower()
Result: "{lowercase}"
""")

# STEP 4: Add prefix
final = f"Course: {lowercase}"
print(f"\nStep 4: Add prefix using f-string")
print(f"""
final = f"Course: {{lowercase}}"
Result: "{final}"
""")

# STEP 5: Print result
print(f"\nStep 5: Print the result")
print(f"""
print(final)
Output: {final}
""")

# ============================================================================
# HOW TO PRACTICE YOURSELF
# ============================================================================
print("\n" + "=" * 70)
print("HOW TO PRACTICE YOURSELF")
print("=" * 70)

print("""
NOW IT'S YOUR TURN! Here's how to practice:

STEP 1: Open exercises.py in VS Code
        Click on the exercises.py file in the explorer

STEP 2: Find the TODO section you want to work on
        Look for: # TODO Exercise A, B, C, or D

STEP 3: Read the instructions carefully
        Understand what you need to create

STEP 4: Write your code
        Replace the # TODO with your actual code
        Remember: Python is case-sensitive!

STEP 5: Run your code
        Press F5 or type: python exercises.py
        See if it works!

STEP 6: Check your results
        Did you get the expected output?
        If not, look at this guide for help

STEP 7: Compare with solutions
        Open test.py to see the solutions
        See if your approach was similar
""")

# ============================================================================
# PRACTICE EXERCISE FOR YOU
# ============================================================================
print("\n" + "=" * 70)
print("YOUR PRACTICE EXERCISE")
print("=" * 70)

print("""
Try this practice exercise to get comfortable:

CREATE AN EXERCISE:
-------------------
Write code to:
1. Create variables for a pizza order:
   - pizza_name (e.g., "Pepperoni")
   - quantity (e.g., 2)
   - price_per_pizza (e.g., 15.99)
   - discount_percentage (e.g., 10)

2. Calculate:
   - subtotal (price_per_pizza * quantity)
   - discount_amount (subtotal * discount_percentage / 100)
   - final_price (subtotal - discount_amount)

3. Print results:
   "Order: 2 Pepperoni pizzas"
   "Subtotal: $31.98"
   "Discount (10%): $3.20"
   "Final Price: $28.78"

THIS IS WHERE YOU PRACTICE:
----------------------------
Write this code in a NEW FILE called practice_pizza.py:

pizza_name = "Pepperoni"
quantity = 2
price_per_pizza = 15.99
discount_percentage = 10

# Write the calculations
subtotal = ???
discount_amount = ???
final_price = ???

# Write the print statements
print(f"Order: {quantity} {pizza_name} pizzas")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount ({discount_percentage}%): ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")

THEN RUN IT:
python practice_pizza.py

EXPECTED OUTPUT:
Order: 2 Pepperoni pizzas
Subtotal: $31.98
Discount (10%): $3.20
Final Price: $28.78
""")

# ============================================================================
# UNDERSTANDING THE WORKFLOW
# ============================================================================
print("\n" + "=" * 70)
print("YOUR WORKFLOW")
print("=" * 70)

print("""
Here's exactly what to do:

EVERY DAY:
1. Open exercises.py
2. Read each section with comments
3. Find TODO exercises
4. Write your solution code
5. Run the file: python exercises.py
6. See if it works
7. If stuck, look at test.py for solutions
8. Understand the solution
9. Try again yourself

PRACTICE:
- Create new files like practice_pizza.py
- Try variations (different numbers, scenarios)
- Combine concepts from multiple sections

TESTING:
- Run test.py to see complete examples
- Compare your code with the solutions
- Understanding WHY it works is key

MOVING ON:
- When you understand a day completely
- Move to the next day
- Build on what you learned
""")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("QUICK SUMMARY")
print("=" * 70)

print("""
EXERCISES.PY HAS:
1. Annotated examples (read and understand)
2. TODO sections (YOUR PRACTICE)
3. Main block (where you test)

YOUR JOB:
1. Replace TODO with your code
2. Run it
3. Check if it works
4. Understand why it works

WHERE TO PRACTICE:
- exercises.py (the TODO sections)
- test.py (see how solutions look)
- Create your own practice files

YOU NOW KNOW:
[OK] How the curriculum is structured
[OK] How to work through exercises
[OK] Where to practice (exercises.py TODOs)
[OK] How to test your code
[OK] How to compare with solutions

NEXT: Go back to exercises.py and complete all 4 TODO exercises!
""")

print("\n" + "=" * 70)
