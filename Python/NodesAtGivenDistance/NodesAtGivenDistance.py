#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:

    def KDistanceNodes(self, root, target, k):
        # code here
        # return the sorted list all nodes at k distance from target

        parent_map = {}
        target_node = None

        def dfs(root, p):
            if root is None:
                return None
            if root.data == target:
                nonlocal target_node
                target_node = root

            parent_map[root.data] = p
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)
        ans = []

        def get_k(root, visited, dist):
            if root is None:
                return
            if root in visited:
                return
            if dist == k:
                ans.append(root.data)
                return
            visited.add(root)
            get_k(parent_map[root.data], visited, dist + 1)
            get_k(root.left, visited, dist + 1)
            get_k(root.right, visited, dist + 1)
            visited.discard(root)

        get_k(target_node, set(), 0)
        ans.sort()
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends