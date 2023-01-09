class Solution:
    
    def possibleCombo(self, arr, N, K, total):
        
        ind = su = 0
        count = 0
        
        while ind < N:
            
            su += arr[ind]
            
            if su >= total:
                count += 1
                su = arr[ind]
                
                
            ind += 1
        
        if count >= K:
            return True
        
        return False
        
        
    #Function to find minimum number of pages.
    def findPages(self, arr, N, K):
        #code here
        
        if N < K:
            return -1
            

        low, high = 0, sum(arr)
        answer = max(arr)
        
        if N == K:
            return answer
        

        while low<=high:
            
            mid = (low+high)//2
    
            
            if self.possibleCombo(arr, N, K, mid):
                
                answer = max(mid, answer)
                low = mid + 1
                
            else:
                
                high = mid - 1
                
        return answer
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends