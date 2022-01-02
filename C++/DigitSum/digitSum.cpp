#include<bits/stdc++.h>
using namespace std;

int getSumDigits(int num){
    int sum=0;
    assert(num >= 0);
    while(num){
        sum+=num%10;
        num/=10;
    }
    return sum;
}

int main() {
    int T; cin >> T;
    while(T--){
        int N; cin >> N;
        int sum=0;
        while(N--) {
            int n; cin >> n;
            sum+=n;
        }
        while((sum=getSumDigits(sum)) >= 10);
        cout << sum << endl;
    }
    return 0;
}