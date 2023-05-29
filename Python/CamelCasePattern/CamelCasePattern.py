#User function Template for python3

import re

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        #code here
        p = "^[a-z]*"
        for ch in Pattern:
            p += ch + "[a-z]*"
        
        ans = []
        for word in Dictionary:
            if re.search(p, word):
                ans.append(word)
        
        return ans if ans else [-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends