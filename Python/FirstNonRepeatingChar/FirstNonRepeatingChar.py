#User function Template for python3

class Solution:
    def FirstNonRepeating(self, A):
        
        # Code here
        n=len(A)
        stack=[]
        l=''
        d=''
        for i in range(n):
         
            if A[i] in stack:
                if A[i]==stack[0]:
                    stack.pop(0)
                    if len(stack)>0:
                        l=l+stack[0]
                    else:
                        l=l+'#'
                        
                else:
                    stack.remove(A[i])
                    l=l+stack[0]
            else:
                if A[i] not in d:
                    stack.append(A[i])
                    d=d+A[i]
                    l=l+stack[0]
                else:
                    
                    if len(stack)>0:
                        l=l+stack[0]
                    else:
                        l=l+'#'
        return l


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends