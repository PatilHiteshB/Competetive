
class Solution:
    def arrayRepresentHeap(self, arr, n):
        # Your code goes here 
        
        index = 0
        
        while index < n:
            
            parent = arr[index]
            
            l, r = 2*index+1, 2*index+2
            
            if l < n and parent < arr[l]:
                return 0
            if r < n and parent < arr[r]:
                return 0
            
            index += 1
            
        return 1



#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(ob.arrayRepresentHeap(arr,n))
# } Driver Code Ends