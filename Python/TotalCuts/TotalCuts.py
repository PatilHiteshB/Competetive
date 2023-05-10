from typing import List


class Solution:
    def totalCuts(self, N : int, K : int, arr : List[int]) -> int:
        # code here
        left = [0]*N
        right = [0]*N
        
        
        ma = arr[0]
        for i in range(N):
            ma = max(ma, arr[i])
            left[i] = ma
                
        ma = arr[N-1]
        for i in range(N-1, -1, -1):
            ma = min(ma, arr[i])
            right[i] = ma
                
        count = 0
        for i in range(1, N):
            if left[i-1] + right[i] >= K:
                count += 1
                
        return count


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
        
        
        K = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.totalCuts(N,K,A)
        
        print(res)
        

# } Driver Code Ends