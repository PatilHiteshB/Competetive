#User function Template for python3

class Solution:
    
    def arrangeString(self, S):
        # code here
        if S=="A":
            return "A"
        x=[]
        y=[]
        for i in S:
            if i.isalpha():
                x.append(i)
            elif i.isnumeric():
                y.append(int(i))
        x=sorted(x)
        z=''.join(x)
        return (z+str(sum(y)))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)
# } Driver Code Ends