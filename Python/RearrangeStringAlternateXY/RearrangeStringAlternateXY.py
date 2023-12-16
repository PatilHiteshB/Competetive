#User function Template for python3

class Solution:
    def arrangeString(self, s, x, y):
        # code here
        ans = ''
        zero,one = s.count('0'),s.count('1')
        
        while zero>0 and one>0:
            ans += '0' * min(x,zero)
            zero -= min(x,zero)
            ans += '1' * min(y,one)
            one -= min(y,one)
        ans += '0' * zero + '1' * one
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x,y = input().strip().split(" ")
        x,y = int(x), int(y)
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s,x,y)
        print(ans)
# } Driver Code Ends