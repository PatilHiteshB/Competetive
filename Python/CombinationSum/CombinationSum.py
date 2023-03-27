#User function Template for python3

class Solution:
    def solve(self, arr, index, target, some, lst, ans):
        
        if some <= 0 or index >= len(arr) or some - arr[index] < 0:
            return
        
        if some - arr[index] == 0:
            # print(lst+[arr[index]])
            ans.add(tuple(lst+[arr[index]]))
            return
            
        if some - arr[index] > 0:
            
            self.solve(arr, index+1, target, some-arr[index], lst+[arr[index]], ans)
            self.solve(arr, index+1, target, some, lst, ans)
            
        
        
    def combinationSum2(self, arr, target):
        # Code here
        arr.sort()
        ans = set()
        self.solve(arr, 0, target, target, [], ans)
        return list(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, target = list(map(int, input().split()))
        candidates = list(map(int, input().split()))
        ob = Solution()
        res = ob.combinationSum2(candidates, target)
        res.sort()
        print('[ ', end = '')
        for subset in res:
            print('[ ', end = '')
            for val in subset:
                print(val, end = ' ')
            print(']', end = '')
        print(' ]')
# } Driver Code Ends