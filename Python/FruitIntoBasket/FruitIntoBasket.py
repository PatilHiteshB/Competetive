#User function Template for python3

class Solution:
    def sumSubarrayMins(self, N, arr):
        # Code here
        mp = {}
        
        start = end = answer = 0
        
        while end < N:
            
            if arr[end] in mp.keys():
                mp[arr[end]] += 1
                
            else:
                mp[arr[end]] = 1
                
                
            if len(mp) <= 2:
                
                temp = end - start + 1
                
                if temp > answer:
                    answer = temp
                    
            else:
                
                if mp[arr[start]] > 0:
                    mp[arr[start]] += -1
                    
                if mp[arr[start]] == 0:
                    mp.pop(arr[start])
                        
                start += 1
                
            
            end += 1
        
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        fruits = list(map(int, input().split()))
        ob = Solution()
        res = ob.sumSubarrayMins(N, fruits)
        print(res)
# } Driver Code Ends