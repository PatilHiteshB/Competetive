#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def __init__(self):
        self.uppersum = self.mini = 0
        
    def f(self, root, target):
        
        if root == None: return None
        
        if root.data == target: return root
        
        self.uppersum += root.data
        
        if root.data > target: return self.f(root.left, target)
        if root.data < target: return self.f(root.right, target)
        
        return None
        
    def miniSum(self, root, lowersum):
        
        if root == None: return
    
        if root.left == None and root.right == None:
            lowersum += root.data
            self.mini = min(self.mini, lowersum)
            
        lowersum += root.data
        
        self.miniSum(root.left, lowersum)
        self.miniSum(root.right, lowersum)
        
        
    def maxDifferenceBST(self,root, target):
        #code here
        self.uppersum = 0
        targetRoot = self.f(root, target)
        
        if targetRoot == None: return -1
        
        self.mini = float('inf')
        self.miniSum(targetRoot, 0)
        
        self.mini -= target 
        return self.uppersum - self.mini


#{ 
 # Driver Code Starts
#Initial Template for Python 3
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node

    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end= " ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)
    
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        #tree.traverseInorder(root)
        target = int(input())
        
        res = Solution().maxDifferenceBST(root, target)
        print(res)

# } Driver Code Ends