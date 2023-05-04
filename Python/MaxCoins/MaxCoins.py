from typing import List


class Solution:
    def maxCoins(self, n: int, ranges: List[List[int]]) -> int:
        ranges.sort()
        mx = [0] * (n+1)

        cnt = -1
        mx[n] = 0
        for i in range(n-1, -1, -1):
            cnt = max(cnt, ranges[i][2])
            mx[i] = cnt

        ans = -1
        for i in range(n):
            sec = ranges[i][1]
            l, h = i + 1, n - 1
            while (l <= h):
                m = l + (h - l) // 2
                if ranges[m][0] < sec:
                    l = m + 1
                else:
                    h = m - 1
            ans = max(ans, ranges[i][2] + mx[l])

        return ans



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        ranges=IntMatrix().Input(n, 3)
        
        obj = Solution()
        res = obj.maxCoins(n, ranges)
        
        print(res)
        

# } Driver Code Ends