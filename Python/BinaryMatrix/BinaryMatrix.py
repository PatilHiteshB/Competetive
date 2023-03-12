#User function Template for python3

class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        ans = count = 0
        j = N-1
        
        for i in range(N):
            
            while j>=0 and mat[i][j] == 1:
                j += -1
                
            if N-j-1 > count:
                ans = i
                count = N-j-1
                
        return (ans, count)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob=Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end =" ")
        print()
# } Driver Code Ends