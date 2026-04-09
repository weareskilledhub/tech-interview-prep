
# Contains Duplicate

## Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## Examples

### Example 1

**Input**

```text
nums = [1, 2, 3, 1]
````

**Output**

```text
true
```

**Explanation**

The value `1` appears more than once.

---

### Example 2

**Input**

```text
nums = [1, 2, 3, 4]
```

**Output**

```text
false
```

**Explanation**

All elements are distinct.

---

### Example 3

**Input**

```text
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
```

**Output**

```text
true
```

**Explanation**

Several values appear more than once.

---

## Constraints

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

---

## Expected Thinking Process

When solving this problem, think about the following:

* How can we detect duplicates efficiently?
* Do we need to compare every pair of elements?
* Can a data structure help us remember what we have already seen?
* What is the trade-off between speed and memory?

This problem looks simple, but it is a good introduction to **set-based lookup**.

---

## Recommended Approach

A strong solution uses a **set**.

### Core idea

1. Traverse the array from left to right.
2. Keep a set of values that have already been seen.
3. If the current value is already in the set, return `True`.
4. If not, add it to the set and continue.
5. If the loop ends, return `False`.

This approach is clean, readable, and efficient.

---

## Why a Set Helps

A set allows fast membership checking:

```python
value in seen
```

This makes it possible to detect duplicates without repeatedly scanning the full array.

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

### Why?

* We may visit each element once.
* We may store up to `n` elements in the set.

---

## Common Mistakes

### 1. Writing the wrong complexity

A set-based solution is **not** `O(1)` overall.

Correct complexity:

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

### 2. Comparing full lists unnecessarily

A student may try:

* convert to set
* compare lengths

That works, but it is still important to understand **why** it works.

### 3. Using nested loops

A brute-force solution with nested loops usually leads to:

* **Time Complexity:** `O(n^2)`

This becomes slow for large inputs.

---

## Student Task

Implement the solution in:

```text
solution.py
```

Before opening a Pull Request, make sure that:

* your code returns the correct boolean value
* your code handles repeated values correctly
* you understand why a set is used
* you can explain the time and space complexity
* you use the shared benchmark utility if needed

---

## Suggested Test Cases

### Case 1

```text
nums = [1, 2, 3, 1]
expected = True
```

### Case 2

```text
nums = [1, 2, 3, 4]
expected = False
```

### Case 3

```text
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
expected = True
```

### Case 4

```text
nums = [5]
expected = False
```

### Case 5

```text
nums = [0, 0]
expected = True
```

---

## Alternative Idea

Another valid approach is:

* convert the list to a set
* compare lengths

Example idea:

```python
len(nums) != len(set(nums))
```

This is also acceptable, but students should still understand the underlying set logic.

---

## Benchmark Note

This repository includes a shared benchmark tool:

```text
tools/benchmark.py
```

You may use it to observe:

* runtime
* peak memory
* peak CPU usage

Important: benchmark values and Big-O complexity are not the same thing.

* **Big-O** explains theoretical growth
* **Benchmark** shows practical execution measurements

Both are useful, but they answer different questions.

---

## File Structure

This problem should follow this structure:

```text
leetcode/
└── arrays/
    └── contains_duplicate/
        ├── README.md
        └── solution.py
```

---

## Goal

The goal is not only to produce a working answer.

The real goal is to write a solution that is:

* correct
* readable
* efficient
* explainable in an interview



