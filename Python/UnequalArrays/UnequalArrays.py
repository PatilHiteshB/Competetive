from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        if sum(A) != sum(B):
            return -1
            
        AEven, BEven = [], []
        AOdd, BOdd = [], []
        
        for i in range(N):
            
            if abs(A[i])&1 == 0:
                AEven.append(A[i])
            else:
                AOdd.append(A[i])
            
            if abs(B[i])&1 == 0:
                BEven.append(B[i])
            else:
                BOdd.append(B[i])
                
        if len(AEven) != len(BEven):
            return -1
            
        AEven.sort()
        BEven.sort()
        AOdd.sort()
        BOdd.sort()
        
        ans = 0
        for i in range(len(AEven)):
            ans += abs(AEven[i]-BEven[i])
        for i in range(len(AOdd)):
            ans += abs(AOdd[i]-BOdd[i])
            
        return ans//4
            
        
        



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
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, A, B)
        
        print(res)
        

# } Driver Code Ends