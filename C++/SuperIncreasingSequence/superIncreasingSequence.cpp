#include<bits/stdc++.h>
using namespace std;

bool isSuperIncreasing(vector<int> vctor){
    int sum=0; 
    for(int i=0; i<vctor.size(); i++){
        if(sum>vctor[i])
            return false;
        sum+=vctor[i];
    }
    return true;
}

int main(){
    int N; cin >> N;
    vector<int> vctor;
    for(int i=0; i<N; i++){
        int temp; cin >> temp;
        vctor.push_back(temp);
    }

    cout << ((isSuperIncreasing(vctor) == 1) ? "true" : "false");
    return 0;
}