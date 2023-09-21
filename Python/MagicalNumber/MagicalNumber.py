#User function Template for python3

def binarySearch(arr,low,high):
    '''
    arr: given array
    low: low index initialize as zero
    high: high index initialize as len(arr)-1
    return: magical n.o or -1
    '''
    
    ans = -1 # if mid != mid[arr]
    while low <= high:
        #mid is my index 
        mid = (high + low)//2
        if mid == arr[mid]: 
            ans = arr[mid] #store whatever is the last ans
            high = mid - 1 # look on the left sided for smaller 
        elif arr[mid] > mid:
            high = mid -1
        else:
            low = mid + 1
        
    return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        print(binarySearch(arr,0,n-1))
# } Driver Code Ends