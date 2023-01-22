#User function Template for python3
from queue import PriorityQueue
class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self, arr, N, K):
        # code here
        que = PriorityQueue()
        
        for i in arr:
            
            que.put(i)
            
        answer = []
        for i in range(1, K+1):
            answer.append(que.get())
            
        for i in range(len(answer)):
            answer[i] = -1 * answer[i]
            
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends