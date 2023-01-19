#User function Template for python3


class Solution:
    def carpetBox(self, A,B,C,D):
        #code here
        
        answer1 = answer2 = 0
        
        Lt = A
        Bt = B
        
        while Lt > C:
            Lt //= 2
            answer1 += 1
            
        while Bt > D:
            Bt //= 2
            answer1 += 1
            
        Lt = B
        Bt = A
        
        while Lt > C:
            Lt //= 2
            answer2 += 1
            
        while Bt > D:
            Bt //= 2
            answer2 += 1
            
            
        
        return min(answer1, answer2)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            A,B,C,D = map(int, input().split())
            
            obj = Solution()
            print(obj.carpetBox(A,B,C,D))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends