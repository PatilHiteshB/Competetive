#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        low, high = 0, n-1
        
        while low <= high:
            
            mid = (low+high)//2
            
            if mid-1>0 and arr[mid-1] > arr[mid]:
                return mid
                
            elif mid+1<n and arr[mid+1] < arr[mid]:
                return mid+1
                
            if arr[mid] < arr[high]:
                high = mid-1
            else:
                low = mid+1
                
        return 0
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends