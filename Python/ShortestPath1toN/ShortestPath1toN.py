#User function Template for python3

class Solution:
    def minimumStep (self, n):
        #complete the function here
        if n == 1:
            return 0
            
        i = n
        count = 0
        
        while True:
            if i%3 == 0:
                i //= 3
            
            else:
                i += -1
            
            count += 1
            
            if i == 1:
                return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minimumStep(n))
# } Driver Code Ends