

from typing import List
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, arr : List[int]) -> bool:
        # code here
        
        count = 0
        
        for i in range(m):
            
            if arr[i] == 1:
                
                if i-1 >= 0:
                    arr[i-1] = 2
                if i+1 < m and arr[i+1] == 0:
                    arr[i+1] = 2
                    
                    
        for i in range(m):
            
            if arr[i] == 0:
                
                count += 1
                
                if i-1 >= 0:
                    arr[i-1] = 2
                if i+1 < m:
                    arr[i+1] = 2
                    
        return count >= n
                    
        



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
        
        
        m = int(input())
        
        
        seats=IntArray().Input(m)
        
        obj = Solution()
        res = obj.is_possible_to_get_seats(n, m, seats)
        
        result_val = "Yes" if res else "No"
        print(result_val)

# } Driver Code Ends