#User function Template for python3

class Solution:
    
    def isPallin(self, S, start, end):
        while start < end:
            if S[start] != S[end]:
                return False
            start += 1
            end -= 1
            
        return True
    def longestPalin(self, S):
        # code here
        ma = 1
        maS = S[0]
        for i in range(len(S)):
            for j in range(i+1, len(S)):
                if self.isPallin(S, i, j) and len(S[i:j+1]) > ma:
                    ma = len(S[i:j+1])
                    maS = S[i:j+1]
        return maS

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends