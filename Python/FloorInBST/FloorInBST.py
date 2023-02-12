#User function Template for python3

class Solution:
    
    def solve(self, root, k):
        
        if root.data == k:
            return k
            
        if root.data > k and root.left != None:
            
            return self.solve(root.left, k)
            
        if root.data < k:
            
            if root.right != None:
                
                x = self.solve(root.right, k)
                return x if x != -1 else root.data
                
            return root.data
            
        return -1
        
    def floor(self, root, x):
        # Code here
        
        if root == None:
            return -1
            
        return self.solve(root, x)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends