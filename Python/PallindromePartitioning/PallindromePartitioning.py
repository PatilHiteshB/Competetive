#User function Template for python3

class Solution:
    def is_palindrome(self,s,i,j):
        while i<j:
            if s[i-1]!=s[j-1]:
                return False
            i+=1
            j-=1
        return True
    
    def pp(self,s,n):
        dp=[None]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            dp[i]=float("inf")
            for j in range(i,0,-1):
                if self.is_palindrome(s,j,i):
                    dp[i]=min(dp[i],1+dp[j-1])
        return dp[n]
        
        # recursive approach
        # if n==0:
        #     return 0
        # res=float("inf")
        # for i in range(n,0,-1):
        #     if self.is_palindrome(s,i,n):
        #         res=min(res,1+self.pp(s,i-1))
        # return res
    
    def palindromicPartition(self, string):
        return self.pp(string,len(string))-1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends