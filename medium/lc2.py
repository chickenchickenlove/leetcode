'''
- 비어있지 않은 LinkedList. 2개의 양의 정수임.
- reverse order로 자리수가 표현되어있고, 각각 노드가 single dist임
- linked list의 합을 구해라.

- 2개의 숫자들은 그 자체가 0인 경우를 제외하고는 0이 없다.


1. 자리수가 큰 녀석을 기준으로 0을 더 채워주자. 그리고 뒤집어주자.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
def get_list(list_node: Optional[ListNode]) -> list[int]:
    ret = []
    while list_node is not None:
        ret.append(list_node.val)
        list_node = list_node.next
    return ret



def update(list1, list2):
    diff = abs(len(list1) - len(list2))
    if len(list1) > len(list2):
        for _ in range(diff):
            list2.append(0)
    if len(list1) < len(list2):
        for _ in range(diff):
            list1.append(0)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1, list2 = get_list(l1), get_list(l2)
        update(list1, list2)

        result = [0]

        for n1, n2 in zip(list1, list2):
            mid_sum = n1 + n2 + result.pop()
            if mid_sum >= 10:
                result.append(mid_sum-10)
                result.append(1)
            else:
                result.append(mid_sum)
                result.append(0)

        if result[-1] == 0:
            result.pop()

        output_node = ListNode()
        tail = output_node

        for index, v in enumerate(result):
            tail.val = v

            if index == len(result)-1:
                break

            tail.next = ListNode()
            tail = tail.next

        return output_node