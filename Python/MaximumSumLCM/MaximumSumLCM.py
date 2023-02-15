#User function Template for python3
class Solution:

        
    def maxSumLCM (self, n):
        # code here 
            
        ls = [n]
        
        for i in range(1, int(n**0.5)+1):
            
            if n%i == 0:
                ls.append(i)
                
                if i != n//i:
                    ls.append(n//i)
                
        return sum(set(ls))


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.maxSumLCM(n))
# } Driver Code Ends