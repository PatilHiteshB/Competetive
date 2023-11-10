#User function Template for python3
class Solution:
    
    def printMinNumberForPattern(ob,S):
        n=len(S)
        stack=[]
        ans=""
        count=1
        for i in range(n):
            stack.append(count)
            count+=1
            if S[i]=="I":
                while stack:
                    ans+=str(stack.pop())
        stack.append(count)
        while stack:
            ans+=str(stack.pop())
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends