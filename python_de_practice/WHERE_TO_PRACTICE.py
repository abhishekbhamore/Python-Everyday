"""
========================================================================
PRACTICE GUIDE: WHERE AND HOW TO PRACTICE
========================================================================

This file shows you EXACTLY where to practice and how to do it.
"""

print("=" * 80)
print("WHERE TO PRACTICE - COMPLETE GUIDE")
print("=" * 80)

print("""
You asked: "I don't see any place for practice"

ANSWER: Here are 4 PLACES to practice:
=========================================

PLACE 1: exercises.py (Main Practice - Days 1, 2, 3, 4...)
          Location: day01/exercises.py
          What: TODO sections
          How: Replace TODO with your code

PLACE 2: Create Your Own Files (Practice Variations)
          Location: day01/practice_pizza.py, practice_email.py, etc.
          What: New files you create
          How: Write similar code with different scenarios

PLACE 3: Modify Examples (Experiment)
          Location: exercises.py example sections
          What: Change values and see what happens
          How: Edit numbers and run again

PLACE 4: test.py (Learning from Solutions)
          Location: day01/test.py
          What: Complete working examples
          How: Read, understand, then apply

""")

# ============================================================================
# PRACTICAL EXAMPLE: SHOWING ALL 4 PRACTICE LOCATIONS
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE: THE COMPLETE PRACTICE WORKFLOW")
print("=" * 80)

print("""
SCENARIO: Learning Day 01 Exercise A

STEP 1: STUDY THE EXAMPLE (exercises.py)
--------
Read: Annotated examples at top of exercises.py
What: Learn how variables, calculations work
Time: 15 minutes

STEP 2: SEE IT IN ACTION (test.py)
--------
Open: day01/test.py
Run: python test.py
See: Complete working solutions
Time: 10 minutes

STEP 3: PRACTICE IN exercises.py (TODO)
--------
Location: Look for # TODO Exercise A
Task: Complete the exercise
Your code:

    customer_name = "karan johoar"
    product_name = "laptop"
    unit_price = 99.99
    quantity = 2
    tax_rate = 0.08
    
    total_before_tax = unit_price * quantity
    tax_amount = total_before_tax * tax_rate
    total_with_tax = total_before_tax + tax_amount

Run: python exercises.py
See: Does it work?
Time: 20 minutes

STEP 4: CREATE YOUR OWN PRACTICE (practice_*.py)
--------
Create: practice_invoice.py
Purpose: Variations of the same concept
Your code:

    item1_price = 50.00
    item2_price = 30.00
    item1_qty = 3
    item2_qty = 2
    tax_rate = 0.08
    
    subtotal = (item1_price * item1_qty) + (item2_price * item2_qty)
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    print(f"Invoice: ${subtotal:.2f} + ${tax:.2f} = ${total:.2f}")

Run: python practice_invoice.py
See: Similar pattern, different data
Time: 15 minutes

STEP 5: COMPARE & UNDERSTAND
--------
Look at: test.py Exercise A solution
Compare: Your code vs. solution
Learn: Why your approach worked
Time: 10 minutes

TOTAL TIME: ~70 minutes = 1 complete learning session
""")

# ============================================================================
# SHOWING WHAT EXISTS RIGHT NOW
# ============================================================================

print("\n" + "=" * 80)
print("WHAT YOU HAVE RIGHT NOW (Files in Your Folder)")
print("=" * 80)

import os

structure = """
C:\CRMA\Python\python_de_practice\
|
+-- README.md                  <- START HERE (overview)
+-- CURRICULUM.md              <- See all 10 days
+-- QUICK_REFERENCE.md         <- Visual guide (you're using this!)
+-- PRACTICE_GUIDE.md.py       <- Step-by-step walkthrough
|
+-- day01/
|   +-- exercises.py           <- YOUR MAIN PRACTICE FILE
|   +-- test.py                <- SEE SOLUTIONS HERE
|   |
|   +-- practice_pizza.py       <- (YOU CREATE THESE)
|   +-- practice_email.py       <- (YOU CREATE THESE)
|   +-- practice_transaction.py <- (YOU CREATE THESE)
|
+-- day02/
|   +-- exercises.py           <- NEXT LEVEL PRACTICE
|   +-- test.py                <- SEE SOLUTIONS
|
+-- day03/
|   +-- exercises.py
|   +-- test.py
|
+-- day04/
|   +-- exercises.py
|   +-- test.py
"""

print(structure)

print("\nEXERCISES.PY STRUCTURE:")
print("-" * 80)

example = """
exercises.py has:

SECTION 1: Examples (Read & Learn)
    - Annotated code
    - Shows how things work
    - Already has values set

SECTION 2: Examples (Read & Learn)
    - More annotated code
    - Different concepts

...more sections...

SECTION PRACTICAL EXERCISES: (YOU WRITE HERE!)
    # TODO Exercise A: ...
    # Instructions...
    customer_name = ???
    product_name = ???
    ...write your code...

    # TODO Exercise B: ...
    ...write your code...

    # TODO Exercise C: ...
    ...write your code...

    # TODO Exercise D: ...
    ...write your code...

MAIN BLOCK: (Tests your code)
    if __name__ == "__main__":
        print(your_variables)
        Run: python exercises.py
"""

print(example)

# ============================================================================
# YOUR 3-STEP DAILY PRACTICE ROUTINE
# ============================================================================

print("\n" + "=" * 80)
print("YOUR 3-STEP DAILY PRACTICE ROUTINE (60 minutes)")
print("=" * 80)

routine = """
EVERY DAY:

STEP 1: LEARN (15 minutes)
   1. Open exercises.py
   2. Read Section 1, 2, 3, ... (annotated examples)
   3. Understand the concepts
   4. Don't write code yet - just read

STEP 2: SEE SOLUTIONS (15 minutes)
   1. Open test.py
   2. Run: python test.py
   3. See complete working examples
   4. Compare with exercises.py

STEP 3: PRACTICE (30 minutes)
   1. Back to exercises.py
   2. Find # TODO Exercise A, B, C, D
   3. Write your code to complete each TODO
   4. Run: python exercises.py
   5. Check: Does it work?
   6. If stuck: Look at test.py for help
   7. Try again

BONUS: CREATE VARIATIONS (Optional, 20+ minutes)
   1. Create practice_yourname.py
   2. Write similar code with different data
   3. Test it
   4. Experiment with variations
"""

print(routine)

# ============================================================================
# SPECIFIC EXAMPLE: Exercise A IN DETAIL
# ============================================================================

print("\n" + "=" * 80)
print("DETAILED EXAMPLE: EXERCISE A START TO FINISH")
print("=" * 80)

print("""
LOCATION: day01/exercises.py (around line 190)

THE INSTRUCTIONS YOU SEE:
---
# TODO Exercise A: Create variables for a customer purchase
# - customer_name (string)
# - product_name (string)
# - unit_price (float)
# - quantity (integer)
# - tax_rate (float - use 0.08 for 8%)
# - Calculate: total_before_tax, tax_amount, total_with_tax
---

YOUR TASK: FILL IN THE CODE

STEP 1: Understand what's needed
   - 5 variables to create (as listed)
   - 3 calculations to do

STEP 2: Write the code
---
customer_name = "karan johoar"          # String
product_name = "laptop"                 # String
unit_price = 99.99                      # Float
quantity = 2                            # Integer
tax_rate = 0.08                         # Float (8%)

total_before_tax = unit_price * quantity
tax_amount = total_before_tax * tax_rate
total_with_tax = total_before_tax + tax_amount
---

STEP 3: Test it
   Run: python exercises.py
   
   Expected Output:
   [Exercise A] Customer Purchase Calculation:
     Customer: karan johoar
     Product: laptop
     Unit Price: $99.99
     Quantity: 2
     Subtotal: $199.98
     Tax (8%): $16.00
     Total: $215.98

STEP 4: Understand it
   - unit_price * quantity = subtotal
   - subtotal * tax_rate = tax amount
   - subtotal + tax = final total

STEP 5: Verify with test.py
   Open: test.py
   Find: Exercise A solution
   Compare: Is your code similar?

STEP 6: Create variations
   Create: practice_invoice.py
   Write: Similar code with different products
   Test: Does it still work?
""")

# ============================================================================
# THE 4 PRACTICE LOCATIONS IN DETAIL
# ============================================================================

print("\n" + "=" * 80)
print("4 PLACES TO PRACTICE - DETAILED EXPLANATION")
print("=" * 80)

print("""
PLACE 1: exercises.py - THE TODO SECTIONS
==========================================
Location: day01/exercises.py (around line 190)
What: # TODO Exercise A, B, C, D
How: Replace TODO with your code
Why: This is the main learning
When: Every day you work
Output: python exercises.py
Skills: Following instructions, writing code, testing

Example:
# TODO Exercise A: Create variables...
customer_name = "???"          <- YOUR CODE HERE
product_name = "???"           <- YOUR CODE HERE
unit_price = ???               <- YOUR CODE HERE
quantity = ???                 <- YOUR CODE HERE
tax_rate = 0.08                <- FILL IN THE NUMBER
total_before_tax = ???         <- YOUR CODE HERE
tax_amount = ???               <- YOUR CODE HERE
total_with_tax = ???           <- YOUR CODE HERE


PLACE 2: CREATE YOUR OWN practice_*.py FILES
=============================================
Location: day01/practice_anything.py (you create)
What: New files with variations
How: Write similar code with different data
Why: Practice variations, build confidence
When: After completing exercises.py
Output: python practice_anything.py
Skills: Creating files, applying concepts, experimenting

Examples you can create:
- practice_pizza.py       (Calculate pizza orders)
- practice_email.py       (Clean email addresses)
- practice_transaction.py (Parse transaction data)
- practice_student.py     (Calculate grades)
- practice_shopping.py    (Shopping cart calculations)

Example:
# Create: practice_shopping.py
shirt_price = 25.00
pants_price = 50.00
shirt_qty = 3
pants_qty = 2
tax_rate = 0.08

subtotal = (shirt_price * shirt_qty) + (pants_price * pants_qty)
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Total: ${total:.2f}")


PLACE 3: MODIFY EXAMPLES IN exercises.py
=========================================
Location: exercises.py (top section with examples)
What: Change the example values
How: Edit and re-run
Why: See how values affect output
When: After reading examples
Output: python exercises.py
Skills: Understanding cause and effect

Original:
full_name = "John Doe"

Your change:
full_name = "Your Name Here"

Re-run and see different output!


PLACE 4: test.py - LEARNING FROM SOLUTIONS
===========================================
Location: day01/test.py
What: Complete working examples
How: Read and understand
Why: See how solutions are written
When: When you're stuck or comparing
Output: python test.py
Skills: Reading code, understanding patterns

Use for:
- Understanding correct syntax
- Seeing how to structure code
- Comparing your approach
- Learning best practices
""")

# ============================================================================
# QUICK CHECKLIST: "AM I PRACTICING ENOUGH?"
# ============================================================================

print("\n" + "=" * 80)
print("QUICK CHECKLIST: Am I Practicing Enough?")
print("=" * 80)

print("""
CHECK THESE BOXES EACH DAY:

Exercise Practice:
  [ ] Read exercises.py examples (15 min)
  [ ] Ran test.py to see solutions (10 min)
  [ ] Completed Exercise A TODO (15 min)
  [ ] Completed Exercise B TODO (15 min)
  [ ] Completed Exercise C TODO (10 min)
  [ ] Completed Exercise D TODO (10 min)
  [ ] Ran python exercises.py successfully
  [ ] All TODOs replaced with actual code

Extra Practice:
  [ ] Created 1 practice_*.py file
  [ ] Modified example values
  [ ] Tested variations
  [ ] Understood WHY the code works

If you checked 10+: GOOD! You're learning
If you checked 8-10: OK, but try more practice files
If you checked <8: Not practicing enough, do more TODAY


PRACTICE INTENSITY LEVELS:

BEGINNER (Start here):
  - Complete exercises.py TODOs
  - Run python exercises.py
  - Compare with test.py
  - Time: 45 minutes/day

INTERMEDIATE (After 2-3 days):
  - All above +
  - Create 1-2 practice files per day
  - Try variations
  - Time: 60-75 minutes/day

ADVANCED (After 1 week):
  - All above +
  - Create 3-5 practice files
  - Combine concepts
  - Challenge yourself with new scenarios
  - Time: 90+ minutes/day
""")

# ============================================================================
# YOUR NEXT STEP RIGHT NOW
# ============================================================================

print("\n" + "=" * 80)
print("YOUR NEXT STEP RIGHT NOW")
print("=" * 80)

print("""
DO THIS NOW:

1. Open: day01/exercises.py
   (You already started Exercise A - good!)

2. Complete:
   [ ] Exercise A (you're close!)
   [ ] Exercise B (parse transaction)
   [ ] Exercise C (validation function)
   [ ] Exercise D (string manipulation)

3. Test:
   Run: python exercises.py
   Check: Does it print correct output?

4. Compare:
   Open: day01/test.py
   Find: [Exercise A] section
   Compare: Is your code similar?

5. Create Practice:
   Create: day01/practice_pizza.py
   Write: Pizza order calculation
   Run: python practice_pizza.py
   Test: Does it work?

AFTER ALL THAT (maybe 60-90 min):
   You're done with Day 01!
   Ready for Day 02!
""")

print("\n" + "=" * 80)
print("You now have EVERYTHING you need to practice!")
print("=" * 80)
