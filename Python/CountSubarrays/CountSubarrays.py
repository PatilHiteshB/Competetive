#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        i = 0
        j = 0
        pro = 1
        ans = 0
    
        while i < n:
            pro *= a[i]
        
            while j <= i and pro >= k:
                pro /= a[j]
                j += 1
        
            ans += (i - j + 1)
            i += 1
    
        return ans
    
    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends