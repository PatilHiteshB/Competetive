class Solution:
    def maxInstance(self, s : str) -> int:
        # code here
        
        mps = {}
        for i in s:
            if i in mps:
                mps[i] += 1
            else:
                mps[i] = 1
        
        mpb = {}        
        for i in "balloon":
            if i in mpb:
                mpb[i] += 1
            else:
                mpb[i] = 1
                
        ans = len(s)
        for i in mpb:
            if i not in mps:
                return 0
            else:
                ans = min(ans, mps[i]//mpb[i])
            
        return ans


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.maxInstance(s)
        
        print(res)

# } Driver Code Ends