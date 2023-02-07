#User function Template for python3


class Solution:
    def maxLength(self, arr, n):
        #code here
        ma = 0
        for i in range(n):
            pr = arr[i]
            
            if pr > 0:
                    ma = max(ma, 1)
                    
            for j in range(i+1, n):
                pr *= arr[j]
                
                if pr > 0:
                    ma = max(ma, j-i+1)
            
        
        return ma

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