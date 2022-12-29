#User function Template for python3

class Solution:
    def asteroidCollision(self, N, arr):
        # Code here
        stck = []
        
        for i in arr:
            
            flag = True
            
            while stck and (stck[-1]>0 and i<0):
                
                if abs(i) > abs(stck[-1]):
                    stck.pop()
                elif abs(i) == abs(stck[-1]):
                    flag = False
                    stck.pop()
                    break
                else:
                    flag = False
                    break
            
            if flag == True:
                stck.append(i)
                
        return stck
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends