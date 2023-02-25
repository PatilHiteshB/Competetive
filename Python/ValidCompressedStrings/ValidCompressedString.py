#User function Template for python3

class Solution:
    def checkCompressed(self, S, T):
        # code here 
        i, j = 0, 0
        
        while i < len(S) and j < len(T):
            
            if S[i] == T[j]:
                 i += 1
                 j += 1
                 continue
             
            tmp = 0
            while j < len(T) and T[j].isnumeric():
                tmp = tmp*10 + int(T[j])
                j += 1
                
            i += tmp
            if tmp == 0: return 0
            
            
            
                
        return 1 if i == len(S) and j == len(T) else 0
            
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        T = input()
        
        ob = Solution()
        print(ob.checkCompressed(S,T))
# } Driver Code Ends