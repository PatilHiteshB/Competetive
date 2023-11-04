#User function Template for python3

class Solution:
    def indexes(self, arr, el):
        def helper(arr):
            nonlocal first
            s, e = 0, len(arr)-1
            while s <= e:
                mid = (s+e)//2
                if el == arr[mid]:
                    if first:
                        if mid == 0 or el > arr[mid-1]:
                            first = False
                            return mid
                        else:
                            e = mid-1
                    else:
                        if mid == len(arr)-1 or el < arr[mid+1]:
                            first = True
                            return mid
                        else:
                            s = mid+1
                
                elif el < arr[mid]:
                    e = mid-1
                else:
                    s = mid+1
            
            return -1
        
        first = True
        return (helper(arr), helper(arr))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends