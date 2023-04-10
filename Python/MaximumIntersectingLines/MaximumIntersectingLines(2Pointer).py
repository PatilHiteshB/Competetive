#User function Template for python3

class Solution: 
    def maxIntersections(self, lines, N):
        # Code here
        
        start = sorted([i[0] for i in lines])
        end = sorted([i[1] for i in lines])
        
        i, j = 0, 0
        ans, count = 0, 0
        
        while i < N and j < N:
            
            if start[i] <= end[j] :
                
                count += 1
                ans = max(ans, count)
                i += 1
                
            else:
                
                count -= 1
                j += 1
        
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