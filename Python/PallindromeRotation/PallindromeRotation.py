#User function Template for python3

class Solution:
    def isRotatedPalindrome(self, s):
        l = [0] * 26
        for i in range(len(s)):
            l[ord(s[i])-ord('a')] += 1
        
        #Try, if the number ob symbols is enought for palidrom.
        count = 0
        for i in range(len(l)):
            if l[i] % 2 == 1 and count > 1:
                return 0
                
            if l[i] % 2 == 1:
                count += 1
        
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.isRotatedPalindrome(s)
		print(answer)
		
# } Driver Code Ends