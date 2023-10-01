#User function Template for python3

class Solution:
   def endPoints(self, matrix, m, n):
       direction={
           "up":"right",
           "right":"down",
           "down":"left",
           "left":"up",
       }
       i,j=0,0
       curr="right"
       while True:
           if matrix[i][j]==0:
               if curr=="left":
                   j-=1
                   if j<0:
                       return [i,j+1]
               elif curr=="right":
                   j+=1
                   if j>n-1:
                       return [i,j-1]
               elif curr=="down":
                   i+=1
                   if i>m-1:
                       return [i-1,j]
               elif curr=="up":
                   i-=1
                   if i<0:
                       return [i+1,j]
           else:
               matrix[i][j]=0
               curr=direction[curr]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends