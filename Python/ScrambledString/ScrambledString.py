#User function Template for python3

class Solution:
    def __init__ (self):
        self.mp = {}
    def isSimilar(self, s1, s2):
        
        # print("{} {}".format(s1, s2))
        if s1 == s2:
            return True
            
        if len(s1) <= 1:
            return False
        
        # if len(s1) != len(s2):
        #     return False
        
        N = len(s1)
        
        flag = False
        
        key = s1 + "_" + s2
        
        if key in self.mp.keys():
            return self.mp[key]
        
        for i in range(1, N):
            
            if self.isSimilar(s1[:i], s2[:i]) and self.isSimilar(s1[i:], s2[i:]):
                flag = True
                break
            
            if self.isSimilar(s1[:i], s2[N-i:]) and self.isSimilar(s1[i:], s2[:N-i]):
                flag = True
                break
        
        key = s1 + "_" + s2
        self.mp[key] = flag
            
        return flag
        
        
            
        
    def isScramble(self, s1, s2):
        ##code here
        return self.isSimilar(s1, s2)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        S1,S2=input().split()
        if(Solution().isScramble( S1 , S2)):
            print("Yes")
        
        else:
            print("No")


# } Driver Code Ends