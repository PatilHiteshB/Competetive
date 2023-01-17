#User function Template for python3

class Solution:
    def longestOnes(self, n, arr, k):
        # Code here
        
        ans = 0
        start = end = 0
        count0 = count1 = 0
        while end < n:
            
            if arr[end] == 0:
                count0 += 1
                
            if count0 > k:
                
                if arr[start] == 0:
                    count0 -= 1
                    
                start += 1
                
            else:
                
                ans = max(ans, end-start+1)
                
            end += 1
            
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