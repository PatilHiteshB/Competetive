class Solution:
    def stringMirror(self, arr : str) -> str:
        # code here
        
        ans = arr[0]
        
        for i in range(1, len(str)):
            
            if ord(arr[i-1]) >= ord(arr[i]) and arr[0] != arr[1]:
                ans += arr[i]
                
            else: break
        
        return ans + ans[::-1]
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.stringMirror(str)
        
        print(res)
        

# } Driver Code Ends