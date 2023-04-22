from typing import List


class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        # code here
        xrr = sorted(arr)
        mp = {}
        
        mp[xrr[0]] = 0
        su = xrr[0]
        
        i = 1
        while i < n:
            if xrr[i-1] < xrr[i]:
                mp[xrr[i]] = su
            su += xrr[i]
            i += 1    
        # print(mp)    
        for i in range(n):
            arr[i] = mp[arr[i]]
            
        return arr
        
        



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
        res = obj.smallerSum(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends