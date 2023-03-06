class Solution:
    def noConseBits(self, n):
        ans = 0
        i = 31
        count = 0
        while i >= 0:
            if count <= 1 and (n & (1 << i)):
                ans = ans | (1 << i)
                count += 1
            else:
                count = 0
            i -= 1
        return ans

        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.noConseBits(n)
        
        print(res)
        

# } Driver Code Ends