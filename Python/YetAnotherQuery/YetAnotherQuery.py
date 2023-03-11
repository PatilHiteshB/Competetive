from typing import List

from bisect import bisect_left, bisect_right


class Solution:
    def solveQueries(self, N, num, a, Q):
        freq = {}
        for x in a:
            freq[x] = freq.get(x, 0) + 1
            
        mp = {}
        for i in range(N):
            if freq[a[i]] in mp:
                mp[freq[a[i]]].append(i)
            else:
                mp[freq[a[i]]] = [i]
            freq[a[i]] -= 1
            
        ans = []
        for x in Q:
            l, r, k = x[0], x[1], x[2]
            v = mp.get(k, [])
            it1 = bisect_left(v, l)
            it2 = bisect_right(v, r)
            ans.append(it2 - it1)
            
        return ans




#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



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
        
        N = int(input())
        
        
        num = int(input())
        
        
        A=IntArray().Input(N)
        
        
        Q=IntMatrix().Input(num, 3)
        
        obj = Solution()
        res = obj.solveQueries(N, num, A, Q)
        
        IntArray().Print(res)
        

# } Driver Code Ends