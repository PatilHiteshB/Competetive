#User function Template for python3

class Solution:
    def left(self, arr):
        
        ans = [-1]*len(arr)
        stck = []
        for i in range(len(arr)):
            
            while stck and arr[stck[-1]] >= arr[i]:
                stck.pop()
                
            if stck:
                ans[i] = stck[-1]
            
            stck.append(i)
            
        return ans
        
    def right(self, arr):
        
        ans = [-1]*len(arr)
        stck = []
        for i in range(len(arr)-1, -1, -1):
            
            while stck and arr[stck[-1]] >= arr[i]:
                stck.pop()
                
            if stck:
                ans[i] = stck[-1]
            
            stck.append(i)
            
        return ans
        
    def nearestSmallestTower(self,arr):
        #code here
        left = self.left(arr)
        right = self.right(arr)
        
        ans = [-1]*len(arr)
        # print(left)
        # print(right)
        
        for i in range(len(arr)):
            
            leftdist = float('inf') if left[i] == -1 else i-left[i]
            rightdist = float('inf') if right[i] == -1 else right[i] - i                             
            
            if leftdist < rightdist or (leftdist == rightdist and left[i] != -1 and arr[left[i]] <= arr[right[i]]):
                ans[i] = left[i]
            elif leftdist > rightdist or (leftdist == rightdist and right[i] != -1 and arr[right[i]] <= arr[left[i]]):
                ans[i] = right[i]
            else:
                ans[i] = -1
                    
        return ans
        
        
        
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input().strip())):
        N=int(input())
        arr=[int(i) for i in input().strip().split()]
        obj=Solution()
        ans=obj.nearestSmallestTower(arr)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends