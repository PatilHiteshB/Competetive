#User function Template for python3

class Solution:
    def Solve(self, N, piles, H):
        # Code here
        low, high = 1, max(piles)+1
        
        while low<high:
            
            mid = (low+high)//2
            count = 0
            
            for p in piles:
                count += (p+mid-1)//mid
            if count > H:
                low = mid+1
            else:
                high = mid
                
        return low


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        piles = list(map(int, input().split()))
        H = int(input())
        ob = Solution()
        print(ob.Solve(N, piles, H))
# } Driver Code Ends