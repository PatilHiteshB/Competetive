#User function Template for python3

class Solution:
    def beautySum(self, s):
        # Code here
        
        answer = 0
        
        for i in range(len(s)):
            
            mp = {}

            for j in range(i, len(s)):
                
                if s[j] in mp.keys():
                    mp[s[j]] += 1
                
                else:
                    mp[s[j]] = 1
                    
                ma = max(mp.values())
                mi = min(mp.values())
                
                answer += ma - mi
                
                
        return answer        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.beautySum(s))
# } Driver Code Ends