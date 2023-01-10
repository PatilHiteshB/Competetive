#User function Template for python3

class Solution:
    
    def romanToDecimal(self, S): 
        # code here
        
        mp = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
        
        prev = answer = 0
        index = len(S)-1
        
        while index >= 0:
            
            if mp[S[index]] >= prev:
                answer += mp[S[index]]
            else:
                answer -= mp[S[index]]
                
            prev = mp[S[index]]
            index -= 1
            
            
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends