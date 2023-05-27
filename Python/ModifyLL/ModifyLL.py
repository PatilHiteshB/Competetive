#User function Template for python3

class Solution:

    def modify_the_list(self, head):
        v = []
        while head:
            v.append(head.data)
            head = head.next

        left = 0
        right = len(v) - 1
        while left < right:
            temp = v[left]
            v[left] = v[right] - v[left]
            v[right] = temp
            left += 1
            right -= 1

        l1 = Node(v[0])
        ans = l1
        for i in range(1, len(v)):
            next_node = Node(v[i])
            l1.next = next_node
            l1 = l1.next

        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def modify_the_list(head):
    current = head
    while current is not None:
        if current.next is not None and current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


t = int(input())
while t > 0:
    n = int(input())
    linked_list_arr = list(map(int, input().split()))
    head = None
    temp = None
    for a in linked_list_arr:
        new_node = Node(a)
        if head is None:
            head = new_node
        else:
            temp.next = new_node
        temp = new_node
    head = Solution().modify_the_list(head)
    print_list(head)
    t -= 1
# } Driver Code Ends