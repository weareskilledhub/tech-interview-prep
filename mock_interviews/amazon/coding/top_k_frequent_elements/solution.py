from tools.benchmark import benchmark


def top_k_frequent(nums, k):
    """
    Return the k most frequent elements.

    Args:
        nums (list[int]): List of integers.
        k (int): Number of most frequent elements to return.

    Returns:
        list[int]: The k most frequent elements.
    """
    raise NotImplementedError("Student should implement this solution.")


if __name__ == "__main__":
    test_cases = [
        {
            "nums": [1, 1, 1, 2, 2, 3],
            "k": 2,
            "expected": [1, 2],
        },
        {
            "nums": [1],
            "k": 1,
            "expected": [1],
        },
        {
            "nums": [4, 4, 4, 5, 5, 6, 6, 6, 6],
            "k": 2,
            "expected": [6, 4],
        },
        {
            "nums": [1, 2, 3, 4],
            "k": 1,
            "expected_options": [[1], [2], [3], [4]],
        },
        {
            "nums": [5, 5, 5, 5],
            "k": 1,
            "expected": [5],
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        nums = case["nums"]
        k = case["k"]

        try:
            stats = benchmark(top_k_frequent, nums, k)
            result = stats["result"]

            if "expected" in case:
                passed = sorted(result) == sorted(case["expected"])
                expected_display = case["expected"]
            else:
                passed = any(sorted(result) == sorted(option) for option in case["expected_options"])
                expected_display = case["expected_options"]

            print(f"Test Case {i}")
            print(f"Input: nums = {nums}, k = {k}")
            print(f"Expected: {expected_display}")
            print(f"Result: {result}")
            print(f"Pass: {passed}")
            print(f"Runtime: {stats['runtime_ms']:.4f} ms")
            print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
            print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
            print("-" * 50)

        except NotImplementedError as e:
            print(f"Test Case {i}")
            print(f"Input: nums = {nums}, k = {k}")
            print("Solution is not implemented yet.")
            print(f"Details: {e}")
            print("-" * 50)
            break