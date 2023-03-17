#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        ans = [1 if i == 0 else 0 for i in arr]
        
        su = ans[0]
        for i in range(1, n):
            if arr[i] == 0:
                ans[i] += ans[i-1]
            su += ans[i]
            
        return su


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends