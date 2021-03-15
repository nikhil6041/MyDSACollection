#include <bits/stdc++.h>

using namespace std;

int main(){
    int N , H , X ;
    bool flg = false; 
    // input
    
    cin >> N >> H >> X ;
    //cout << "N = " << N << " H = " << H << " X = " << X << "\n";
    
    int timedifference = H - X ;  // always positive
    
    int tmp ;
    for( int i = 0; i < N ; i++){
        cin >> tmp;
        if (tmp == timedifference){
            flg = true;
        }
    }

    // output 
    if (flg){
        cout << "YES";
    }
    else{
        cout << "NO";
    }
    return 0;
}