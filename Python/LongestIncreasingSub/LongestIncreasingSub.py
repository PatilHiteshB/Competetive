#User function Template for python3

from bisect import bisect_left

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        res = []
        l = 1  #length of subsequence
        
        res.append(a[0])
        
        for i in range(n):
            if(a[i] > res[len(res)-1]):
                res.append(a[i])
                l += 1
            else:
                low = bisect_left(res,a[i])
                res[low] = a[i]
        return(l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends