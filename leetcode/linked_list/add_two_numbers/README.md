
# Add Two Numbers

## Problem

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in **reverse order**, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number `0` itself.

---

## Examples

### Example 1

**Input**

```text
l1 = [2, 4, 3]
l2 = [5, 6, 4]
````

**Output**

```text
[7, 0, 8]
```

**Explanation**

```text
342 + 465 = 807
```

Since the digits are stored in reverse order:

* `l1 = [2, 4, 3]` represents `342`
* `l2 = [5, 6, 4]` represents `465`

Their sum is `807`, so the result is:

```text
[7, 0, 8]
```

---

### Example 2

**Input**

```text
l1 = [0]
l2 = [0]
```

**Output**

```text
[0]
```

---

### Example 3

**Input**

```text
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
```

**Output**

```text
[8, 9, 9, 9, 0, 0, 0, 1]
```

---

## Constraints

* The number of nodes in each linked list is in the range `[1, 100]`
* `0 <= Node.val <= 9`
* It is guaranteed that the list represents a number that does not have leading zeros

---

## Expected Thinking Process

When solving this problem, think about the following:

* How do we add two numbers digit by digit?
* What happens when the sum of two digits is greater than or equal to `10`?
* How do we keep track of the carry value?
* What happens if one linked list is longer than the other?
* What if a carry remains after both lists end?

This problem is essentially the linked-list version of elementary school addition.

---

## Recommended Approach

A strong solution uses:

* two pointers for the two linked lists
* a `carry` variable
* a dummy head node to simplify result list construction

### Core idea

1. Traverse both linked lists at the same time.
2. Read the current digit from each list. If a list has ended, use `0`.
3. Compute:

```text
digit_sum = val1 + val2 + carry
```

4. The new digit becomes:

```text
digit_sum % 10
```

5. The new carry becomes:

```text
digit_sum // 10
```

6. Add the new digit to the result linked list.
7. Continue until:

   * both lists are finished
   * and there is no remaining carry

---

## Why a Dummy Node Helps

A dummy head node makes linked list construction easier.

Without a dummy node, you would need extra logic for:

* creating the first node
* handling the head separately

With a dummy node:

* append nodes normally
* return `dummy.next` at the end

This makes the code cleaner and less error-prone.

---

## Complexity

* **Time Complexity:** `O(max(n, m))`
* **Space Complexity:** `O(max(n, m))`

Where:

* `n` is the length of `l1`
* `m` is the length of `l2`

### Why?

* We visit each node at most once.
* The result linked list may contain up to `max(n, m) + 1` nodes.

---

## Common Mistakes

### 1. Forgetting the carry at the end

Example:

```text
[5] + [5] = [0, 1]
```

If the final carry is ignored, the result becomes incorrect.

### 2. Stopping when one list ends

The algorithm must continue until both lists are finished.

### 3. Reversing the interpretation of digits

The digits are stored in **reverse order**.

So:

```text
[2, 4, 3]
```

means:

```text
342
```

not `243`.

### 4. Not handling different list lengths

One list may be longer than the other.

---

## Student Task

Implement the solution in:

```text
solution.py
```

Before opening a Pull Request, make sure that:

* your solution handles carry correctly
* your solution works when the lists have different lengths
* your solution works when both inputs are zero
* your solution works when a final carry creates a new node
* you understand why the result is also stored in reverse order

---

## Suggested Test Cases

### Case 1

```text
l1 = [2, 4, 3]
l2 = [5, 6, 4]
expected = [7, 0, 8]
```

### Case 2

```text
l1 = [0]
l2 = [0]
expected = [0]
```

### Case 3

```text
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
expected = [8, 9, 9, 9, 0, 0, 0, 1]
```

### Case 4

```text
l1 = [5]
l2 = [5]
expected = [0, 1]
```

### Case 5

```text
l1 = [1, 8]
l2 = [0]
expected = [1, 8]
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
leetcode/
└── linked_list/
    └── add_two_numbers/
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

