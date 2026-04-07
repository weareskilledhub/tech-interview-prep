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