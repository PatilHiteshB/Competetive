#User function Template for python3

def maxSumWithK( arr, n, k):
    
    su = 0
    
    for i in range(k):
        
        su += arr[i]
        
    answer = su
    last = start = 0
    end = k
    
    while end < n:
        
        last += arr[start]
        start += 1
        
        su += arr[end]
        answer = max(answer, su)
        
        if last < 0:
            su = su - last
            answer = max(answer, su)
            last = 0
            
        end+=1
        
    return answer
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        print(maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends