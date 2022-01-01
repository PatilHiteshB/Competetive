#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, sum, avg; cin >> N;
    vector<int> vctor;
    
    sum=0;
    for (int i = 0; i < N; i++) {
        int n; cin >> n;
        vctor.push_back(n);
        sum+=vctor[i];
    }
    
    assert(sum%N == 0);
    avg=sum/N;
    
    sum=0;
    for (int i = 0; i < N; i++)
        if(vctor[i]>avg)
            sum+=(vctor[i]-avg);
            

    cout << sum; return 0;
}