#User function Template for python3
from queue import PriorityQueue
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        que = PriorityQueue()
        for xarr in arr:
            for i in xarr:
                que.put(i)
        
        answer = []        
        for i in range(K*K):
            answer.append(que.get())
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends