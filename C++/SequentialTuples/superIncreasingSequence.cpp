	#include<bits/stdc++.h>
	using namespace std;
	#define TYPE long

	TYPE possibleTuples(TYPE N){
		if(N==1) return 1;
		if(N==2) return 4;
		if(N==3) return 10;
		return (N-2)*9;
	}

	int main(){
		TYPE N; cin >> N;
		while(N--){
			TYPE X; cin >> X;
			cout << possibleTuples(X) << endl;
		}
	}