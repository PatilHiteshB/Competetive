#User function Template for python3

#User function Template for python3

class Solution: 
    def minLaptops(self, N, start, end):
        # Code here
        start.sort()
        end.sort()
        
        i, j = 0, 0
        
        ans = 0
        while i<N and j<N:
            
            if start[i] < end[j]:
                ans += 1
            else:
                j += 1
            
            i += 1
            
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))
            
        ob = Solution()
        print(ob.minLaptops(N, start, end))
        
        T -= 1

# } Driver Code Ends