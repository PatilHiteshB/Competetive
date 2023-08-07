#User function Template for python3

class Solution:
    
    def is_safe(self,grid,row,col,val):
        for i in range(9):
            if grid[row][i]==val:
                return False
            if grid[i][col]==val:
                return False
            if grid[(3*(row//3))+(i//3)][(3*(col//3))+(i%3)]==val:
                return False
        return True
    
    def SolveSudoku(self,grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col]==0:
                    for val in range(1,10):
                        if self.is_safe(grid,row,col,val):
                            grid[row][col]=val
                            next=self.SolveSudoku(grid)
                            if next:
                                return True
                            else:
                                grid[row][col]=0
                    return False
        return True
    
    def printGrid(self,arr):
        for row in range(9):
            for col in range(9):
                print(arr[row][col],end=" ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends