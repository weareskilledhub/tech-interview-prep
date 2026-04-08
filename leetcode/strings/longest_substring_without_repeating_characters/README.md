# Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the longest substring without repeating characters.

A **substring** must be contiguous.

---

## Examples

### Example 1

**Input**

```text
s = "abcabcbb"
````

**Output**

```text
3
```

**Explanation**

The answer is `"abc"`, with the length of `3`.

Other valid substrings with the same length include:

* `"bca"`
* `"cab"`

---

### Example 2

**Input**

```text
s = "bbbbb"
```

**Output**

```text
1
```

**Explanation**

The answer is `"b"`, with the length of `1`.

---

### Example 3

**Input**

```text
s = "pwwkew"
```

**Output**

```text
3
```

**Explanation**

The answer is `"wke"`, with the length of `3`.

Note that `"pwke"` is a subsequence, not a substring.

---

## Constraints

* `0 <= s.length <= 5 * 10^4`
* `s` consists of English letters, digits, symbols, and spaces

---

## Expected Thinking Process

When solving this problem, think about the following:

* A substring must be contiguous
* Repeated characters inside the current window are not allowed
* How can we move through the string without restarting from every position?
* Can we track the current valid substring efficiently?

This problem is a classic **sliding window** problem.

---

## Recommended Approach

A strong solution uses:

* two pointers
* a hash map / dictionary
* sliding window logic

### Core idea

We maintain a window `[left, right]` such that all characters inside it are unique.

We use:

* `left` → start of the current window
* `right` → end of the current window
* `last_index` → stores the last seen index of each character
* `max_len` → stores the maximum valid window length found so far

### Steps

1. Traverse the string with `right`
2. Let `ch = s[right]`
3. If `ch` has been seen before and its last seen index is inside the current window:

   * move `left` to `last_index[ch] + 1`
4. Update the last seen index of `ch`
5. Update the current maximum length

This allows us to process the string efficiently in one pass.

---

## Why Sliding Window Works

At every step, we maintain a valid substring with no repeated characters.

Instead of checking every possible substring from scratch, we only expand or shrink the current window as needed.

This avoids unnecessary repeated work.

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(min(n, m))`

Where:

* `n` = length of the string
* `m` = size of the character set used in the string

### Why?

* Each character is processed at most a constant number of times
* The dictionary stores the latest position of characters

---

## Common Mistakes

### 1. Confusing substring and subsequence

A substring must be contiguous.

For example:

* `"wke"` is a substring of `"pwwkew"`
* `"pwke"` is not a substring

### 2. Moving `left` backward

When a duplicate appears, `left` should only move forward.

That is why we must check whether the previous index is still inside the current window.

### 3. Recomputing windows from scratch

That usually leads to a slower solution such as `O(n^2)`.

### 4. Forgetting the empty string case

If `s = ""`, the answer should be `0`.

---

## Student Task

Implement the solution in:

```text
solution.py
```

Before opening a Pull Request, make sure that:

* your code handles empty strings
* your code correctly updates the window
* your code does not move `left` backward
* you understand why the solution is `O(n)`
* you use the shared benchmark utility if needed

---

## Suggested Test Cases

### Case 1

```text
s = "abcabcbb"
expected = 3
```

### Case 2

```text
s = "bbbbb"
expected = 1
```

### Case 3

```text
s = "pwwkew"
expected = 3
```

### Case 4

```text
s = ""
expected = 0
```

### Case 5

```text
s = "dvdf"
expected = 3
```

### Case 6

```text
s = "abba"
expected = 2
```

### Case 7

```text
s = " "
expected = 1
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
└── strings/
    └── longest_substring_without_repeating_characters/
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


