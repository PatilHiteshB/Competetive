#User function Template for python3

class Solution:
    def searchWord(self, grid, word):
        row=len(grid)
        l1=[]
        column=len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j]==word[0]:
                    ans=False
                    ans=ans or self.check_left(i,j,word,grid,0)
                    ans=ans or self.check_up(i,j,word,grid,0)
                    ans=ans or self.check_right(i,j,word,grid,0)
                    ans=ans or self.check_down(i,j,word,grid,0)
                    ans=ans or self.check_left_up(i,j,word,grid,0)
                    ans=ans or self.check_right_up(i,j,word,grid,0)
                    ans=ans or self.check_down_left(i,j,word,grid,0)
                    ans=ans or self.check_down_right(i,j,word,grid,0)
                    if ans==True:
                        l1.append([i,j])
        if not l1:
            return [[-1]]
        else:
            return l1
    def check_left(self,x,y,word,grid,word_i):
        if y<0:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return self.check_left(x,y-1,word,grid,word_i+1)
     
    def check_up(self,x,y,word,grid,word_i):
        if x<0:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return self.check_up(x-1,y,word,grid,word_i+1)
        
    def check_right(self,x,y,word,grid,word_i):
        if y>len(grid[0])-1:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return self.check_right(x,y+1,word,grid,word_i+1)
        
    def check_down(self,x,y,word,grid,word_i):
        if x>len(grid)-1:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return self.check_down(x+1,y,word,grid,word_i+1)
        
    def check_left_up(self,x,y,word,grid,word_i):
        if x<0 or y<0:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return self.check_left_up(x-1,y-1,word,grid,word_i+1)
        
        
    def check_right_up(self,x,y,word,grid,word_i):
        if x<0 or y>len(grid[0])-1:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return self.check_right_up(x-1,y+1,word,grid,word_i+1)
    
    def check_down_left(self,x,y,word,grid,word_i):
        if x>len(grid)-1 or y<0:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return self.check_down_left(x+1,y-1,word,grid,word_i+1)
    
    
    def check_down_right(self,x,y,word,grid,word_i):
        if x>len(grid)-1 or y>len(grid[0])-1:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return self.check_down_right(x+1,y+1,word,grid,word_i+1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends