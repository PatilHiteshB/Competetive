#User function Template for python3

class Solution:
    def countAtMostK(self, s, k):
        start = end = ans = 0
        mp = {}
        
        while end < len(s):
            if s[end] in mp.keys():
                mp[s[end]] += 1
            else:
                mp[s[end]] = 1
                
                
            while len(mp) > k:
                mp[s[start]] -= 1
                if mp[s[start]] == 0:
                    mp.pop(s[start])
                start += 1
                    
            ans += end - start + 1
            end += 1
            
            # print("{} {}".format(s[end-1], len(mp)))
        
        return ans
            
    def substrCount (self,s, k):
        # your code here
        return self.countAtMostK(s, k) - self.countAtMostK(s, k-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends