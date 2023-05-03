from typing import List


class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        # code here
        
        mp = {}
        for i in arr:
            if i in mp: mp[i] += 1
            else: mp[i] = 1
        
        count = 0    
        for i in mp.keys():
            rev = i[::-1]
            if rev in mp:
                
                if mp[i] != mp[rev]:
                    return False
                
                if i == rev:
                    
                    if mp[i]%2 == 1:
                        count += 1
                        
                    if count > 1:
                        return False
            
            else:
                return False
                
        return True
        



#{ 
 # Driver Code Starts
class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=StringArray().Input(n)
        
        obj = Solution()
        res = obj.makePalindrome(n, arr)
        
        result_val = "YES" if res else "NO"
        print(result_val)

# } Driver Code Ends