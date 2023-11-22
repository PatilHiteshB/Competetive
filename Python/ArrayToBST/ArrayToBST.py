class Solution:

    def solve(self,nums,st,lst):
        if st>lst:
            return 
        mid=(st+lst)//2
        self.ans.append(nums[mid])
        self.solve(nums,st,mid-1)
        self.solve(nums,mid+1,lst)
        
    
    def sortedArrayToBST(self, nums):
        st=0
        lst=len(nums)-1
        self.ans=[]
        self.solve(nums,st,lst)
        return self.ans

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	nums = list(map(int, input().split()))
	obj = Solution()
	ans = obj.sortedArrayToBST(nums)
	for _ in ans:
		print(_, end = " ")
	print()

# } Driver Code Ends