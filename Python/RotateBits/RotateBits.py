#User function Template for python3

class Solution:
    def rotate(self, N, D):
        # code here
        
        D %= 16
        if(D == 0):
            return [N,N]
            
        arr=[0]*16
        i=15
        while(N != 0):
            arr[i] = N%2
            N = N//2
            i-=1
        
        ret =[]
        res = 0
        pos = 0
        for i in range(D)[::-1]:
            res += arr[i]*2**pos
            pos+=1
        for i in range(16)[:D-1:-1]:
            res += arr[i]*2**pos
            pos+=1
        
        ret.append(res)
        res = 0
        pos = 0
        for i in range(16-D)[::-1]:
            res += arr[i]*2**pos
            pos+=1
        for i in range(16)[:16-D-1:-1]:
            res += arr[i]*2**pos
            pos+=1
        ret.append(res)
        return ret



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends