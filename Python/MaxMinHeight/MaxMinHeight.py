#User function Template for python3


class Solution:
    def maximizeMinHeight(self, n, k, w, a):
        mn = min(a)
        mx = mn + k + 1
        
        def f(ht):
            days = 0
            curr_ht = a[0]
            flower = [0] * (n + 1)
            
            diff = max(0, ht - curr_ht)
            flower[0] += diff
            days += diff
            flower[w] -= diff
            
            for i in range(1, n):
                flower[i] += flower[i - 1]
                curr_ht = a[i] + flower[i]
                
                diff = max(0, ht - curr_ht)
                flower[i] += diff
                days += diff
                
                if i + w < n:
                    flower[i + w] -= diff
            
            return days <= k
        
        while mn < mx:
            ht = (mn + mx) // 2
            if not f(ht):
                mx = ht
            else:
                mn = ht + 1
                
        return mn - 1

            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n,k,w = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(Solution().maximizeMinHeight(n, k, w,arr))

# } Driver Code Ends