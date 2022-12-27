#User function Template for python3



def maxArea(arr,N):
    #code here
    start, end = 0, N-1
    
    ans = 0
    while start < end:
        water = (end-start)*min(arr[start], arr[end])
        
        if water>ans:
            ans = water
            
        if arr[start] < arr[end]:
            start+=1
        else:
            end-=1
        
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends