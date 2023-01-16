#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def nextGreaterElement(self, N, arr):
        # Code here
        arr += arr
        stck = []
        answer = [-1]*(N*2)
        
        for ind, val in enumerate(arr):
            
            while stck and arr[stck[-1]] < arr[ind]:
                temp = stck.pop()
                answer[temp] = arr[ind]
            else:
                stck.append(ind)
                
        return answer[:N]
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.nextGreaterElement(N, arr)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends