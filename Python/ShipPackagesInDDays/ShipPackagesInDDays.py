#User function Template for python3

class Solution:
    
    def solve(self, arr, capacity, D):
            
        count = 1
        su = 0
        
        for i in arr:
            if su + i <= capacity:
                su += i
            else:
                count += 1
                if count > D or i > capacity:
                    return False
                su = i
        return True
            

    def leastWeightCapacity(self, arr, N, D):
        # code here 
        start, end = 1, sum(arr)
        ans = sum(arr)
        
        while start <= end:
            
            mid = (start+end)//2
            
            if self.solve(arr, mid, D):
                ans = mid
                end = mid-1
            else:
                start = mid+1
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
# } Driver Code Ends