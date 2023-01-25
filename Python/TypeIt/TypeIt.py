#User function Template for python3

class Solution:
    def minOperation(self, s): 
        #code here
        answer = ""
        index = len(s)
        count = 0
        
        while index > 0:
            
            if index&1 == 1:
                count +=1
                index += -1
            
            else:
                
                mid = index//2
                
                if s[:mid] == s[mid:index]:
                    count += mid+1
                    break
                else:
                    count += 1
                    index += -1
                
            
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.minOperation(s)
        print(ans)
# } Driver Code Ends