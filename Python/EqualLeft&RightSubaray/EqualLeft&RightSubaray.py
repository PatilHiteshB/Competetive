# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self, arr, N):
        # Your code here
        
        sleft = [0 for _ in range(N)]
        rleft = [0 for _ in range(N)]
        
        su = 0
        for i in range(0, N):
            sleft[i] = su
            su += arr[i]
            
        su = 0
        for i in range(N-1, -1, -1):
            rleft[i] = su
            su += arr[i]
            
        for i in range(N):
            
            if sleft[i] == rleft[i]:
                return i+1
        
        return -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equalSum(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends