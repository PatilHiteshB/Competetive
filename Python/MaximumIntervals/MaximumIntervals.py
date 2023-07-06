#User function Template for python3

class Solution:

    def findMaxGuests(self, arr, brr, N):
        # code here
        arr.sort()
        brr.sort()
        
        count = 0
        ind = 0
        bnd = 0
        ans = 0
        at = 0
        
        while ind < len(arr) and bnd < len(brr):
            
            count += 1
            
            while bnd < len(brr) and arr[ind] > brr[bnd]:
                count += -1
                bnd += 1
            
            if count > ans:
                ans = count
                at = arr[ind]
            ind += 1
            
        return [ans, at]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        
        N = int(input())

        entry = [int(x) for x in input().split()]
        exit =  [int(x) for x in input().split()]

        solObj = Solution()
        ans = solObj.findMaxGuests(entry, exit, N) 
        print(ans[0],ans[1])
        

# } Driver Code Ends