#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
        
    def countSubsequence(self, strn):
        
        last = [-1]*127
        N = len(strn)
        dp = [0] * (N+1)
        
        dp[0] = 1
        
        for i in range(1, N+1):
            
            dp[i] = 2 * dp[i-1]
            
            if last[ord(strn[i-1])] != -1:
                
                dp[i] = dp[i] - dp[last[ord(strn[i-1])]]
            
            last[ord(strn[i-1])] = i-1
            
        return dp[N]
            
            
                
    def betterString(self, str1, str2):
        # Code here
        
        if self.countSubsequence(str1) >= self.countSubsequence(str2):
            return str1    
        return str2
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends