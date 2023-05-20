#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def check(self, mp, K):
        arr = list(mp.keys())
        start = arr[0]
        
        while K > 0:
            if start in mp:
                if mp[start] > 1:
                    mp[start] += -1
                else:
                    del mp[start]
                
                start += 1
            else:
                return False
                
            K += -1
            
        return True
        
        
    def isStraightHand(self, N, groupSize, hand):
        # Code here
        mp = {i:0 for i in hand}
        for i in hand:
            mp[i] += 1
            
        while mp:
            
            if not self.check(mp, groupSize):
                return False
                
        return True
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, groupSize = list(map(int, input().split()))
        hand = list(map(int, input().split()))
        ob = Solution()
        res = ob.isStraightHand(N, groupSize, hand);
        print(res)
# } Driver Code Ends