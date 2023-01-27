#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from queue import PriorityQueue

class Solution:
    def leastInterval(self, N, K, arr):
        # Code here
        mp = {i:0 for i in arr}
        for i in arr:
            mp[i] += 1
            
        ma = max(list(mp.values()))
        answer = (ma-1)*(K+1)
        
        for i in mp.keys():
            if mp[i] == ma:
                answer += 1
            
        return max(len(arr), answer)
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        tasks = input().split()
        ob = Solution()
        res = ob.leastInterval(N, K, tasks)
        print(res)
# } Driver Code Ends