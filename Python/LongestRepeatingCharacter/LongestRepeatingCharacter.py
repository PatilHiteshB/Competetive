#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def characterReplacement(self, arr, K):
        # Code here
        
        start = end = answer = 0
        
        max_count = 0
        char_count = [0]*26
        while end < len(arr):
            
            temp = ord(arr[end])-ord("A")
            char_count[temp] += 1
            max_count = max(max_count, char_count[temp])
            
            while end - start - max_count + 1 > K:
                
                char_count[ord(arr[start])-ord("A")] += -1
                start += 1
                
            answer = max(answer, end-start+1)
                
            end += 1
            
        
        return answer
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends