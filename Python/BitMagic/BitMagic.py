from typing import List


class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        # code here
        start, end = 0, n-1
        
        count = 0
        while start < end:
            
            if arr[start] != arr[end]:
                count += 1
                
            start += 1
            end += -1
            
        return count%2 + count//2
        



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
        res = obj.bitMagic(n, arr)
        
        print(res)
        

# } Driver Code Ends