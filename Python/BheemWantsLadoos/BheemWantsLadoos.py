'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    
    def findTarget(self, root, home):
        
        qu = [root]
        
        while qu:
            
            curr = qu.pop(0)
            if curr.data == home: return curr
            if curr.left != None:
                qu.append(curr.left)
            if curr.right != None:
                qu.append(curr.right)
        
        return None
            
    
    def markParent(self, root, mp):
        
        qu = [root]
        
        while qu:
            curr = qu.pop(0)
            
            if curr.left != None:
                mp[curr.left] = curr
                qu.append(curr.left)
            
            if curr.right != None:
                mp[curr.right] = curr
                qu.append(curr.right)
                
                
            
    def ladoos(self, root, home, k):
        # Your code goes here
        
        ans = 0
        parent = {}
        target = self.findTarget(root, home)
        self.markParent(root, parent)
        
        vis = {target:True}
        qu = [target]
        level = 0
        
        while len(qu) > 0:
            
            n = len(qu)
            if level > k: break
            else: level += 1 
            
            for i in range(n):
                curr = qu.pop(0)
                ans += curr.data 
                
                if curr.left != None and curr.left not in vis: 
                    qu.append(curr.left)
                    vis[curr.left] = True
                    
                if curr.right != None and curr.right not in vis: 
                    qu.append(curr.right)
                    vis[curr.right] = True
                    
                if curr in parent and parent[curr] not in vis: 
                    qu.append(parent[curr])
                    vis[parent[curr]] = True 
                    
        return ans 




#{ 
 # Driver Code Starts
#driver code:
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input()
        root=buildTree(line)
        line=input().strip().split()
        home=int(line[0])
        k=int(line[1])
        obj = Solution();
        print(obj.ladoos(root,home,k))


# } Driver Code Ends