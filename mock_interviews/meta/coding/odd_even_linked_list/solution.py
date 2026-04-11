from tools.benchmark import benchmark


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def odd_even_linked_list(head):
    """
    Group nodes by odd indices first, then even indices.

    The grouping is based on node position, not node value.

    Args:
        head (ListNode | None): Head of the singly linked list.

    Returns:
        ListNode | None: Head of the reordered linked list.
    """
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head



def build_linked_list(values):
    """Build a linked list from a Python list."""
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next



def linked_list_to_list(head):
    """Convert a linked list back into a Python list."""
    values = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next

    return values



def build_sample_list_1():
    """
    1 -> 2 -> 3 -> 4 -> 5
    """
    return build_linked_list([1, 2, 3, 4, 5])



def build_sample_list_2():
    """
    2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
    """
    return build_linked_list([2, 1, 3, 5, 6, 4, 7])



def build_sample_list_3():
    """
    None
    """
    return None



def build_sample_list_4():
    """
    1
    """
    return build_linked_list([1])



def build_sample_list_5():
    """
    1 -> 2
    """
    return build_linked_list([1, 2])



def build_sample_list_6():
    """
    1 -> 2 -> 3 -> 4
    """
    return build_linked_list([1, 2, 3, 4])


if __name__ == "__main__":
    test_cases = [
        {
            "head": build_sample_list_1(),
            "expected": [1, 3, 5, 2, 4],
        },
        {
            "head": build_sample_list_2(),
            "expected": [2, 3, 6, 7, 1, 5, 4],
        },
        {
            "head": build_sample_list_3(),
            "expected": [],
        },
        {
            "head": build_sample_list_4(),
            "expected": [1],
        },
        {
            "head": build_sample_list_5(),
            "expected": [1, 2],
        },
        {
            "head": build_sample_list_6(),
            "expected": [1, 3, 2, 4],
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        head = case["head"]
        expected = case["expected"]

        stats = benchmark(odd_even_linked_list, head)
        result_head = stats["result"]
        result = linked_list_to_list(result_head)

        passed = result == expected

        print(f"Test Case {i}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {passed}")
        print(f"Runtime: {stats['runtime_ms']:.4f} ms")
        print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
        print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
        print("-" * 50)
