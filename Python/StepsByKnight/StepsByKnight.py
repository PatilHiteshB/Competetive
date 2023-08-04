class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    from collections import deque
	    
	    source_row = KnightPos[0] - 1
	    source_col = KnightPos[1] - 1
	    
	    dist = (TargetPos[0] -1, TargetPos[1] - 1)

	    queue = deque([(source_row, source_col, 0)])
	    
        deltas = [(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2), (-2,-1), (-1,-2)]
	    
	    visited = set()
	    
	    while queue:
	        row, col, step = queue.popleft()
	        
	        if (row, col) == dist: return step
	    
	        for drow, dcol in deltas:
	            row_delta = drow + row
	            col_delta = dcol + col
	            
	            row_inbound = 0 <= row_delta < N
                col_inbound = 0 <= col_delta < N 
        
                if not row_inbound or not col_inbound: continue
	            
	            if (row_delta, col_delta) not in visited:
	                queue.append((row_delta, col_delta, step + 1))
	                visited.add((row_delta, col_delta))
	        
	    return -1

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends