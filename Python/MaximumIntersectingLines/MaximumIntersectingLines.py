#User function Template for python3

class Solution: 
    def maxIntersections(self, lines, N):
        # Code here
        
        mp = {}
        
        for i in lines:
            
            start = i[0]
            end = i[1]+1
            
            if start in mp: mp[start] += 1
            else: mp[start] = 1
            
            if end in mp: mp[end] -= 1
            else: mp[end] = -1
            
        ans = 0
        su = 0
        
        for entry in sorted(mp.keys()):
            
            su += mp[entry]
            ans = max(ans, su)
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        lines=[[] for j in range(N)]
        for j in range(2):
            prr = [int(i) for i in input().split()] 
            for i in range(N): 
                lines[i].append(prr[i])
            
    
        ob = Solution()
        print(ob.maxIntersections(lines, N))
        
        T -= 1

# } Driver Code Ends