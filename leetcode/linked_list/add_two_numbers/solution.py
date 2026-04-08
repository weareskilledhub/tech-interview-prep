from tools.benchmark import benchmark


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    """
    Add two numbers represented by linked lists in reverse order.

    Args:
        l1 (ListNode | None): First linked list.
        l2 (ListNode | None): Second linked list.

    Returns:
        ListNode | None: Head of the resulting linked list.
    """
    raise NotImplementedError("Student should implement this solution.")


def build_linked_list(values):
    """Build a linked list from a Python list."""
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    """Convert a linked list back to a Python list."""
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


if __name__ == "__main__":
    test_cases = [
        {
            "l1": [2, 4, 3],
            "l2": [5, 6, 4],
            "expected": [7, 0, 8],
        },
        {
            "l1": [0],
            "l2": [0],
            "expected": [0],
        },
        {
            "l1": [9, 9, 9, 9, 9, 9, 9],
            "l2": [9, 9, 9, 9],
            "expected": [8, 9, 9, 9, 0, 0, 0, 1],
        },
        {
            "l1": [5],
            "l2": [5],
            "expected": [0, 1],
        },
        {
            "l1": [1, 8],
            "l2": [0],
            "expected": [1, 8],
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        l1 = build_linked_list(case["l1"])
        l2 = build_linked_list(case["l2"])
        expected = case["expected"]

        try:
            stats = benchmark(add_two_numbers, l1, l2)
            result_list = linked_list_to_list(stats["result"])

            passed = result_list == expected

            print(f"Test Case {i}")
            print(f"Input: l1 = {case['l1']}, l2 = {case['l2']}")
            print(f"Expected: {expected}")
            print(f"Result: {result_list}")
            print(f"Pass: {passed}")
            print(f"Runtime: {stats['runtime_ms']:.4f} ms")
            print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
            print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
            print("-" * 50)

        except NotImplementedError as e:
            print(f"Test Case {i}")
            print(f"Input: l1 = {case['l1']}, l2 = {case['l2']}")
            print("Solution is not implemented yet.")
            print(f"Details: {e}")
            print("-" * 50)
            break