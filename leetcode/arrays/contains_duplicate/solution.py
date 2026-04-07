from tools.benchmark import benchmark


def contains_duplicate(nums):
    """
    Return True if any value appears at least twice in the array.
    Return False if every element is distinct.

    Args:
        nums (list[int]): List of integers.

    Returns:
        bool: True if a duplicate exists, otherwise False.
    """
    return len(nums) > len(set(nums)) # Listenin boyu, kümenin boyundan büyükse demek ki bir şeyler silinmiş!
    raise NotImplementedError("Student should implement this solution.")




if __name__ == "__main__":
    test_cases = [
        {
            "nums": [1, 2, 3, 1],
            "expected": True,
        },
        {
            "nums": [1, 2, 3, 4],
            "expected": False,
        },
        {
            "nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            "expected": True,
        },
        {
            "nums": [5],
            "expected": False,
        },
        {
            "nums": [0, 0],
            "expected": True,
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        nums = case["nums"]
        expected = case["expected"]

        try:
            stats = benchmark(contains_duplicate, nums)
            result = stats["result"]

            passed = result == expected

            print(f"Test Case {i}")
            print(f"Input: nums = {nums}")
            print(f"Expected: {expected}")
            print(f"Result: {result}")
            print(f"Pass: {passed}")
            print(f"Runtime: {stats['runtime_ms']:.4f} ms")
            print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
            print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
            print("-" * 50)

        except NotImplementedError as e:
            print(f"Test Case {i}")
            print(f"Input: nums = {nums}")
            print("Solution is not implemented yet.")
            print(f"Details: {e}")
            print("-" * 50)
            break