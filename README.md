# Python Daily Practice

Welcome! 👋

This repository is dedicated to my daily Python practice. My goal is to improve my Python skills by solving exercises, building small projects, and learning new concepts every day.

## Structure
- Each folder (day01, day02, ...) contains the code and exercises I worked on that day.
- Test files are included to check my solutions.

## Why this repo?
- To track my progress and stay consistent.
- To showcase my commitment to learning Python.
- To help others who want to follow a similar path.

## How to use
- Browse the folders by day to see my daily work.
- Feel free to suggest improvements or new challenges!

---

**Let’s keep learning, one day at a time!**
cd day01
python exercises.py
```

### Tips for Success

1. **Type the Code** - Don't just read it, type it out
2. **Experiment** - Change values, break things, see what happens
3. **Complete TODO Exercises** - These reinforce learning
4. **Run Often** - Test your code frequently
5. **Move Sequentially** - Each day builds on previous days

## Current Progress

### ✅ Completed Days

**Day 01: Python Fundamentals & Data Types**
- Variables and naming conventions
- Data types: int, float, str, bool
- Type casting and conversions
- String manipulation and f-strings
- Basic arithmetic and logical operations

**Day 02: Data Structures**
- Lists: The foundation of data processing
- Dictionaries: Representing records
- List of Dictionaries: Most common data structure
- Tuples: Immutable sequences
- Sets: Unique values and deduplication

**Day 03: Control Flow & Functions**
- If/elif/else decision making
- For and while loops
- Functions: Reusable logic
- Lambda functions
- Practical validation patterns

**Day 04: File I/O & Data Processing**
- Reading and writing files
- Processing files line by line
- Working with different file formats
- Error handling
- Complete ETL pipeline example

### 🚧 Coming Next

**Day 05: Working with JSON & CSV** (Coming soon)
**Day 06: Error Handling & Data Validation** (Coming soon)
**Day 07: AWS Libraries (boto3)** (Coming soon)

## Day-by-Day Breakdown

### Day 01: Fundamentals
**What you'll learn:**
- How to work with different data types
- Converting between types (critical for data pipelines)
- String manipulation for data processing
- Validation logic

**Key for AWS DE:**
- Data from APIs and S3 comes as strings
- Must convert to appropriate types
- Validate before processing

### Day 02: Data Structures
**What you'll learn:**
- Lists for sequences of data
- Dicts for records (like JSON objects)
- Combining lists and dicts (like database rows)
- Sets for finding unique values

**Key for AWS DE:**
- Every API response is a dict or list of dicts
- Database query results are lists of dicts
- Sets help with deduplication

### Day 03: Control Flow & Functions
**What you'll learn:**
- Making decisions with if/else
- Processing data with loops
- Writing reusable functions
- Building validation logic

**Key for AWS DE:**
- Every pipeline has validation logic
- Functions make code reusable
- Loops process batches of records

### Day 04: File I/O
**What you'll learn:**
- Reading data from files
- Writing results to files
- Processing large files efficiently
- Handling errors gracefully

**Key for AWS DE:**
- S3 operations are similar to file operations
- Must handle corrupt or missing data
- ETL patterns (Extract, Transform, Load)

## Common Questions

**Q: Do I need prior Python experience?**
A: No! This course assumes you know the concepts but not how to write the code.

**Q: How long will this take?**
A: Spend 1-2 hours per day. Take your time with exercises.

**Q: Can I skip days?**
A: Not recommended! Each day builds on previous days.

**Q: What if I get stuck?**
A: Look at the test.py file for the same day - it has solutions!

**Q: When will I learn AWS-specific stuff?**
A: Day 07+ covers boto3, S3, DynamoDB, etc. Days 1-6 build the foundation.

## Practical Examples in This Course

Throughout this course, you'll work with realistic scenarios:
- Processing transaction records
- Validating customer data
- Reading from CSV/JSON files
- Building ETL pipelines
- Handling errors gracefully
- Aggregating and transforming data

## Getting Help

If you're stuck:
1. Read the comments in exercises.py
2. Look at test.py for that day
3. Try smaller parts of the code
4. Print variables to see what they contain
5. Search for error messages online

## Next Steps

1. Open [CURRICULUM.md](CURRICULUM.md) to see the full learning path
2. Start with [day01/exercises.py](day01/exercises.py)
3. Run [day01/test.py](day01/test.py) to see examples
4. Complete the TODO exercises
5. Move to day02 when ready!

## Remember

**The best way to learn programming is by writing code!**

Don't just read - type it out, experiment, break things, fix them. That's how you learn.

Good luck! 🚀
