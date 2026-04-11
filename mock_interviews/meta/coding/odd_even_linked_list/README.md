
## Company

Meta

## Category

Coding Interview

---

## Problem

Given the head of a singly linked list, group all nodes positioned at **odd indices** together followed by the nodes positioned at **even indices**, and return the reordered list.

Important:

- The grouping is based on the **node position**, not the node value.
- The first node is considered **odd**, the second node is **even**, and so on.
- You must preserve the **relative order** of the odd nodes and the relative order of the even nodes.

---

## Example

### Example 1

**Input**

```text
1 -> 2 -> 3 -> 4 -> 5
````

**Output**

```text
1 -> 3 -> 5 -> 2 -> 4
```

**Explanation**

* Odd positions: `1, 3, 5`
* Even positions: `2, 4`
* Final order: odd nodes first, then even nodes

---

### Example 2

**Input**

```text
2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
```

**Output**

```text
2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

**Explanation**

* Odd positions: `2, 3, 6, 7`
* Even positions: `1, 5, 4`

---

### Example 3

**Input**

```text
head = None
```

**Output**

```text
None
```

---

## Constraints

* The number of nodes in the list is in the range `[0, 10^4]`
* `-10^6 <= Node.val <= 10^6`

---

## Expected Thinking Process

When solving this problem, think about the following:

* Are we grouping by **value** or by **position**?
* How can we separate odd-position nodes and even-position nodes in one traversal?
* How can we reconnect the list without creating new nodes?
* Can this be done in `O(n)` time?
* Can this be done using only `O(1)` extra space?

This problem is not only about linked lists.
It is also about careful **pointer manipulation** under interview pressure.

---

## Recommended Approach

A clean solution usually uses **two running pointers**:

* one pointer for the odd chain
* one pointer for the even chain

You also keep a reference to the **head of the even list** so that after finishing the odd chain, you can connect it to the even chain.

### Core idea

1. Handle the edge case where the list is empty.
2. Start:

   * `odd = head`
   * `even = head.next`
   * `even_head = even`
3. While `even` and `even.next` exist:

   * link the next odd node
   * move the odd pointer
   * link the next even node
   * move the even pointer
4. At the end, connect the odd chain to `even_head`

This approach is efficient, interview-friendly, and does not require extra arrays or lists.

---

## Why This Works Well

The linked list is already in alternating odd-even order by position.

That means we do not need to compute indices explicitly.

We can simply:

* skip one node at a time for the odd chain
* skip one node at a time for the even chain

By doing this carefully, we split the original list into two internal chains and then join them at the end.

This is why the pointer-based solution is both elegant and optimal.

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

Where `n` is the number of nodes in the linked list.

---

## Common Mistakes

### 1. Grouping by node value instead of node position

This is the most common mistake.

The problem does **not** ask for odd values and even values.
It asks for nodes at odd and even **indices**.

---

### 2. Losing the head of the even list

If you do not store `even_head` at the beginning, you may not be able to reconnect the even chain correctly at the end.

---

### 3. Breaking the list structure

Incorrect pointer updates can:

* skip nodes
* create cycles
* disconnect part of the list

Order matters a lot in linked list manipulation.

---

### 4. Not handling short lists

Lists with:

* `0` nodes
* `1` node
* `2` nodes

should still work correctly without errors.

---

## Student Task

Implement the solution in:

```text
solution.py
```

Before opening a Pull Request, make sure that:

* your code handles an empty list
* your code preserves relative order
* your solution groups by position, not value
* your code runs in `O(n)` time
* your solution uses `O(1)` extra space
* you understand why `even_head` must be saved

---

## Suggested Test Cases

### Case 1

```text
Input:
1 -> 2 -> 3 -> 4 -> 5

Expected:
1 -> 3 -> 5 -> 2 -> 4
```

### Case 2

```text
Input:
2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7

Expected:
2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

### Case 3

```text
Input:
None

Expected:
None
```

### Case 4

```text
Input:
1

Expected:
1
```

### Case 5

```text
Input:
1 -> 2

Expected:
1 -> 2
```

### Case 6

```text
Input:
1 -> 2 -> 3 -> 4

Expected:
1 -> 3 -> 2 -> 4
```

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
mock_interviews/
└── meta/
    └── coding/
        └── odd_even_linked_list/
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

