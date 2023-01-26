#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self, arr, N):
        #code here
        stckU = []
        stckL = []
        
        for i in arr:
            if ord(i) in range(ord('A'), ord('Z')+1):
                stckU.append(i)
            else:
                stckL.append(i)
        
        stckL.sort()
        stckU.sort()
                
        answer = ""
        
        for i in arr:
            if ord(i) in range(ord('A'), ord('Z')+1):
                answer += stckU.pop(0)
            else:
                answer += stckL.pop(0)
                
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends