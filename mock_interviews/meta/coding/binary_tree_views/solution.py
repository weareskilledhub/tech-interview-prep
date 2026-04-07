from collections import deque
from tools.benchmark import benchmark


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_views(root):
    """
    Return the left view and right view of a binary tree.

    Args:
        root (TreeNode | None): Root of the binary tree.

    Returns:
        dict: {
            "left_view": list[int],
            "right_view": list[int]
        }
    """
    raise NotImplementedError("Student should implement this solution.")


def build_sample_tree_1():
    """
            1
          /   \
         2     3
          \     \
           5     4
    """
    return TreeNode(
        1,
        left=TreeNode(2, right=TreeNode(5)),
        right=TreeNode(3, right=TreeNode(4)),
    )


def build_sample_tree_2():
    """
            10
           /
          6
         /
        3
    """
    return TreeNode(10, left=TreeNode(6, left=TreeNode(3)))


def build_sample_tree_3():
    """
        None
    """
    return None


def build_sample_tree_4():
    """
        7
         \
          8
           \
            9
    """
    return TreeNode(7, right=TreeNode(8, right=TreeNode(9)))


if __name__ == "__main__":
    test_cases = [
        {
            "root": build_sample_tree_1(),
            "expected": {
                "left_view": [1, 2, 5],
                "right_view": [1, 3, 4],
            },
        },
        {
            "root": build_sample_tree_2(),
            "expected": {
                "left_view": [10, 6, 3],
                "right_view": [10, 6, 3],
            },
        },
        {
            "root": build_sample_tree_3(),
            "expected": {
                "left_view": [],
                "right_view": [],
            },
        },
        {
            "root": build_sample_tree_4(),
            "expected": {
                "left_view": [7, 8, 9],
                "right_view": [7, 8, 9],
            },
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        root = case["root"]
        expected = case["expected"]

        try:
            stats = benchmark(binary_tree_views, root)
            result = stats["result"]

            passed = result == expected

            print(f"Test Case {i}")
            print(f"Expected: {expected}")
            print(f"Result: {result}")
            print(f"Pass: {passed}")
            print(f"Runtime: {stats['runtime_ms']:.4f} ms")
            print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
            print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
            print("-" * 50)

        except NotImplementedError as e:
            print(f"Test Case {i}")
            print("Solution is not implemented yet.")
            print(f"Details: {e}")
            print("-" * 50)
            break