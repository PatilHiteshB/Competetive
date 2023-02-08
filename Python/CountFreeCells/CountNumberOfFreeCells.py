#User function Template for python3

class Solution():
    def countZero(self, n, k ,arr):
        #your code here
        mpR, mpC = {}, {}
        ans = []
        
        for i in arr:
            
            mpR[i[0]] = 1
            mpC[i[1]] = 1
            
            rlen = len(mpR.keys())
            clen = len(mpC.keys())
            ans.append(n*n - rlen*n - clen*n + rlen*clen)
            
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = []
    for i in range(k):
        x,y=map(int,input().split())
        arr.append([x, y])
    obj = Solution()
    res = obj.countZero(n, k, arr)
    for i in res:
        print(i,end = " ")
    print()
# } Driver Code Ends