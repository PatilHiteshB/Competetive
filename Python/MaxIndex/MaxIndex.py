#User function Template for python3
class Solution:

	def maxIndexDiff(self, arr, n):
	    
        v_min = [0] * n
        v_max = [0] * n
        v_min[0] = arr[0]
        v_max[n - 1] = arr[n - 1]
        for i in range(1, n):
            v_min[i] = min(v_min[i - 1], arr[i])
            v_max[n - i - 1] = max(v_max[n - i], arr[n - i - 1])
            
        ans = 0
        i = 0
        j = 0
        while i < n and j < n:
            if v_min[i] <= v_max[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends