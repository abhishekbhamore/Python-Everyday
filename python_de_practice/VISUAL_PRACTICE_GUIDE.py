"""
VISUAL GUIDE: WHERE AND HOW TO PRACTICE
========================================

This shows you EXACTLY what to do and where to practice.
"""

print("""
╔════════════════════════════════════════════════════════════════════════════════╗
║                     YOUR PYTHON LEARNING STRUCTURE                            ║
╚════════════════════════════════════════════════════════════════════════════════╝


YOUR FOLDER STRUCTURE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C:\\CRMA\\Python\\python_de_practice\\
│
├─ README.md                    👈 START HERE (Overview)
├─ CURRICULUM.md                👈 10-day learning path
├─ QUICK_REFERENCE.md           👈 Visual guide (SAVE THIS!)
├─ PRACTICE_GUIDE.md.py         👈 Step-by-step examples
├─ WHERE_TO_PRACTICE.py         👈 Detailed workflow
│
├─ day01/
│  ├─ exercises.py              👈 YOUR MAIN PRACTICE!
│  ├─ test.py                   👈 SEE SOLUTIONS HERE
│  ├─ practice_pizza.py          👈 (YOU CREATE)
│  ├─ practice_email.py          👈 (YOU CREATE)
│  └─ practice_transaction.py    👈 (YOU CREATE)
│
├─ day02/
│  ├─ exercises.py
│  ├─ test.py
│  └─ practice_*.py (you create)
│
└─ day03, day04, ...


╔════════════════════════════════════════════════════════════════════════════════╗
║                         YOUR DAILY WORKFLOW                                   ║
╚════════════════════════════════════════════════════════════════════════════════╝

TIME: 60-75 MINUTES PER DAY

Step 1 (15 min)         Step 2 (15 min)         Step 3 (20 min)
┌─────────────┐        ┌─────────────┐        ┌──────────────┐
│   READ      │        │   SEE       │        │   PRACTICE   │
│             │        │             │        │              │
│ exercises.py│        │  test.py    │        │ exercises.py │
│             │        │             │        │              │
│ Sections 1-8│        │  python     │        │ Replace TODO │
│ (examples)  │        │  test.py    │        │ with code    │
│             │        │             │        │              │
│ Understand  │───────→│ See complete│───────→│ Write your   │
│ concepts    │        │ solutions   │        │ answers      │
└─────────────┘        └─────────────┘        └──────────────┘
                                                      │
                                                      ↓
                                            ┌──────────────┐
                                            │  Run tests   │
                                            │              │
                                            │  python      │
                                            │  exercises.py│
                                            │              │
                                            │  Does it     │
                                            │  work?       │
                                            └──────────────┘

Step 4 (15-20 min)      Step 5 (5 min)
┌──────────────┐       ┌─────────────┐
│   CREATE     │       │  COMPARE    │
│              │       │             │
│ practice_    │       │ Your code   │
│ pizza.py     │       │ vs.         │
│              │       │ test.py     │
│ practice_    │       │ solutions   │
│ email.py     │       │             │
│              │       │ Understand  │
│ practice_    │       │ your        │
│ trans.py     │       │ approach    │
│              │       │             │
│ Write        │──────→│ Learn why   │
│ variations   │       │ it works    │
└──────────────┘       └─────────────┘


╔════════════════════════════════════════════════════════════════════════════════╗
║                    4 PLACES TO PRACTICE (MAP)                                  ║
╚════════════════════════════════════════════════════════════════════════════════╝


PLACE 1: exercises.py - MAIN PRACTICE
├── What:    # TODO Exercise A, B, C, D
├── Where:   day01/exercises.py (around line 190)
├── How:     Replace TODO with your code
├── Time:    20-30 min per exercise
└── Test:    python exercises.py


PLACE 2: Create YOUR OWN practice_*.py FILES
├── What:    New files with variations
├── Where:   day01/practice_pizza.py (you create)
├── How:     Write similar code, different data
├── Time:    15 min each
├── Examples:
│   ├── practice_pizza.py
│   ├── practice_email.py
│   ├── practice_invoice.py
│   └── practice_transaction.py
└── Test:    python practice_pizza.py


PLACE 3: Modify EXAMPLES (Experiment)
├── What:    Change example values
├── Where:   day01/exercises.py (top sections)
├── How:     Edit numbers, re-run
├── Time:    5-10 min
└── Test:    python exercises.py


PLACE 4: test.py - LEARN FROM SOLUTIONS
├── What:    Complete working examples
├── Where:   day01/test.py
├── How:     Read, understand, compare
├── Time:    10-15 min
└── Test:    python test.py


╔════════════════════════════════════════════════════════════════════════════════╗
║                      EXERCISES.PY STRUCTURE                                    ║
╚════════════════════════════════════════════════════════════════════════════════╝


exercises.py CONTENT:

┌─────────────────────────────────────────────────────────┐
│ SECTION 1: Variables & Naming                           │
│ ├─ Example code with values set                         │
│ └─ Read and understand                                  │
├─────────────────────────────────────────────────────────┤
│ SECTION 2: Data Types                                   │
│ ├─ Example code with values set                         │
│ └─ Read and understand                                  │
├─────────────────────────────────────────────────────────┤
│ SECTION 3: Type Casting                                 │
│ ├─ Example code with values set                         │
│ └─ Read and understand                                  │
│                                                         │
│ ... MORE SECTIONS ...                                   │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ PRACTICAL EXERCISES - YOUR PRACTICE AREA! 👈            │
│                                                         │
│ # TODO Exercise A: Create variables                     │
│ customer_name = ???  👈 WRITE YOUR CODE HERE           │
│ product_name = ???   👈 WRITE YOUR CODE HERE           │
│ ...                                                     │
│                                                         │
│ # TODO Exercise B: Parse data                           │
│ ...                                                     │
│                                                         │
│ # TODO Exercise C: Create function                      │
│ ...                                                     │
│                                                         │
│ # TODO Exercise D: String manipulation                  │
│ ...                                                     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│ MAIN BLOCK (Testing)                                    │
│                                                         │
│ if __name__ == "__main__":                              │
│     print(your_variables)                               │
│     # Run: python exercises.py                          │
│     # See all results                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘


╔════════════════════════════════════════════════════════════════════════════════╗
║                        EXERCISE WORKFLOW EXAMPLE                               ║
╚════════════════════════════════════════════════════════════════════════════════╝


EXERCISE A: Create variables for a customer purchase

INSTRUCTIONS (in exercises.py):
─────────────────────────────
# TODO Exercise A: Create variables for a customer purchase
# - customer_name (string)
# - product_name (string)
# - unit_price (float)
# - quantity (integer)
# - tax_rate (float - use 0.08 for 8%)
# - Calculate: total_before_tax, tax_amount, total_with_tax


YOUR CODE (what you write):
──────────────────────────
customer_name = "karan johoar"
product_name = "laptop"
unit_price = 99.99
quantity = 2
tax_rate = 0.08

total_before_tax = unit_price * quantity
tax_amount = total_before_tax * tax_rate
total_with_tax = total_before_tax + tax_amount


TEST IT:
───────
$ python exercises.py

[Exercise A] Customer Purchase Calculation:
  Customer: karan johoar
  Product: laptop
  Unit Price: $99.99
  Quantity: 2
  Subtotal: $199.98
  Tax (8%): $16.00
  Total: $215.98


UNDERSTAND IT:
──────────────
99.99 * 2 = 199.98         ✓ Subtotal
199.98 * 0.08 = 15.99      ✓ Tax amount
199.98 + 15.99 = 215.97    ✓ Total


COMPARE WITH test.py:
────────────────────
$ python test.py
Look for [Exercise A] section
Compare your code with the solution


CREATE VARIATION (practice_invoice.py):
─────────────────────────────────────
item1_price = 50.00
item2_price = 30.00
qty1 = 3
qty2 = 2
tax_rate = 0.08

subtotal = (item1_price * qty1) + (item2_price * qty2)
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")


╔════════════════════════════════════════════════════════════════════════════════╗
║                           QUICK CHECKLIST                                      ║
╚════════════════════════════════════════════════════════════════════════════════╝


EACH DAY, CHECK THESE:

Exercise Practice:
  [ ] Read exercises.py examples (15 min)
  [ ] Run test.py (10 min)
  [ ] Complete Exercise A (15 min)
  [ ] Complete Exercise B (15 min)
  [ ] Complete Exercise C (10 min)
  [ ] Complete Exercise D (10 min)
  [ ] Run python exercises.py successfully
  [ ] All exercises working correctly

Extra Practice:
  [ ] Create 1 practice_*.py file
  [ ] Modified example values
  [ ] Tested variations
  [ ] Understood why code works


╔════════════════════════════════════════════════════════════════════════════════╗
║                           KEY FILES TO USE                                     ║
╚════════════════════════════════════════════════════════════════════════════════╝


📖 FOR LEARNING:
  ├─ exercises.py         Read annotated examples
  ├─ test.py              See complete solutions
  └─ QUICK_REFERENCE.md   Visual guide (bookmark this!)


✏️  FOR PRACTICE:
  ├─ exercises.py         Fill in # TODO sections
  ├─ practice_*.py        Create your own files
  └─ Modify examples      Change values, test


🔍 FOR HELP:
  ├─ PRACTICE_GUIDE.md.py  Step-by-step walkthrough
  ├─ WHERE_TO_PRACTICE.py  Detailed workflow
  ├─ test.py               See solutions
  └─ This file             Visual diagrams


╔════════════════════════════════════════════════════════════════════════════════╗
║                         YOUR NEXT STEPS NOW                                    ║
╚════════════════════════════════════════════════════════════════════════════════╝


YOU ALREADY DID:
  [✓] Exercise A - Customer Purchase (completed!)

DO THIS NEXT:
  [ ] Complete Exercise B - Parse Transaction
      Location: day01/exercises.py, around line 200
      
  [ ] Complete Exercise C - Validation Function
      Location: day01/exercises.py, around line 208
      
  [ ] Complete Exercise D - String Manipulation
      Location: day01/exercises.py, around line 215
      
  [ ] Test: python exercises.py
      Expected: All exercises print correct output

THEN DO THIS:
  [ ] Create practice_pizza.py
  [ ] Create practice_email.py
  [ ] Create practice_transaction.py
  [ ] Test each one

FINALLY:
  [ ] Compare your code with test.py
  [ ] Understand your approach
  [ ] Ready for Day 02!


╔════════════════════════════════════════════════════════════════════════════════╗
║                              YOU'VE GOT THIS! 🚀                              ║
╚════════════════════════════════════════════════════════════════════════════════╝

You have EVERYTHING you need to practice:

✓ Clear instructions (exercises.py)
✓ Working examples (test.py)
✓ Multiple practice locations
✓ Detailed guides (PRACTICE_GUIDE.md.py, WHERE_TO_PRACTICE.py)
✓ Visual references (QUICK_REFERENCE.md, this file)

Now go write some code and learn! Remember:
THE ONLY WAY TO LEARN IS BY DOING!

Good luck! 🎯
""")
