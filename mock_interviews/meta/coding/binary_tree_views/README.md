# Binary Tree Views

## Company

Meta

## Category

Coding Interview

---

## Problem

Given the root of a binary tree, return the visible nodes from the **left view** and the **right view** of the tree.

- The **left view** contains the first visible node from each level when the tree is viewed from the left side.
- The **right view** contains the last visible node from each level when the tree is viewed from the right side.

Return the result in the following format:

```python
{
    "left_view": [...],
    "right_view": [...]
}
```

---

## Example

### Example 1

**Input**

```text
        1
      /   \
     2     3
      \     \
       5     4
```

**Output**

```python
{
    "left_view": [1, 2, 5],
    "right_view": [1, 3, 4]
}
```

**Explanation**

- Level 0 → leftmost = `1`, rightmost = `1`
- Level 1 → leftmost = `2`, rightmost = `3`
- Level 2 → leftmost = `5`, rightmost = `4`

---

### Example 2

**Input**

```text
        10
       /
      6
     /
    3
```

**Output**

```python
{
    "left_view": [10, 6, 3],
    "right_view": [10, 6, 3]
}
```

---

### Example 3

**Input**

```text
root = None
```

**Output**

```python
{
    "left_view": [],
    "right_view": []
}
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^5]`
- `-10^4 <= Node.val <= 10^4`

---

## Expected Thinking Process

When solving this problem, think about the following:

- How can you process the tree level by level?
- How can you identify the first node of a level?
- How can you identify the last node of a level?
- Is BFS a natural fit here?
- Could DFS also work if level information is tracked?

This problem is not only about tree traversal.  
It is also about understanding what is visible from different perspectives of the same tree.

---

## Recommended Approach

A clean solution usually uses **Breadth-First Search (BFS)**.

### Core idea

1. Traverse the tree level by level.
2. For each level:
   - the first node gives the **left view**
   - the last node gives the **right view**
3. Store both results and return them at the end.

This approach is simple, readable, and efficient.

---

## Why BFS Works Well

BFS naturally groups nodes by depth.

That makes it easy to determine:

- the first node in a level
- the last node in a level

This is why BFS is often the most straightforward solution for this problem.

---

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

Where `n` is the number of nodes in the tree.

---

## Common Mistakes

### 1. Mixing up traversal order and visible order

Traversal order is not the same thing as what is visible from a side view.

### 2. Forgetting to process by level

If level boundaries are ignored, the result may be incorrect.

### 3. Not handling an empty tree

If `root` is `None`, both views should be empty lists.

### 4. Taking the wrong node for the view

- left view → first node at each level
- right view → last node at each level

---

## Student Task

Implement the solution in:

```text
solution.py
```

Before opening a Pull Request, make sure that:

- your code handles an empty tree
- your code returns both left and right views
- your solution works level by level
- you understand why BFS is a strong choice
- you use the shared benchmark utility if needed

---

## Suggested Test Cases

### Case 1

```text
Tree:
        1
      /   \
     2     3
      \     \
       5     4

Expected:
left_view  = [1, 2, 5]
right_view = [1, 3, 4]
```

### Case 2

```text
Tree:
        10
       /
      6
     /
    3

Expected:
left_view  = [10, 6, 3]
right_view = [10, 6, 3]
```

### Case 3

```text
Tree:
None

Expected:
left_view  = []
right_view = []
```

### Case 4

```text
Tree:
    7
     \
      8
       \
        9

Expected:
left_view  = [7, 8, 9]
right_view = [7, 8, 9]
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
        └── binary_tree_views/
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