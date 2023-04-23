#User function Template for python3

class Solution:
    
    def GCD(self, a, b):
        if b == 0:
            return a
        return self.GCD(b, a%b)
        
    def minimumNumber(self, n, arr):
        #code here
        ans = 0
        for i in arr:
            ans = self.GCD(ans, i)
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends