#User function Template for python3

from typing import List
 
from collections import deque

class Solution:

    def minimumMultiplications(self, arr, start, end):

        if start == end:
            return 0

        mod = 10 ** 5

        vis = [False] * mod

        q = deque()
        q.append((0, start))

        vis[start] = True

        while q:

            level, temp = q.popleft()

            for i in range(len(arr)):

                prod = (temp * arr[i]) % mod

                if prod == end:
                    return level + 1

                if vis[prod]:
                    continue

                q.append((level + 1, prod))
                vis[prod] = True

        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends