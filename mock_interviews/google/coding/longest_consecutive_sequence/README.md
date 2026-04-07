# Longest Consecutive Sequence with a FAANG Engineer

## Company

Google

## Category

Coding Interview

---

## Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

---

## Examples

### Example 1

**Input**

```text
nums = [100, 4, 200, 1, 3, 2]
```

**Output**

```text
4
```

**Explanation**

The longest consecutive sequence is:

```text
[1, 2, 3, 4]
```

Its length is `4`.

---

### Example 2

**Input**

```text
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
```

**Output**

```text
9
```

**Explanation**

The longest consecutive sequence is:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8]
```

Its length is `9`.

---

### Example 3

**Input**

```text
nums = [1, 0, 1, 2]
```

**Output**

```text
3
```

**Explanation**

The longest consecutive sequence is:

```text
[0, 1, 2]
```

Its length is `3`.

---

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Expected Thinking Process

When solving this problem, think about the following questions:

- How would a brute-force solution work?
- Why would sorting be slower than the expected target?
- How can we quickly check whether a number exists in the array?
- How can we avoid counting the same sequence many times?

A strong solution should avoid unnecessary repeated checks.

---

## Recommended Approach

A good `O(n)` solution uses a **set**.

### Core idea

1. Put all numbers into a set for fast lookup.
2. A number should be treated as the **start** of a sequence only if `num - 1` is not in the set.
3. If it is the start, keep checking `num + 1`, `num + 2`, and so on.
4. Track the maximum sequence length found.

This works well because each number is effectively processed only when needed.

---

## Why a Set Helps

A set allows fast membership checking:

- `x in my_set`

This is much faster than searching inside a list again and again.

That is why a set-based solution can achieve the expected `O(n)` time complexity.

---

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Common Mistakes

### 1. Sorting first and assuming it is optimal

Sorting is a valid idea, but it usually gives:

- **Time Complexity:** `O(n log n)`

This does not meet the expected `O(n)` target.

### 2. Starting from every number

If you try to build a sequence starting from every element, you may repeat the same work many times.

### 3. Forgetting duplicates

The input may contain duplicate values.  
Using a set helps remove duplicates automatically for lookup purposes.

---

## Student Task

Implement the solution in:

```text
solution.py
```

Before opening a Pull Request, make sure that:

- your code works correctly
- the sample cases produce the expected outputs
- you understand why the solution is `O(n)`
- you can explain why a set is used
- you use the shared benchmark utility if needed

---

## Suggested Test Cases

You should test at least the following cases:

### Case 1
```text
nums = [100, 4, 200, 1, 3, 2]
expected = 4
```

### Case 2
```text
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
expected = 9
```

### Case 3
```text
nums = [1, 0, 1, 2]
expected = 3
```

### Case 4
```text
nums = []
expected = 0
```

### Case 5
```text
nums = [5]
expected = 1
```

### Case 6
```text
nums = [10, 30, 20]
expected = 1
```

---

## Benchmark Note

This repository includes a shared benchmark tool:

```text
tools/benchmark.py
```

You may use it to observe:

- runtime
- peak memory
- peak CPU usage

Important: benchmark values and Big-O complexity are not the same thing.

- **Big-O** explains theoretical growth
- **Benchmark** shows practical execution measurements

Both are useful, but they answer different questions.

---

## File Structure

This problem should follow this structure:

```text
mock_interviews/
└── google/
    └── coding/
        └── longest_consecutive_sequence/
            ├── README.md
            └── solution.py
```

---

## Goal

The goal is not only to produce a working answer.

The real goal is to write a solution that is:

- correct
- readable
- efficient
- explainable in an interview