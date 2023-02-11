from typing import List


class Solution:
    
    def getMinimumDays(self, N : int, S : str, P : List[int]) -> int:
        # code here
        arr = list(S)
        dups = 0
        for i in range(1, N):
            if arr[i] == arr[i-1]:
                dups += 1
                
        i = count = 0
        while dups > 0:
            
            if (P[i]-1 >= 0 and P[i]+1 < N) and (arr[P[i]] == arr[P[i]-1] and arr[P[i]] == arr[P[i]+1]):
                dups += -2
                
            elif (P[i]-1 >= 0 and arr[P[i]] == arr[P[i]-1]) or (P[i]+1 < N and arr[P[i]] == arr[P[i]+1]):
                dups += -1
        
            arr[P[i]] = '?'
            i += 1
            count += 1
                
            # print(dups)
                    
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
        
        
        S = (input())
        
        
        P=IntArray().Input(N)
        
        obj = Solution()
        res = obj.getMinimumDays(N, S, P)
        
        print(res)
        

# } Driver Code Ends