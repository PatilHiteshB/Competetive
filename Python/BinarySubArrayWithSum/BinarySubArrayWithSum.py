#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def numberOfSubarrays(self, arr, N, target):
        # Code here
        
        m = {}
        su = count = 0
        
        for i in range(N):
            
            su += arr[i]
            if su == target:
                count += 1
                
            if su - target in m.keys():
                count += m[su-target]
            
            if su not in m.keys():
                m[su] = 1
            else:
                m[su] += 1
            
        
        return count
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, target = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.numberOfSubarrays(arr, N, target)
        print(res)
# } Driver Code Ends