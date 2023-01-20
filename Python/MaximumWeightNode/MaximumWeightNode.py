#User function Template for python3

class Solution():
    def maxWeightCell(self, N, arr):
        #your code goes here
        
        mp = {}
        
        answer = 0
        count = 0
        
        for i in range(N):
            
            if arr[i] in mp.keys():
                
                mp[arr[i]] += i
                
            else:
                
                mp[arr[i]] = i
                
            if arr[i] != -1 and mp[arr[i]] >= count:
                
                answer = arr[i]
                count = mp[arr[i]]
                
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends