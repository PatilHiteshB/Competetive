#User function Template for python3

class Solution:
    def countFractions(self, n, numerator, denominator):
        ans = 0
        v = []
        m = {}
        
        for i in range(n):
            num = numerator[i] / denominator[i]
            v.append(num)
            m[num] = m.get(num, 0) + 1
    
        for i in range(n):
            num = numerator[i] / denominator[i]
            a = (denominator[i] - numerator[i]) / denominator[i]
            m[num] -= 1
            ans += m.get(a, 0)
    
        return ans

#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
# } Driver Code Ends