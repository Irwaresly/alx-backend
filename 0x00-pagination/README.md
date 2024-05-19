# 0x00. Pagination

## Description

This project focuses on implementing pagination in a backend context using Python. Pagination is essential for handling large datasets by breaking them into smaller, manageable chunks. The project covers simple pagination with page and page_size parameters, hypermedia pagination, and deletion-resilient pagination. 

## Learning Objectives

By the end of this project, you should be able to:

- Implement simple pagination using page and page_size parameters.
- Implement hypermedia pagination with metadata.
- Ensure pagination is deletion-resilient.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- Code style must follow pycodestyle (version 2.5.*)
- All modules, functions, and classes must have documentation.
- Functions and coroutines must be type-annotated.

## Project Tasks

### Task 0: Simple Helper Function

Create a function `index_range` that returns a tuple containing the start and end indexes for pagination.

**File:** `0-simple_helper_function.py`

### Task 1: Simple Pagination

Implement a `Server` class that reads a CSV file and paginates the dataset.

**File:** `1-simple_pagination.py`

### Task 2: Hypermedia Pagination

Extend the `Server` class to include hypermedia pagination with metadata.

**File:** `2-hypermedia_pagination.py`

### Task 3: Deletion-Resilient Hypermedia Pagination

Enhance the `Server` class to ensure pagination is resilient to deletions.

**File:** `3-hypermedia_del_pagination.py`

## How to Use

1. Clone the repository.
2. Ensure you have Python 3.7 installed.
3. Run the provided `main.py` files to test the implementation.
4. Modify the dataset file `Popular_Baby_Names.csv` as required.
