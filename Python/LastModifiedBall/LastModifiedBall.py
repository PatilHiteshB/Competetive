#User function Template for python3

class Solution():
    def solve(self, N, arr):
        #your code here
        for i in range(N):
            if arr[N-i-1] == 9:
                continue
            return N-i
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    array=[int(i) for i in input().split()]
    obj = Solution()
    print(obj.solve(n, array))
# } Driver Code Ends