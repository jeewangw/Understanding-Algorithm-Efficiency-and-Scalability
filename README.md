# Assignment 3: How Well Algorithms Work and Grow

## Overview
This repository has Python code and a report on Randomized Quicksort and Hashing with Chaining. We tested these algorithms to see how they handle different kinds of data and loads.

## Files in This Project
- `randomized_quicksort.py`: Randomized Quicksort algorithm.
- `deterministic_quicksort.py`: Deterministic Quicksort algorithm (uses the first element as pivot).
- `hash_table_chaining.py`: A hash table using chaining to handle collisions.
- `report.pdf`: A report explaining the tests, results, and conclusions.
- `README.md`: Instructions on how to run the code and a summary of results.

## How to Run the Code
1. **Comparing Randomized and Deterministic Quicksort:**
   - Run `randomized_quicksort.py` and `deterministic_quicksort.py` on lists with different types (random, sorted, reverse-sorted, etc.).
   - Use the sample lists in the code or create your own to see how each algorithm performs.

2. **Running the Hash Table with Chaining:**
   - Run `hash_table_chaining.py` to insert, search, and delete items in a hash table.
   - Test how it performs as you increase the number of items to see how resizing keeps it efficient.

## Summary of Results
- **Randomized Quicksort** works consistently at \(O(n \log n)\) time, regardless of the list type.
- **Deterministic Quicksort** slows down to \(O(n^2)\) with sorted data due to unbalanced splits.
- **Hashing with Chaining** remains fast by resizing to manage load, keeping search, insert, and delete times steady.

For more details, see the `report.pdf`.

## Author
- Jeevan Gyawali
