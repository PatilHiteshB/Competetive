#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        dic={}
        ans=0
        result=-1
        i=0
        j=0
        while i < (len(s)):
            if s[i] not in dic:
                dic[s[i]]=1
                
            else:
                dic[s[i]]+=1
            if len(dic)==k:
                ans=sum(dic.values())
            while len(dic)>k:
                dic[s[j]]-=1
                ans-=1
                if dic[s[j]]==0:
                    del dic[s[j]]
                j+=1
            result=max(ans,result)
            i+=1
        if result==0:
            return -1
        return result
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends