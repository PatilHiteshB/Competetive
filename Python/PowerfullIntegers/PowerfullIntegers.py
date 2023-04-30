from typing import List


class Solution:
    def powerfullInteger(self, n : int, arr : List[List[int]], k : int) -> int:
        # code here
        mp = {}
        
        for i, j in arr:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
                
            if j+1 in mp:
                mp[j+1] += -1
            else:
                mp[j+1] = -1
                
        # print(mp)
        count = 0
        pcount = -1
        ans = -1
        for i in sorted(mp.keys()):
            
            count += mp[i]
                
            if count >= k:
                ans = i
            elif pcount >= k:
                ans = i-1
                
            pcount = count
                
        return ans


#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        intervals=IntMatrix().Input(n, 2)
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.powerfullInteger(n, intervals, k)
        
        print(res)
        

# } Driver Code Ends