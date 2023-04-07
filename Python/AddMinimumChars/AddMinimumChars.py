#User function Template for python3

class Solution:
    def addMinChar (self, arr):
        # code here 
        start, end = 0, len(arr)-1
        
        ans = len(arr)-1
        while start < end:
            
            if arr[start] != arr[end]:
                start = 0
                end = ans
                ans += -1
            else:
                start += 1
            
            end += -1
            
        return len(arr)-ans-1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends