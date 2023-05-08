#User function Template for python3

class Solution():
    def modulo(self, s, m):
        #your code goes here
        n = 0
        for i in s:
            n += int(i)
            n <<= 1
            
        return (n>>1)%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s,m = input().split()
        m = int(m)
        print(Solution().modulo(s, m))

# } Driver Code Ends