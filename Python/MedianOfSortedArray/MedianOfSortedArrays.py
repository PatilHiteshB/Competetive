#User function Template for python3

class Solution:
    def MedianOfArrays(self, arr1, arr2):
            #code here
            
            n, m = len(arr1), len(arr2)
            
            if n > m:
                
                return self.MedianOfArrays(arr2, arr1)
            
            count = (n+m+1)//2
            
            low, high = 0, n
            
            while low <= high:
                
                cut1 = (low+high)//2
                cut2 = count - cut1
                
                l1 = -1 if cut1-1 < 0 else arr1[cut1-1]
                l2 = -1 if cut2-1 < 0 else arr2[cut2-1]
                r1 = 10**5+1 if cut1 >= n else arr1[cut1]
                r2 = 10**5+1 if cut2 >= m else arr2[cut2]
                
                if l1 <= r2 and l2 <= r1:
                    
                    if (n+m)&1 == 1:
                        return max(l1, l2)
                    
                    ans = max(l1, l2) + min(r1, r2)
                    
                    if ans&1 == 1:
                        return ans/2
                    return ans//2
                    
                if l1 > r2:
                    
                    high = cut1 - 1
                
                else:
                    
                    low = cut1 + 1
                    
            return -1
                
                
            
            
                    
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends