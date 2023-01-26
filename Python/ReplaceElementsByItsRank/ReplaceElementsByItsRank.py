#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def replaceWithRank(self, N, arr):
        # Code here
        
        mp = {}
        
        for i in range(N):
            if arr[i] not in mp.keys():
                mp[arr[i]] = 0
        
        tarr = list(mp.keys())
        tarr.sort()
        
        for i in range(len(tarr)):
            mp[tarr[i]] = i+1
            
        for i in range(N):
            arr[i] = mp[arr[i]]
            
        return arr
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.replaceWithRank(N, arr)
        for rank in res:
            print(rank, end = ' ')
        print()
# } Driver Code Ends