#User function Template for python3


from typing import List


class Solution:
    def maxCoins(self, N: int, arr: List[int]) -> int:
        arr = [1] + arr + [1]  # add dummy balloons at the ends
        dp = [[0] * (N + 2) for _ in range(N + 2)]  # initialize dp matrix
        
        for len in range(1, N + 1):  # iterate over diagonals
            for i in range(1, N - len + 2):
                j = i + len - 1
                for k in range(i, j + 1):
                    coins = dp[i][k-1] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j+1]
                    dp[i][j] = max(dp[i][j], coins)
                    
        return dp[1][N]

        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(Solution().maxCoins(n, a))
# } Driver Code Ends