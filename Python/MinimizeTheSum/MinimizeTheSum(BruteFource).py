#User function Template for python3


class Solution:
    
    def insertElement(self, arr, N, x):
        
        low, high = 0, N-1
        
        while low < high:
            
            mid = (low+high)//2
            
            if arr[mid] > x:
                
                high = mid-1
                
            else:
                
                low = mid+1
                
        if arr[low] > x:  
            
            return arr[:low] + [x] + arr[low:]
            
        return arr[:low+1] + [x] + arr[low+1:]
                
                
        
    def minimizeSum(self, N, arr):
        # Code here
        arr.sort()
        su = 0
        

        while len(arr) > 1:
            
            arr = self.insertElement(arr, len(arr), arr[0]+arr[1])
            
            su += arr.pop(0) + arr.pop(0)
            
        return su


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends