#User function Template for python3

class Solution:
    def swapBitGame (self,N):
        # code here 
        bnum = bin(N)[2:]  #change to binary number
        count = 0    #count variable to count number of set bits
        for i,bit in enumerate(bnum):
            if bit == '1':
                count+=1
        if count%2==0:  #count is even then player 2 wins otherwise player 1
            return 2
        else:
            return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
        

        ob = Solution()
        print(ob.swapBitGame(N))
# } Driver Code Ends