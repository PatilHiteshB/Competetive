#User function Template for python3
from queue import PriorityQueue
class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self, arr, N):
        #code here
        mpL = {}
        mpU = {}
        
        
        for i in arr:
            if i.islower():
                if i in mpL.keys():
                    mpL[i] += 1
                else:
                    mpL[i] = 1
            else:
                if i in mpU.keys():
                    mpU[i] += 1
                else:
                    mpU[i] = 1
                
        answer = ""
        stckL = list(mpL.keys())
        stckL.sort()
        stckU = list(mpU.keys())
        stckU.sort()
        
        
        l = u = 0
        for i in arr:
            if i.islower():
                if mpL[stckL[l]] > 1:
                    answer += stckL[l]
                    mpL[stckL[l]] += -1
                    continue
                answer += stckL[l]
                l += 1
            else:
                if mpU[stckU[u]] > 1:
                    answer += stckU[u]
                    mpU[stckU[u]] += -1
                    continue
                answer += stckU[u]
                u += 1
                
                
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