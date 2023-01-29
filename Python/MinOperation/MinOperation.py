class Solution:
    def solve(self, a : int, b : int) -> int:
        # code here
        if a == b:
            return 0
        
        k = a&b
        if a == k or b == k:
            return 1
            
        return 1 if (a == 0 or b == 0) else 2



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.solve(a, b)
        
        print(res)
        

# } Driver Code Ends