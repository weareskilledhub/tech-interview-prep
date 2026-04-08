from tools.benchmark import benchmark


def length_of_longest_substring(s):
    """
    Return the length of the longest substring without repeating characters.

    Args:
        s (str): Input string.

    Returns:
        int: Length of the longest valid substring.
    """
    left = 0
    max_len = 0
    last_index = {}

    for right, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= left:
            left = last_index[ch] + 1

        last_index[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    test_cases = [
        {
            "s": "abcabcbb",
            "expected": 3,
        },
        {
            "s": "bbbbb",
            "expected": 1,
        },
        {
            "s": "pwwkew",
            "expected": 3,
        },
        {
            "s": "",
            "expected": 0,
        },
        {
            "s": "dvdf",
            "expected": 3,
        },
        {
            "s": "abba",
            "expected": 2,
        },
        {
            "s": " ",
            "expected": 1,
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        s = case["s"]
        expected = case["expected"]

        stats = benchmark(length_of_longest_substring, s)
        result = stats["result"]

        passed = result == expected

        print(f"Test Case {i}")
        print(f"Input: s = {repr(s)}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {passed}")
        print(f"Runtime: {stats['runtime_ms']:.4f} ms")
        print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
        print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
        print("-" * 50)