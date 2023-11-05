from collections import Counter
class Solution:
    def topK(self, arr, k):
        a=Counter(arr)
        x=sorted(a.items(),key=lambda x:(-x[1],-x[0]))
        return [i[0] for i in x][:k]


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
    	
# } Driver Code Ends