#User function Template for python3

class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        MAX = max(arr)
        factor = [False for _ in range(MAX+1)]
        
        mp = {}
        for i in range(N):
            
            if arr[i] in mp:
                mp[arr[i]] += 1
                continue
                
            for j in range(2*arr[i], MAX+1, arr[i]):
                factor[j] = True
                
            mp[arr[i]] = 1
        # print(mp)    
        
        ans = 0
        for i in arr:
            if factor[i] or mp[i] > 1:
                ans += 1
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))
        
        T -= 1
# } Driver Code Ends