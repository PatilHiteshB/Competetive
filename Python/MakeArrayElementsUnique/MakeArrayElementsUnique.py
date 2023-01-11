#User function Template for python3

class Solution:
    def minIncrements(self, arr, N): 
        # Code here
        mp = {i:0 for i in arr}
        
        answer = 0
        for i in arr:
            
            if i in mp and mp[i] == 0:
                mp[i] += 1
            elif i in mp:
 
                temp = i
                while temp in mp:
                    answer += 1
                    temp += 1
                mp[temp] = 0
                
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr,N))
        
        T -= 1
# } Driver Code Ends