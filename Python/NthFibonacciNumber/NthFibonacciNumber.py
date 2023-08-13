
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n in [0, 1, 2]:
            return 0 if n == 0 else 1
            
        first, second = 1, 1
        
        while n > 2:
            first, second = second, first+second
            n += -1
            
        return second % 1000000007



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends