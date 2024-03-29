#User function Template for python3

class Solution:
    def appleSequences(self, n, m, arr):
        # code here 
        
        start = end = ans = 0
        
        while end < len(arr):
            
            if arr[end] == 'O':
                
                m += -1
                
            while m < 0 and start < len(arr):
                
                if arr[start] == 'O':
                    m += 1
                start += 1
                
            ans = max(ans, end-start+1)
            end += 1
            
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N, M, arr))

# } Driver Code Ends