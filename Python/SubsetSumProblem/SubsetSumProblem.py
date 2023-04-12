#User function Template for python3

class Solution:
    
    def solve(self, arr, ind, sum):
        if ind < 0:
            return sum == 0
            
        return self.solve(arr, ind-1, sum-arr[ind]) or self.solve(arr, ind-1, sum)
        
    def isSubsetSum (self, N, arr, sum):
        # code here 
        return self.solve(arr, N-1, sum)
        
        


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