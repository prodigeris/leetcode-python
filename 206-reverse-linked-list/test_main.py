import unittest
from main import Solution, ListNode


def list_to_listnode(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head


def listnode_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_reverse_multiple_elements(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        result = self.solution.reverseList(head)
        self.assertEqual([5, 4, 3, 2, 1], listnode_to_list(result))

    def test_reverse_single_element(self):
        head = list_to_listnode([1])
        result = self.solution.reverseList(head)
        self.assertEqual([1], listnode_to_list(result))

    def test_reverse_empty_list(self):
        result = self.solution.reverseList(None)
        self.assertEqual([], listnode_to_list(result))


if __name__ == '__main__':
    unittest.main()
