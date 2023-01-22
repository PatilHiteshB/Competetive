

from typing import List
class Solution:
            
            
    def solve(self, N : int, K : int, arr : List[int]) -> int:
        # code here
        
        for i in range(1, N):
            arr[i] += arr[i-1]
            
        su = arr[-1]
        
        fact, i = [], 1
        while i*i <= su:
            
            if su%i == 0:
            
                fact.append(i)
                if i != su//i:
                    fact.append(su//i)
                
            i += 1
                
        fact.sort(reverse=True)
        answer = 1
        
        for i in fact:
            count = 0
            for k in arr:
                if k%i == 0:
                    count += 1
            if count >= K:
                answer = i
                break
        
        return answer
            
        



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
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, K, arr)
        
        print(res)
        

# } Driver Code Ends