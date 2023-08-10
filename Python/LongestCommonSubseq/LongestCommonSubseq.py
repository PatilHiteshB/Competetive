#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, s1, s2):
        
        # code here
        if m > n:
            n, m = m, n
            s1, s2 = s2, s1
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr.copy()
        return prev[m]



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends