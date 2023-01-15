#User function Template for python3


class Solution():
    
    def merge(self, l, mid, r, arr, temp):
        
        i = l
        j = mid
        k = l
        
        count = 0
        while i<mid and j<=r:
            
            if arr[i] < arr[j]:
                
                count += (mid-i)
                temp[k] = arr[j]
                
                k+=1
                j+=1
                
            else:
                
                temp[k] = arr[i]
                k += 1
                i +=1
                
        
        while i<mid:
            temp[k] = arr[i]
            k += 1
            i += 1
            
        while j<=r:
            temp[k] = arr[j]
            k += 1
            j += 1
            
        for i in range(l, r+1):
            arr[i] = temp[i]
            

            
        return count
        
    def mergeSort(self, l, r, arr, temp):
        
        if l > r:
            return 0
        
        if l == r:

            return 1 if arr[l] > 0 else 0
            
        mid = (l+r)//2
        left = self.mergeSort(l, mid, arr, temp)
        right = self.mergeSort(mid+1, r, arr, temp)
        
        total = left + right
        
        total += self.merge(l, mid+1, r, arr, temp)
        
        
        return total
        
    def countSubstring(self, S, index=0):
        #your code here
        N = len(S)
        
        arr = [1 if S[0] == "1" else -1]
        
        for i in range(1, N):
            
            if S[i] == "1":
                arr.append(arr[-1]+1)
            else:
                arr.append(arr[-1]-1)
                
        
        return self.mergeSort(0, N-1, arr, [0]*N)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().countSubstring(s))
# } Driver Code Ends