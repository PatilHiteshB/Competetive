#User function Template for python3

class Solution():
    def minCost(self, arr, N):
        #your code goes here
        for i in range(1, N):
            
            arr[i][0] = min(arr[i-1][1]+arr[i][0], arr[i-1][2]+arr[i][0])
            arr[i][1] = min(arr[i-1][0]+arr[i][1], arr[i-1][2]+arr[i][1])
            arr[i][2] = min(arr[i-1][0]+arr[i][2], arr[i-1][1]+arr[i][2])
            
        return min(arr[N-1][0], arr[N-1][1], arr[N-1][2])
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ =="__main__":
    for _ in range(int(input())):
        n = int(input())
        colors = []
        for i in range(n):
            tmp = [int(i) for i in input().split()]
            colors.append(tmp)
        print(Solution().minCost(colors, n))
# } Driver Code Ends