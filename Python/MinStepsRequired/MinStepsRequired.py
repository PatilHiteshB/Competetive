class Solution:
    def minSteps(self, arr : str) -> int:
        # code here
        a, b = 0, 0
        
        ind = 0
        while ind < len(str):
            
            if arr[ind] == 'a':
                
                while ind < len(str) and arr[ind] == 'a':
                    ind += 1
                a += 1
                
            else:
                
                while ind < len(str) and arr[ind] == 'b':
                    ind += 1
                b += 1
                
        return min(a, b)+1
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends