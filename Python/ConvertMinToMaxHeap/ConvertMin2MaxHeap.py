#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def heapify(self, arr, index):
        
        l, r = 2*index+1, 2*index+2
        largest = index
        
        if l<len(arr) and arr[largest] < arr[l]:
            largest = l
        if r<len(arr) and arr[largest] < arr[r]:
            largest = r
            
        if arr[largest] != arr[index]:
            arr[largest], arr[index] = arr[index], arr[largest]
            self.heapify(arr, largest)
            

    def convertMinToMaxHeap(self, N, arr):
        # Code here
        
        for i in range((N-1)//2, -1, -1):
            self.heapify(arr, i)
            
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.convertMinToMaxHeap(N, arr)
        for val in arr:
            print(val, end = ' ')
        print()
# } Driver Code Ends