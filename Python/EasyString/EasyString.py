#User function Template for python3

class Solution:

    def transform(self, S):
        # code here
        x=S.lower()
        string = ""
        count = 0
        temp = x[0]
        
        for i in range(len(S)):
            if x[i] == temp :
                count = count + 1
            else:
                string = string + str(count)
                string = string + temp
                count = 1
                temp = x[i]
                
        return string+str(count)+temp

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.transform(S))
# } Driver Code Ends