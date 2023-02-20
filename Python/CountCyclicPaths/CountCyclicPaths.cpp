//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function Template for C++

class Solution{   
public:
    int countPaths(int N){
        // code here 
        long m = 1000000000 + 7;
        long o = 0, a, b, c;
        a = b = c = 1;
        
        long ans = 0;
        for(long i=2; i<=N; i++) {
            long ways2o = (a+b+c)%m;
            long ways2a = (ans+b+c)%m;
            long ways2b = (ans+a+c)%m;
            long ways2c = (ans+b+a)%m;
            
            ans = ways2o;
            a = ways2a;
            b = ways2b;
            c = ways2c;
            
        }
        
        return ans%m;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin >> N;
        
        Solution ob;
        cout << ob.countPaths(N) << endl;
    }
    return 0; 
}

// } Driver Code Ends