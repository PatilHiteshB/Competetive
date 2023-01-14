#User function Template for python3

class Solution: 
    
    def printPermutation(self, arr, N, index, mp):
        answer = 0
        
        if index == N:
            return 1
        
        for i in range(index, N):
            arr[i], arr[index] = arr[index], arr[i]
            
            if index == 0:
                answer += self.printPermutation(arr, N, index+1, mp)
            elif (arr[index], arr[index-1]) in mp:
                answer += self.printPermutation(arr, N, index+1, mp)
            arr[i], arr[index] = arr[index], arr[i]
        
        return answer
        
    def luckyPermutations(self, N, M, arr, graph):
        # Code here
        
        mp1 = {(i[0], i[1]):1 for i in graph}
        mp2 = {(i[1], i[0]):1 for i in graph}
        
        mp = {**mp1, **mp2}
        # print(mp)
        
        return self.printPermutation(arr, N, 0, mp)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0:
        N, M=[int(i) for i in input().split()]
        arr = [int(i) for i in input().split()]
        graph = []
        for i in range(M):
            graph.append([int(i) for i in input().split()])
        ob = Solution()
        print(ob.luckyPermutations(N, M, arr,graph))
        
        T -= 1
# } Driver Code Ends