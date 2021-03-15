#include <bits/stdc++.h>

using namespace std;
long int countgroups(string s){
    long int c = 0;
    int i = 1;
    int n = s.length();
    char prev = s[0], current ;
    
    if (prev == '1'){
        c = 1;
    }
    while (i < n){
        current = s[i];
        if (prev == '0' and current == '1'){
            c++;
        }
        prev = current;
        i++;
    }
    return c;
}
int main(){
    int T;
    string S;
    //input
    cin >> T;
    for (int i = 0 ; i < T ; i++ ){
        cin >> S;
        // cout << S;
        //output
        // cout << "count = " << countgroups(S) << endl;
        cout << countgroups(S) << endl;
    }
    return 0;
}