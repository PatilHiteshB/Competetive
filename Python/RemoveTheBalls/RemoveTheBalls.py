from typing import List


class Solution:
    
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        
        balls = [[-1, -1]]
        res = 0
        
        for i in range(N):
            if color[i] == balls[-1][0] and radius[i] == balls[-1][1]:
               res -= 1
               balls.pop()
               
            else:
               res += 1 
               balls.append([color[i], radius[i]])
        

        return res
        



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
        
        
        color=IntArray().Input(N)
        
        
        radius=IntArray().Input(N)
        
        obj = Solution()
        res = obj.finLength(N, color, radius)
        
        print(res)
        

# } Driver Code Ends