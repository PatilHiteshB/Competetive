#User function Template for python3



class Solution():
        
    def longestString(self, arr, n):
        #your code goes here
        arr.sort(key=compare)
        mp = {i:1 for i in arr}

        ans = ""
        for i in arr:
            isValid = True
            
            for k in range(len(i)):
                if i[:k+1] not in mp.keys():
                    isValid = False
                    break
            if isValid:
                if len(ans) < len(i):
                    ans = i
                elif len(ans) == len(i) and ans > i:
                    ans = i
        
        return ans
                    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends