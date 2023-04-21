#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        #code here
        i, j = 0, 0
        n, m = len(s1), len(s2)
        ans = 0
        
        while i<n and j<m:
            
            if s2[j] in s1[i]:
                
                ln = len(s2[j])
                pre = s1[i][:ln]
                suf = s1[i][-ln:]
                
                if pre == s2[j] or suf == s2[j]:
                    ans += 1
                    i = 0
                    j += 1
                else:
                    i += 1
                    
            else:
                i += 1
        
        return ans
        
        

#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        s1 = list(map(str, input().split()))
        s2 = list(map(str, input().split()))
        obj=Solution()
        print(obj.prefixSuffixString(s1, s2))
# } Driver Code Ends