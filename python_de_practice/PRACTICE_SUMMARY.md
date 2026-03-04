# COMPLETE SUMMARY: HOW TO PRACTICE

## TL;DR (Too Long; Didn't Read) - Quick Answer

**You asked:** "I don't see any place for practice"

**Answer:** There are 4 places to practice:

1. **exercises.py** - Replace TODO with your code (MAIN PRACTICE)
2. **Create practice_*.py files** - Your own practice variations
3. **Modify examples** - Change values and test
4. **test.py** - Learn from solutions when stuck

---

## What You Have Right Now

```
day01/
├── exercises.py       <- YOUR MAIN PRACTICE (has TODO sections)
├── test.py           <- SEE SOLUTIONS HERE
└── (create these):
    ├── practice_pizza.py
    ├── practice_email.py
    └── practice_transaction.py
```

---

## Your Day 01 - What You Already Completed ✓

```python
# Exercise A: Customer Purchase Calculation
customer_name = "karan johoar"
product_name = "laptop"
unit_price = 99.99
quantity = 2
tax_rate = 0.08
total_before_tax = unit_price * quantity     # 199.98
tax_amount = total_before_tax * tax_rate     # 16.00
total_with_tax = total_before_tax + tax_amount  # 215.98
```

Run: `python exercises.py`
Output: Shows all exercises results ✓

---

## Your 4 Practice Locations (Detailed)

### LOCATION 1: exercises.py - TODO Sections (Main)

**Path:** `day01/exercises.py`
**What:** Lines with `# TODO Exercise A, B, C, D`
**Your Job:** Replace TODO with actual code
**Time:** 20-30 minutes per exercise
**Test:** `python exercises.py`

**Example:**
```python
# TODO Exercise A: Create variables for a customer purchase
# Your code here...

customer_name = "karan johoar"
product_name = "laptop"
unit_price = 99.99
quantity = 2
tax_rate = 0.08

total_before_tax = unit_price * quantity
tax_amount = total_before_tax * tax_rate
total_with_tax = total_before_tax + tax_amount
```

### LOCATION 2: Create Your Own practice_*.py Files

**Path:** `day01/practice_anything.py` (you create)
**What:** New files with similar code, different data
**Your Job:** Write variations of exercises
**Time:** 15-20 minutes each
**Test:** `python practice_anything.py`

**Examples to Create:**

**practice_pizza.py:**
```python
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

**practice_email.py:**
```python
emails = ["  JOHN@EXAMPLE.COM  ", "  JANE@DOMAIN.CO.UK  "]

for email in emails:
    cleaned = email.strip().lower()
    print(f"Original: '{email}'")
    print(f"Cleaned:  '{cleaned}'")
    print()
```

**practice_transaction.py:**
```python
transactions = [
    "1001,250.50,completed",
    "1002,150.00,pending",
    "1003,75.25,failed"
]

for trans in transactions:
    parts = trans.split(",")
    trans_id = int(parts[0])
    amount = float(parts[1])
    status = parts[2]
    
    print(f"ID: {trans_id} | Amount: ${amount:.2f} | Status: {status}")
```

### LOCATION 3: Modify Examples (Experiment)

**Path:** `day01/exercises.py` (top section)
**What:** Change example values
**Your Job:** Edit numbers and re-run
**Time:** 5-10 minutes
**Test:** `python exercises.py`

**Original:**
```python
full_name = "John Doe"
message = f"Customer {customer_id} ordered ${order_amount}"
```

**Your Modification:**
```python
full_name = "Your Name"
message = f"Customer 2024 ordered $999.99"
```

Run and see different output!

### LOCATION 4: test.py - Learning from Solutions

**Path:** `day01/test.py`
**What:** Complete working examples
**Your Job:** Read, understand, compare with your code
**Time:** 10-15 minutes
**Test:** `python test.py`

Use when:
- You get stuck
- You want to compare your code
- You want to see best practices

---

## Your Complete Daily Workflow

### TIME: 60-75 minutes per day

```
MINUTE 0-15: READ THE EXAMPLES
├── Open: exercises.py
├── Read: Sections 1-8 (annotated examples)
└── Goal: Understand the concepts

MINUTE 15-30: SEE SOLUTIONS
├── Open: test.py
├── Run: python test.py
└── Goal: See how things work

MINUTE 30-50: COMPLETE EXERCISES
├── Back to: exercises.py
├── Find: # TODO Exercise A, B, C, D
├── Write: Your solution code
├── Run: python exercises.py
└── Goal: All exercises working

MINUTE 50-70: CREATE PRACTICE FILE
├── Create: practice_yourname.py
├── Write: Similar code, different data
├── Run: python practice_yourname.py
└── Goal: Practice variations

MINUTE 70-75: COMPARE & VERIFY
├── Open: test.py
├── Compare: Your code vs solution
└── Goal: Understand your approach
```

---

## Progress Checklist

Use this EVERY DAY:

### Day 01 (You're Here!)
- [ ] Read exercises.py examples (all sections)
- [ ] Run test.py successfully
- [ ] Complete Exercise A (Customer Purchase)
- [ ] Complete Exercise B (Parse Transaction)
- [ ] Complete Exercise C (Validation Function)
- [ ] Complete Exercise D (String Manipulation)
- [ ] Run exercises.py - all output correct
- [ ] Create practice_pizza.py
- [ ] Create practice_email.py
- [ ] Create practice_transaction.py

### Day 02 (Next)
- [ ] Same workflow
- [ ] Learn: Lists, Dicts, Tuples
- [ ] Practice: List operations, filtering

### Day 03 (After that)
- [ ] Same workflow
- [ ] Learn: Control flow, functions
- [ ] Practice: Conditionals, loops, functions

### Day 04
- [ ] Same workflow
- [ ] Learn: File I/O, ETL pipelines
- [ ] Practice: Reading/writing files

---

## Real Example: Exercise A Complete Walkthrough

### THE TASK
```
# TODO Exercise A: Create variables for a customer purchase
# - customer_name (string)
# - product_name (string)
# - unit_price (float)
# - quantity (integer)
# - tax_rate (float - use 0.08 for 8%)
# - Calculate: total_before_tax, tax_amount, total_with_tax
```

### YOUR CODE
```python
customer_name = "karan johoar"      # String
product_name = "laptop"             # String
unit_price = 99.99                  # Float
quantity = 2                        # Integer
tax_rate = 0.08                     # Float (8% = 0.08)

# Calculate subtotal
total_before_tax = unit_price * quantity
# = 99.99 * 2
# = 199.98

# Calculate tax
tax_amount = total_before_tax * tax_rate
# = 199.98 * 0.08
# = 15.9984 (rounded to $16.00)

# Calculate final total
total_with_tax = total_before_tax + tax_amount
# = 199.98 + 16.00
# = 215.98
```

### TEST IT
```bash
python exercises.py
```

### EXPECTED OUTPUT
```
[Exercise A] Customer Purchase Calculation:
  Customer: karan johoar
  Product: laptop
  Unit Price: $99.99
  Quantity: 2
  Subtotal: $199.98
  Tax (8%): $16.00
  Total: $215.98
```

### VERIFY WITH test.py
```bash
python test.py
```
Find [Exercise A] section and compare.

### CREATE VARIATION (practice_invoice.py)
```python
item1_name = "Shirt"
item1_price = 25.00
item1_qty = 3

item2_name = "Pants"
item2_price = 50.00
item2_qty = 1

tax_rate = 0.08

subtotal = (item1_price * item1_qty) + (item2_price * item2_qty)
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Invoice for {item1_qty} {item1_name} and {item2_qty} {item2_name}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
```

Run: `python practice_invoice.py`

---

## Common Questions

**Q: Where exactly do I write my code?**
A: In exercises.py, replace `# TODO` with your actual code

**Q: What if I don't understand?**
A: 
1. Read the comments above the TODO
2. Look at test.py for solutions
3. Try smaller pieces first
4. Create practice files

**Q: Can I modify the examples?**
A: Yes! Change values and test - great for learning!

**Q: How long should each day take?**
A: 60-75 minutes:
   - 15 min: read examples
   - 15 min: see solutions
   - 20 min: complete exercises
   - 15 min: create practice file

**Q: What if I get an error?**
A: Check:
   1. Is the filename correct?
   2. Is syntax correct (quotes, brackets)?
   3. Are variables named right?
   4. Run test.py to see correct code

**Q: Can I skip days?**
A: Not recommended. Each day builds on previous days.

**Q: When do I learn AWS stuff?**
A: Days 1-4: Python basics (you're here)
   Days 5-6: Data formats (JSON, CSV)
   Days 7-10: AWS libraries (boto3, S3, DynamoDB)

---

## Files You Need to Know About

| File | Purpose | Open When |
|------|---------|-----------|
| exercises.py | Main practice | Every day, fill in TODOs |
| test.py | See solutions | When stuck, comparing |
| QUICK_REFERENCE.md | Visual guide | Need to understand structure |
| PRACTICE_GUIDE.md.py | Step-by-step | Want detailed walkthrough |
| WHERE_TO_PRACTICE.py | This file | Understanding where to practice |
| practice_*.py | Your own files | Create to practice variations |

---

## Next Steps Right Now

1. **You already completed Exercise A!** ✓
   - customer_name, product_name, calculations all working

2. **Next: Finish Exercises B, C, D**
   - Open exercises.py
   - Complete Exercise B (parse transaction)
   - Complete Exercise C (validation function)
   - Complete Exercise D (string manipulation)
   - Run: `python exercises.py`

3. **Then: Create Practice Files**
   - Create practice_pizza.py
   - Create practice_email.py
   - Create practice_transaction.py
   - Run each one

4. **Finally: Move to Day 02**
   - Open day02/exercises.py
   - Repeat the same workflow

---

## You Have Everything You Need!

✓ Clear instructions in exercises.py
✓ Working examples in test.py
✓ Multiple practice locations
✓ Detailed guides (QUICK_REFERENCE.md, PRACTICE_GUIDE.md.py)
✓ This summary (WHERE_TO_PRACTICE.py)

**Now go practice! 🚀**

Remember: The only way to learn programming is by WRITING CODE!
