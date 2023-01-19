#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def subSequence(self, strn):
        
        answer = set()
        N = 1 << len(strn)
        
        for i in range(N):
            
            temp = ""
            
            for j in range(len(strn)):
                if (i>>j)&1 == 1:
                    temp += strn[j]
            
            answer.add(temp)
            
        return len(answer)
            
            
                
    def betterString(self, str1, str2):
        # Code here
        
        if self.subSequence(str1) >= self.subSequence(str2):
            return str1    
        return str2
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends