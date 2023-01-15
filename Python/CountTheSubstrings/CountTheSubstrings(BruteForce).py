#User function Template for python3


class Solution():
    def solve(self, arr):
        cnt0 = cnt1 = 0
        for i in arr:
            if i == "0":
                cnt0 += 1
            else:
                cnt1 += 1
                
        return 1 if cnt1 > cnt0 else 0
        
    def countSubstring(self, S, index=0):
        #your code here
        N = len(S)
        
        if len(S) == 0:
            return 0
            
        answer = 0
        for i in range(1, N+1):
            
            for j in range(N-i+1):
                
                answer += self.solve(S[j:j+i])
                
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().countSubstring(s))
# } Driver Code Ends