#User function Template for python3

class Solution:
    
    def atmost(self, n, arr, k):
        
        start = end = answer = count = 0
        
        while end < n:
            if arr[end]&1 == 1:
                count += 1
                
            while count>k and start<n:
                if arr[start]&1 == 1:
                    count += -1
                start += 1
            answer += end-start+1
            end += 1
            
        return answer
        
    def countSubarray(self, n, arr, k):
        # Code here
        return self.atmost(n, arr, k) - self.atmost(n, arr, k-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        print(ob.countSubarray(n, nums, k))
# } Driver Code Ends