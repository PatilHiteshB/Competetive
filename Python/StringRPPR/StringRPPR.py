#User function Template for python3

class Solution:
    def count(self, c1, c2, string):
        s1 = []
        s2 = []
        
        cnt1 = cnt2 = 0
        
        s1.append(string[0])
        
        for i in range(1, len(string)):
            
            if s1 and s1[-1] == c1 and string[i] == c2:
                s1.pop()
                cnt1 += 1
                
            else:
                s1.append(string[i])
                
        s2.append(s1.pop())
        
        while s1:
            
            if s2 and s2[-1] == c1 and s1[-1] == c2:
                s2.pop()
                cnt2 += 1
            
            else:
                s2.append(s1[-1])
            
            s1.pop()
                
        
        if c1 == 'p': return (cnt1, cnt2)
        return (cnt2, cnt1)
        
    def solve (self, X, Y, string):
        #code here
        ans = (0, 0)
        if X > Y:
            ans = self.count('p', 'r', string)
        else:
            ans = self.count('r', 'p', string)
            
        return ans[0]*X + ans[1]*Y
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()
        

        ob = Solution()
        print(ob.solve(X,Y,S))
# } Driver Code Ends