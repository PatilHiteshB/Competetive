#User function Template for python3

#User function Template for python3

class Solution:
    
    def solve(self, arr, vis, ind):
        
        vis[ind] = True
        ans = arr[ind]
        while ind + arr[ind] < len(arr):
            ind += arr[ind]
            ans += arr[ind]
            vis[ind] = True
            
            if arr[ind] == 0:
                break
            
        return ans
        
        
    def knightInGeekland(self, arr, start):
        x, y = start[0], start[1]
        N, M = len(arr), len(arr[0])
        vis = [[False for _ in range(M)] for _ in range(N)]
        
        pq = [(0, x, y)]
        
        ans = [arr[x][y]]
        vis[x][y] = True
        while len(pq) > 0:
            
            step, m, n = pq.pop(0)
            steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
            for i, j in steps:
                i += m
                j += n
                # print("{} {}".format(N, M))
                
                if i < N and i >= 0 and j < M and j >= 0 and vis[i][j] == False:
                    # print(count)
                    pq.append((step+1, i, j))
                    vis[i][j] = True
                    # count += 1
                    if len(ans) <= step+1:
                        ans.append(arr[i][j])
                    else:
                        ans[step+1] += arr[i][j]
        
        # print(ans)
        vis = [False for _ in range(len(ans))]
        ma, maInd = 0, 0
        for i in range(len(ans)):
            
            if vis[i] == False:
                temp = self.solve(ans, vis, i)
                if temp > ma:
                    ma = temp
                    maInd = i
                    
        return maInd
                    
                

                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,m = map(int, input().split())
        starting_x, starting_y = map(int, input().split())
        orignal_array = []

        for i in range(n):
            l = list(map(int, input().split()))
            orignal_array.append(l)

        res = Solution().knightInGeekland(orignal_array, [starting_x, starting_y])
        print(res)
# } Driver Code Ends