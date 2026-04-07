# Tech Interview Prep

A structured repository for LeetCode practice and coding-based mock interview preparation for top tech companies.

This repository is designed for students who want to improve their problem-solving skills, algorithmic thinking, coding interview performance, and Git/GitHub workflow discipline.

---

## Purpose

This repository helps students improve in the following areas:

- problem solving
- data structures and algorithms
- clean code habits
- time and space complexity analysis
- benchmark-based performance awareness
- branch and pull request workflow
- collaborative development using GitHub

---

## Scope

This repository currently focuses on two main areas:

- **LeetCode practice**
- **Coding mock interviews** for:
  - Amazon
  - Meta
  - Google
  - Microsoft

At this stage, the repository is focused on **coding interview preparation only**.  
System design and behavioral interview content are intentionally excluded for now.

---

## Repository Structure

```text
tech-interview-prep/
├── GUIDE.md
├── README.md
├── requirements-dev.txt
├── .gitignore
├── tools/
│   └── benchmark.py
├── leetcode/
│   ├── arrays/
│   ├── strings/
│   ├── linked_list/
│   ├── trees/
│   ├── graphs/
│   └── dynamic_programming/
└── mock_interviews/
    ├── amazon/
    │   └── coding/
    ├── meta/
    │   └── coding/
    ├── google/
    │   └── coding/
    └── microsoft/
        └── coding/
```

---

## Problem Format

Each problem is generally organized in the following format:

```text
leetcode/
└── arrays/
    └── two_sum/
        ├── README.md
        └── solution.py
```

### File roles

- `README.md`  
  Usually prepared by the instructor.  
  Contains the problem summary, example, approach, and expected complexity discussion.

- `solution.py`  
  Implemented by the student in a feature branch.

---

## Student Workflow

Students should **not** work directly on `main`.

Expected workflow:

1. Clone the repository
2. Pull the latest `main`
3. Create a new feature branch
4. Solve the assigned problem in `solution.py`
5. Test the solution
6. Push the branch
7. Open a Pull Request
8. Wait for review and merge

---

## Example Git Workflow

### Clone the repository

```bash
git clone REPOSITORY_URL
cd tech-interview-prep
```

### Pull the latest version

```bash
git pull origin main
```

### Create a feature branch

```bash
git checkout -b feature/yourname-problem-name
```

Example:

```bash
git checkout -b feature/burak-two-sum
```

### Make your changes, then commit

```bash
git add .
git commit -m "Solve two sum problem"
```

### Push your branch

```bash
git push -u origin feature/yourname-problem-name
```

### Open a Pull Request

Open a PR from your feature branch into `main`.

---

## Branch Naming Convention

Use clean and predictable branch names.

Recommended format:

```text
feature/yourname-problem-name
```

Examples:

```text
feature/burak-two-sum
feature/ayse-valid-parentheses
feature/ali-amazon-top-k-frequent
```

---

## Benchmark Utility

This repository includes a shared benchmark tool:

```text
tools/benchmark.py
```

It can be used to observe:

- runtime
- peak memory
- peak CPU usage

Example usage:

```python
from tools.benchmark import benchmark


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    stats = benchmark(two_sum, nums, target)

    print("Result:", stats["result"])
    print(f"Runtime: {stats['runtime_ms']:.4f} ms")
    print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
    print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
```

### Important note

Benchmark results and Big-O complexity are **not the same thing**.

- **Big-O** is theoretical analysis
- **Benchmark results** are practical measurements from execution

Both are valuable, but they answer different questions.

---

## Complexity Expectations

Students are expected to think about:

- What does the problem ask?
- What is the brute-force solution?
- Is there a better approach?
- Which data structure is most suitable?
- What is the time complexity?
- What is the space complexity?

A correct solution is important, but understanding the reasoning behind the solution is just as important.

---

## Development Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

### PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

### Install development dependencies

```bash
pip install -r requirements-dev.txt
```

---

## Contribution Rules

Please follow these rules before opening a Pull Request:

- do not push directly to `main`
- always use a feature branch
- keep file names clean and consistent
- do not create unnecessary duplicate solution files
- do not push editor or environment files
- test your solution before pushing
- use clear commit messages
- open a PR after your solution is ready

---

## Files That Should Not Be Pushed

Do not push local/editor/system files such as:

- `.idea/`
- `.vscode/`
- `.venv/`
- `__pycache__/`
- `*.pyc`

These files are environment-specific and should stay local.

---

## Commit Message Examples

### Good examples

```text
Solve two sum problem
Add benchmark utility
Update two sum README
Fix bug in valid parentheses solution
```

### Bad examples

```text
final
update
new code
last version
123
```

---

## Pull Request Title Examples

Recommended format:

```text
[LeetCode][Topic] Problem Name
[Mock Interview][Company] Problem Name
```

Examples:

```text
[LeetCode][Arrays] Solve Two Sum
[LeetCode][Strings] Solve Valid Anagram
[Mock Interview][Amazon] Solve Top K Frequent Elements
```

---

## Pull Request Description Example

```md
## Summary
Solved the problem using a hash map approach.

## Details
- Added working solution in `solution.py`
- Used shared benchmark utility
- Verified output with sample input

## Complexity
- Time: O(n)
- Space: O(n)
```

---

## Current Topics

The repository currently includes or is planned to include practice in areas such as:

- arrays
- strings
- linked lists
- trees
- graphs
- dynamic programming

This structure may grow over time as the training scope expands.

---

## Detailed Student Guide

For the complete student workflow, rules, and expectations, see:

[GUIDE.md](./GUIDE.md)

---

## Instructor Note

In this repository, the instructor usually prepares:

- repository structure
- problem folders
- problem descriptions in `README.md`
- workflow rules
- review process

Students mainly focus on:

- implementing solutions in `solution.py`
- testing their code
- committing clean changes
- opening Pull Requests

---

## Goal

This repository is not only for solving coding problems.

It is also designed to help students build professional software development habits, including:

- structured thinking
- clean implementation
- readable code
- correct Git workflow
- disciplined collaboration
- review-driven development

---

## Status

This repository is actively used as a guided interview preparation workspace.