#User function Template for python3

class Solution:

    def findMinDiff(self, arr, N, M):
        # code here
        arr = sorted(arr)
        ans = float('inf')
        for i in range(N):
            if i+M > len(arr):
                break
            # print("{} {}".format(arr[i:i+M], arr[i+M-1]-arr[i]))
            ans = min(ans, arr[i+M-1]-arr[i])
            
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends