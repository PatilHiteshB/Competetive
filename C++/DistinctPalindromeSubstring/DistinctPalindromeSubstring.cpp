//{ Driver Code Starts
// C++ program to find all distinct palindrome sub-strings
// of a given string
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution{
  public:
    int palindromeSubStrs(string s) {
        int n = s.size();
        vector < vector <bool> > dp(n, vector <bool>(n, false));
        unordered_set <string> st;
        
        for(int i = 0; i < n; i++)
            dp[i][i] = true;
        
        for(int i = n - 1; i >= 0; i--) {
            for(int j = i + 1; j < n; j++) {
                if(s[i] == s[j] && (j - i == 1 || dp[i + 1][j - 1])) {
                    string str = s.substr(i, j - i + 1);
                    dp[i][j] = true;
                    st.insert(str);
                }
            }
        }
      int cnt = st.size();
      unordered_map <char, int> mp;
      for(auto x: s) mp[x]++;
      for(auto x: mp) cnt++;
      
      return cnt;
    }
};

//{ Driver Code Starts.

// Driver program
int main() {
    int t;
    cin >> t;
    while (t--) {
        string str;
        cin >> str;
        Solution ob;
        cout << ob.palindromeSubStrs(str) << endl;
    }
    return 0;
}

// } Driver Code Ends