#User function Template for python3
class Solution:
    
    def ispalindrome(self,num,n):
        i=0
        j=n-1
        while i<j:
            if num[i]!=num[j]:
                return False
            i+=1
            j-=1
        return True
        
    def addOne(self,num,n,r):
        num[r]+=1
        while r>0 and num[r]>9:
            num[r]=0 
            num[r-1]=num[r-1]+1 
            r-=1
        if r==0 and num[r]>9:
            num.insert(0,1)
            num[1]=0
        return num
        
        
    def generateNextPalindrome(self,num, n ) :
        if n==1:
            if num[0]!=9:
                num[0]+=1
                return num
            else:
                num=[1,1]
                return num
        
        num=self.addOne(num,n,n-1)
        n=len(num)
        while not self.ispalindrome(num,n):
            i=0
            j=n-1
            while i<j:
                if num[i]==num[j]:
                    i+=1
                    j-=1
                elif num[i]>num[j]:
                    num[j]=num[i]
                else:
                    num=self.addOne(num,n,j)
                    
        return num
#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        num=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends