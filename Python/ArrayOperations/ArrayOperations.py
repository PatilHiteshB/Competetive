from typing import List


class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        # code here
        count = 0
        nonZ = 0
        
        for i in arr:
            
            if i == 0:
                
                if nonZ > 0:
                    count += 1
                nonZ = 0
                
            else:
                nonZ += 1
                
                
        if nonZ == n:
            return -1
            
        elif nonZ > 0:
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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.arrayOperations(n, arr)
        
        print(res)
        

# } Driver Code Ends