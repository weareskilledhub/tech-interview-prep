# Top K Frequent Elements

## Company

Amazon

## Category

Coding Interview

---

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

You may return the answer in **any order**.

---

## Examples

### Example 1

**Input**

```text
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

**Output**

```text
[1, 2]
```

**Explanation**

- `1` appears `3` times
- `2` appears `2` times
- `3` appears `1` time

The `2` most frequent elements are `[1, 2]`.

---

### Example 2

**Input**

```text
nums = [1]
k = 1
```

**Output**

```text
[1]
```

**Explanation**

There is only one element in the array, so the answer is `[1]`.

---

### Example 3

**Input**

```text
nums = [4, 4, 4, 5, 5, 6, 6, 6, 6]
k = 2
```

**Output**

```text
[6, 4]
```

**Explanation**

- `6` appears `4` times
- `4` appears `3` times
- `5` appears `2` times

The `2` most frequent elements are `[6, 4]`.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= number of unique elements in nums`

---

## Expected Thinking Process

When solving this problem, think about the following questions:

- How can we count how many times each number appears?
- After counting, how can we select the top `k` elements efficiently?
- Is sorting the entire frequency list always necessary?
- Which data structure is useful for keeping the highest-frequency elements?

This problem is not only about counting.  
It is also about selecting the most frequent items efficiently.

---

## Recommended Approach

A strong solution usually uses:

- a **hash map / dictionary** for frequency counting
- a **heap** or another efficient selection strategy for retrieving the top `k` frequent elements

### Core idea

1. Count the frequency of each number.
2. Store frequency information in a suitable structure.
3. Extract the `k` elements with the highest frequencies.
4. Return the result.

---

## Why a Dictionary Helps

A dictionary lets us count frequencies efficiently.

Example idea:

- number → count

Such as:

```text
1 -> 3
2 -> 2
3 -> 1
```

This allows fast counting in one pass through the array.

---

## Why a Heap Can Help

A heap is useful when you want to efficiently retrieve the largest or smallest elements based on a priority.

In this problem, the priority is:

- **frequency**

A heap-based solution is often more efficient than sorting everything when the input is large.

---

## Complexity

A common good solution has:

- **Time Complexity:** `O(n log k)` or `O(n log n)` depending on the approach
- **Space Complexity:** `O(n)`

### Note

- If you sort all frequency pairs, complexity is usually higher.
- If you use a heap of size `k`, you can often reduce the selection cost.

Students should understand **why** one approach is better than another.

---

## Common Mistakes

### 1. Sorting without understanding the cost

Sorting works, but students should think about whether it is the most efficient option.

### 2. Forgetting that output order does not matter

The problem says the answer can be returned in **any order**.

### 3. Mixing up frequency and value

The largest value is not always the most frequent value.

### 4. Ignoring duplicate counting logic

The real task is frequency counting first, not unique value listing.

---

## Student Task

Implement the solution in:

```text
solution.py
```

Before opening a Pull Request, make sure that:

- your code works correctly
- your solution returns the `k` most frequent elements
- you understand your frequency counting logic
- you can explain your data structure choice
- you use the shared benchmark utility if needed

---

## Suggested Test Cases

You should test at least the following cases:

### Case 1

```text
nums = [1, 1, 1, 2, 2, 3]
k = 2
expected = [1, 2]
```

### Case 2

```text
nums = [1]
k = 1
expected = [1]
```

### Case 3

```text
nums = [4, 4, 4, 5, 5, 6, 6, 6, 6]
k = 2
expected = [6, 4]
```

### Case 4

```text
nums = [1, 2, 3, 4]
k = 1
expected = [1] or [2] or [3] or [4]
```

### Case 5

```text
nums = [5, 5, 5, 5]
k = 1
expected = [5]
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
└── amazon/
    └── coding/
        └── top_k_frequent_elements/
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