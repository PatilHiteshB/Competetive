#User function Template for python3


class Solution:
    def maxLength(self, arr, N):
        #code here
        
        maxLen, countNeg, prevZero, firstNeg = 0, 0, -1, -1
        
        for i in range(N):
            
            if arr[i] < 0:
                
                countNeg += 1
                if firstNeg == -1:
                    firstNeg = i
            
            if arr[i] == 0:
                
                firstNeg = -1
                countNeg = 0
                prevZero = i
                
            else:
                
                if countNeg%2 == 0:
                    maxLen = max(maxLen, i - prevZero)
                else:
                    maxLen = max(maxLen, i - firstNeg)
                    
        
        return maxLen

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())

            arr=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.maxLength(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends