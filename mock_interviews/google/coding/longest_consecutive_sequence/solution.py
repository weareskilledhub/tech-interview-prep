from tools.benchmark import benchmark


def longest_consecutive(nums): # o(n) formatında olduğu için set kullanıldı. en başta list yapısın kullanıldı fakat yapı o(n**2) olduğundan set tercih edildi. örnekler küçük sayılarda olduğu için cpu ve ms değerleri birbirine çok yakın. fakat büyük listelerde maliyetin n**2 olarak artacağı anlaşıldı.
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for n in num_set:
        if n - 1 not in num_set:
            count = n
            length = 1

            while count + 1 in num_set:
                count += 1
                length += 1

                max_length = max(max_length, length)

    return max_length


if __name__ == "__main__":
    test_cases = [
        {"nums": [100, 4, 200, 1, 3, 2], "expected": 4},
        {"nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], "expected": 9},
        {"nums": [1, 0, 1, 2], "expected": 3},
        {"nums": [], "expected": 0},
        {"nums": [5], "expected": 1},
    ]

    for i, case in enumerate(test_cases, start=1):
        nums = case["nums"]
        expected = case["expected"]

        try:
            stats = benchmark(longest_consecutive, nums)
            result = stats["result"]

            print(f"Test Case {i}")
            print(f"Input: nums = {nums}")
            print(f"Expected: {expected}")
            print(f"Result: {result}")
            print(f"Pass: {result == expected}")
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