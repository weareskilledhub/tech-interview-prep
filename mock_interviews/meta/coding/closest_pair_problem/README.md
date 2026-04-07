# Closest Pair Problem

## Company

Meta

## Category

Coding Interview

---

## Problem

Given a list of points in a 2D plane, return the **minimum Euclidean distance** between any two distinct points.

Each point is represented as:

```python
(x, y)
```

If the input contains fewer than two points, return `0.0`.

---

## Examples

### Example 1

**Input**

```text
points = [(0, 0), (3, 4), (7, 7)]
```

**Output**

```text
5.0
```

**Explanation**

The distance between `(0, 0)` and `(3, 4)` is:

```text
sqrt((3 - 0)^2 + (4 - 0)^2) = 5.0
```

This is the smallest pairwise distance in the set.

---

### Example 2

**Input**

```text
points = [(1, 1), (2, 2), (10, 10)]
```

**Output**

```text
1.4142
```

**Explanation**

The closest pair is `(1, 1)` and `(2, 2)`.

Distance:

```text
sqrt(2) ≈ 1.4142
```

---

### Example 3

**Input**

```text
points = [(5, 5)]
```

**Output**

```text
0.0
```

---

## Constraints

- `0 <= len(points) <= 10^5`
- Coordinates may be positive, negative, or zero

---

## Expected Thinking Process

When solving this problem, think about the following:

- How would the brute-force solution work?
- What is the cost of checking all pairs?
- Can sorting or divide-and-conquer improve performance?
- What does “closest” mean mathematically?

This problem combines algorithm design and geometry reasoning.

---

## Recommended Approaches

### Approach 1 — Brute Force

Check every pair of points and keep the minimum distance.

This is simple and easy to understand.

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

### Approach 2 — Divide and Conquer

A more advanced solution sorts points and recursively narrows the search.

This can improve performance to:

- **Time Complexity:** `O(n log n)`

This approach is more advanced and may be discussed in stronger interview settings.

---

## Euclidean Distance Formula

For two points:

```text
(x1, y1) and (x2, y2)
```

The Euclidean distance is:

```text
sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

---

## Complexity

### Brute-force solution
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

### Divide-and-conquer solution
- **Time Complexity:** `O(n log n)`
- **Space Complexity:** depends on implementation details

---

## Common Mistakes

### 1. Comparing only x or only y differences

Closest distance depends on both coordinates.

### 2. Forgetting edge cases

If there are fewer than two points, return `0.0`.

### 3. Using the wrong distance formula

Be careful with subtraction, squaring, and square root usage.

### 4. Confusing squared distance and actual distance

Squared distance can help comparison, but the final returned value should match the problem requirement.

---

## Student Task

Implement the solution in:

```text
solution.py
```

Before opening a Pull Request, make sure that:

- your code handles empty and single-point inputs
- your distance calculation is correct
- your output is numeric
- you understand the time complexity of your approach
- you use the shared benchmark utility if needed

---

## Suggested Test Cases

### Case 1

```text
points = [(0, 0), (3, 4), (7, 7)]
expected = 5.0
```

### Case 2

```text
points = [(1, 1), (2, 2), (10, 10)]
expected ≈ 1.4142
```

### Case 3

```text
points = [(5, 5)]
expected = 0.0
```

### Case 4

```text
points = []
expected = 0.0
```

### Case 5

```text
points = [(0, 0), (0, 1), (10, 10)]
expected = 1.0
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
└── meta/
    └── coding/
        └── closest_pair_problem/
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