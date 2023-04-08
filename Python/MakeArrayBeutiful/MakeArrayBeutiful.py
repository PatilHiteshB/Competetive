#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        ans = []
        
        for i in arr:
            if ans:
                if (ans[-1] < 0 and i >= 0) or (ans[-1] >= 0 and i < 0):
                    ans.pop()
                else:
                    ans.append(i)
            else:
                ans.append(i)
                
        return ans
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        arr = list(map(int,input().split()))
        
        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends