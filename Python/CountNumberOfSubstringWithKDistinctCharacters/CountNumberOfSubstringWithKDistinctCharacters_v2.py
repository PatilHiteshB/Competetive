#User function Template for python3

class Solution:
    def subStrCountAtMostK(self, s, k):
        count = 0   
        left = 0
        map = dict()

        for right in range(len(s)):
            map[s[right]] = map.get(s[right], 0)
            map[s[right]] += 1

            while len(map) > k:
                map[s[left]] -= 1
                if map[s[left]] == 0:
                    del map[s[left]]
                left += 1

            count += right - left + 1

        return count

    def substrCount(self, s, k):
        return self.subStrCountAtMostK(s, k) - self.subStrCountAtMostK(s, k - 1)
        

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