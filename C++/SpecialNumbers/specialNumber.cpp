#include<bits/stdc++.h>
using namespace std;

bool isSpecial(int num){
    int n=num%10;
    while(num){
        if(n>(num%10)){
            return false;
        }
        num/=10;
    }
    return true;
}

int main(){
    int array_length; cin >> array_length;
    int count=0;
    for(auto i=0; i<array_length; i++){
        int num; cin >> num;
        count+= isSpecial(num);
    }
    
    cout << count << endl;
    return 0;
}