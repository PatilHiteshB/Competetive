#User function Template for python3

class Solution:
    def longestOnes(self, n, arr, k):
        # Code here
        
        ans = 0
        for i in range(n):
            
            temp = k
            count = 0
            for j in range(i, n):
                if arr[j] == 1:
                    count += 1
                    
                elif temp > 0:
                    count += 1
                    temp += -1
                    
                else:
                    break
                
            ans = max(count, ans)
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        print(ob.longestOnes(n, a, k))
# } Driver Code Ends