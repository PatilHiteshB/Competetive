#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here 
        
        mp = {i:0 for i in A}
        for i in range(len(A)):
            mp[A[i]] = i
            
        if B[0] in mp.keys():
            ind = mp[B[0]]
        else:
            return -1
            
        count = (len(B) - ind)//len(A)
        S = ""
        for i in range(count):
            S += A
            
        if S.__contains__(B):
            return count
        S += A
        if S.__contains__(B):
            return count+1
        S += A
        if S.__contains__(B):
            return count+2
        return -1
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends