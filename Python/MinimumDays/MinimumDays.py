from typing import List


class Solution:
    def validate(self, arr, N):
        
        for i in range(1, N):
            
            if arr[i] != '?' and arr[i] == arr[i-1]:
                return False
        
        return True
        
    def getMinimumDays(self, N : int, S : str, P : List[int]) -> int:
        # code here
        arr = list(S)
        
        
        for i in range(N):
            
            if self.validate(arr, N):
                return i
            
            arr[P[i]] = '?'
                
            
        return N
            
            
        




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
        
        
        S = (input())
        
        
        P=IntArray().Input(N)
        
        obj = Solution()
        res = obj.getMinimumDays(N, S, P)
        
        print(res)
        

# } Driver Code Ends