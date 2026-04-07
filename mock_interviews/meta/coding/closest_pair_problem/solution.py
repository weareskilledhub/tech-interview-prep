import math
from tools.benchmark import benchmark


def closest_pair(points):
    """
    Return the minimum Euclidean distance between any two distinct points.

    Args:
        points (list[tuple[int, int] | tuple[float, float]]):
            A list of 2D points represented as (x, y).

    Returns:
        float: Minimum Euclidean distance between any two points.
               Return 0.0 if fewer than two points are provided.
    """
    raise NotImplementedError("Student should implement this solution.")


if __name__ == "__main__":
    test_cases = [
        {
            "points": [(0, 0), (3, 4), (7, 7)],
            "expected": 5.0,
        },
        {
            "points": [(1, 1), (2, 2), (10, 10)],
            "expected": math.sqrt(2),
        },
        {
            "points": [(5, 5)],
            "expected": 0.0,
        },
        {
            "points": [],
            "expected": 0.0,
        },
        {
            "points": [(0, 0), (0, 1), (10, 10)],
            "expected": 1.0,
        },
    ]

    tolerance = 1e-4

    for i, case in enumerate(test_cases, start=1):
        points = case["points"]
        expected = case["expected"]

        try:
            stats = benchmark(closest_pair, points)
            result = stats["result"]

            passed = abs(result - expected) <= tolerance

            print(f"Test Case {i}")
            print(f"Input: points = {points}")
            print(f"Expected: {expected:.4f}")
            print(f"Result: {result:.4f}")
            print(f"Pass: {passed}")
            print(f"Runtime: {stats['runtime_ms']:.4f} ms")
            print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
            print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
            print("-" * 50)

        except NotImplementedError as e:
            print(f"Test Case {i}")
            print(f"Input: points = {points}")
            print("Solution is not implemented yet.")
            print(f"Details: {e}")
            print("-" * 50)
            break