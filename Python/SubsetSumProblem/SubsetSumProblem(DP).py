#User function Template for python3

#User function Template for python3

class Solution:
    
    def solve(self, arr, ind, sum, dp):
        
        if sum == 0:
            return 1
        if ind < 0 or sum < 0:
            return 0
               
        if dp[ind][sum] != -1:
            return dp[ind][sum]
        
        temp = 0    
        if arr[ind] <= sum:    
            temp = self.solve(arr, ind-1, sum-arr[ind], dp)    
        temp = max(temp, self.solve(arr, ind-1, sum, dp))
            
        dp[ind][sum] = temp
        return temp
        

        
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp = [[-1 for _ in range(sum+1)] for _ in range(N+1)]
        return self.solve(arr, N-1, sum, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends