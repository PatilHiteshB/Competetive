#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def removeReverse(self, S): 
        #code here
        
        mp = {i:0 for i in range(26)}
        
        for i in S: mp[ord(i)-ord('a')] += 1
        
        begin = ""
        end = ""
        
        cnt = 0
        flag = True
        
        i, j = 0, len(S)-1
        
        while i <= j:
            
            ch = ''
            if flag: 
                ch = S[i]
                i += 1
            else:
                ch = S[j]
                j += -1
                
            if mp[ord(ch)-ord('a')] > 1:
                mp[ord(ch)-ord('a')] += -1
                cnt += 1
                flag = not flag
            else:
                if flag: 
                    begin += ch
                else: 
                    end = ch + end


        ans = begin + end        
        if cnt%2 == 1: 
            return ans[::-1]
        return ans



        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends