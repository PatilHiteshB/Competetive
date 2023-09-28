from typing import List


class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        
        i = 0
        while i < len(a) and i+1 < len(a):
            
            a[i], a[i+1] = a[i+1], a[i]
            i += 2
            



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
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        obj.convertToWave(n, a)
        IntArray().Print(a)

# } Driver Code Ends