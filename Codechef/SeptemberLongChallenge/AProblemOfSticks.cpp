#include<bits/stdc++.h>

using namespace std;

bool countzeros(long long int arr[],int size){
    int c = 0;
    for (int  i = 0 ; i < size ; i++){

        if (arr[i] == 0){
            c++;
        }

    }

    return (c==size);
}

long long int findSecondMax(long long int arr[],int n){

    int max = -1;
    for (int i = 0 ; i < n ; i++){
        if (max < arr[i]){
            max = arr[i];
        }
    }
    int secondmax = max;

    for (int i = 0 ;i < n ; i++){
        if(secondmax < arr[i] and arr[i]!=max){
            secondmax = arr[i];
        }
    }

    return secondmax;
}
int main(){
    int t;
    cin >> t;

    for ( int i = 0 ; i < t ; i++){

        long long int n ;

        cin >> n;

        long long int a[n];

        for (int j = 0 ; j < n ; j++ ){
            cin >> a[j];
        }

        int cnt = 0;
        long long int smx;
        while (!countzeros(a,n)){
            smx  = findSecondMax(a,n);

            for(int i = 0 ; i < n ; i++ ){
                if (a[i] > smx){
                    a[i] = a[i] - smx;
                }
            }
            cnt++;
            cout << cnt << endl;

        }
        cout << cnt << endl;
    }

    return 0;
}