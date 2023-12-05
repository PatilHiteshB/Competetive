#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans = arr[n-1] - arr[0]
        small = arr[0] + k
        large = arr[n-1] - k
        for i in range(n-1):
            small1 = min(small, arr[i+1] - k) 
            large1 = max(large, arr[i] + k)   
            if small < 0:
                continue
            ans = min(ans, large1 - small1)
        return ans
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends