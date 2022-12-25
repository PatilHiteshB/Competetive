#User function Template for python3

class Solution:
	def MissingNo(self, arr):
		# Code here
		N = len(arr)
		indexi, indexj = 0, 0
		leftD, rightD = 0, 0
		col_sum = [0]*N
		row_sum = [0]*N
		
		for i in range(N):
		    leftD += arr[i][i]
		    rightD += arr[i][N-i-1]
		    
		    
		    
		    for j in range(N):
		        
		        if arr[i][j] == 0:
		            indexi, indexj = i, j
                row_sum[i] += arr[i][j]
                col_sum[j] += arr[i][j]
            
        rowSum = 0    
        if indexi == 0:
            rowSum = row_sum[indexi+1]
        else:
            rowSum = row_sum[indexi-1]
            
            
        colSum = 0
        if indexj == 0:
            colSum = col_sum[indexj+1]
        else:
            colSum = col_sum[indexj-1]
        
        ans = colSum - col_sum[indexj]
        
        if ans <= 0 or ans != (rowSum-row_sum[indexi]):
            return -1
            
        if indexi == indexj:
            leftD += ans
            
        if indexi == (n-indexj-1):
            rightD += ans
            
        if leftD != rightD:
            return -1
            
        col_sum[indexj] += ans
        row_sum[indexi] += ans
        
        for i in row_sum:
            if i != leftD:
                return -1
                
        for i in col_sum:
            if i != leftD:
                return -1
                
        return ans
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.MissingNo(matrix)
		print(ans)

# } Driver Code Ends