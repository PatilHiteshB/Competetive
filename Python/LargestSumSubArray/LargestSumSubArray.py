#User function Template for python3

class Solution():
    
    def maxSumWithK(self, a, n, k):
        # Code here
        i = 0
        j = 0
        sum1 = 0
        last = 0
        ans = float('-inf')
        for i in range(n):
            sum1 = sum1 + a[i]
            if (i-j) + 1 == k:
                ans = max(ans, sum1)
            elif (i-j) + 1 > k:
                last = last + a[j]
                j = j + 1
                if last < 0:
                    sum1 = sum1 - last
                    last = 0
                ans = max(ans, sum1)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends