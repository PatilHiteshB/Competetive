#User function Template for python3

class Solution:    
    def countX(self, start_range, end_range, target_digit):
        digit_count = 0

        for num in range(start_range + 1, end_range):
            digit_count += str(num).count(str(target_digit))

        return digit_count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        L,R,X=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.countX(L,R,X)
        print(ans) 
# } Driver Code Ends