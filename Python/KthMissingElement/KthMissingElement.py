#User function Template for python3

def missingAtIndex(start, end, index):
    return end - (start+index)
def KthMissingElement (arr, N, K) : 
    #Complete the function
    
    if N <= 1:
        return -1
    
    low, high = 0, N-1
    
    while low <= high:
        
        mid = (low+high)//2
        
        if arr[mid] - (arr[0] + mid) < K:
            low = mid + 1
        else:
            high = mid - 1
        
        
            
    if low == N:
        return -1
    return low-1 + arr[0] + K
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n, K = map(int ,input().split())
    arr = list(map(int,input().strip().split()))
    res = KthMissingElement(arr, n, K)
    print(res)



# } Driver Code Ends