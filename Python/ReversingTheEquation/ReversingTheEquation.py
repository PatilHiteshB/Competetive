#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        ans = ""
        ind = len(s)-1
        while ind >= 0:
            
            if s[ind] in ['+', "-", "*", "/"]:
                ans += s[ind]
                ind -= 1
                continue
            
            num = ""
            while ind >= 0 and ord(s[ind]) >= ord('0') and ord(s[ind]) <= ord('9'):
                num += s[ind]
                ind -= 1
                
            ans += num[-1::-1]
            
        return ans
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends