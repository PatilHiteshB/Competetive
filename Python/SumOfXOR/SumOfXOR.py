#User function Template for python3

class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        
        ans = 0
        
        for i in range(32):
            
            c_zero = 0
            c_one = 0
            
            for j in range(n):
                
                if (arr[j] & (1<<i)) == 0:
                    c_zero += 1
                else:
                    c_one += 1
                    
            
            ans += c_zero * c_one * (1<<i)
            
        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends