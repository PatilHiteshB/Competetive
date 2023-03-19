from typing import List


from typing import List


class Solution:
    def getDistinctDifference(self, N : int, arr : List[int]) -> List[int]:
        # code here
        
        mpr, mpl = {}, {}
        arrR, arrL = [0]*N, [0]*N
        ans = [0]*N
        
        for i in range(0, N):
            arrR[i] = len(mpr)
            mpr[arr[i]] = 0
            
        
        for i in range(N-1, -1, -1):
            arrL[i] = len(mpl)
            mpl[arr[i]] = 0
               
            
        # print(arrL)
        # print(arrR)
        for i in range(0, N):
            ans[i] = arrR[i] - arrL[i]
            
        return ans
            
            
            
        


        



#{ 
 # Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass
    
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        A=[int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.getDistinctDifference(N, A)
        
        print(*res)
        

# } Driver Code Ends