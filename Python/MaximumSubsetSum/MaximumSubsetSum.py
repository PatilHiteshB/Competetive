from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, arr : List[int]) -> int:
        # code here
        prev_taken = arr[0]
        prev_not_taken = 0
        
        for i in range(1, N):
            
            curr_taken = arr[i] + max(prev_taken, prev_not_taken)
            curr_not_taken = prev_taken
            
            prev_taken = curr_taken
            prev_not_taken = curr_not_taken
            
            
        return max(prev_taken, prev_not_taken)



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.findMaxSubsetSum(N, A)
        
        print(res)
        

# } Driver Code Ends